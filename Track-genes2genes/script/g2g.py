### Date: 250813

import os
import anndata
import numpy as np
import pandas as pd
import seaborn as sb
import numpy as np
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

from genes2genes import Main
from genes2genes import ClusterUtils
from genes2genes import TimeSeriesPreprocessor
from genes2genes import PathwayAnalyser
from genes2genes import VisualUtils

import argparse
parser = argparse.ArgumentParser(
    description='Gene-to-gene alignment with default paths & threshold'
)
parser.add_argument(
    '--h5ad_ref',
    default='/data/work/cotton/cellrank2/test5/K2_cr2_cytotrace.h5ad',
    help='Path to reference h5ad (default: K2_cr2_cytotrace.h5ad)'
)
parser.add_argument(
    '--h5ad_query',
    default='/data/work/cotton/cellrank2/test5/C1_cr2_cytotrace.h5ad',
    help='Path to query h5ad (default: C1_cr2_cytotrace.h5ad)'
)
parser.add_argument(
    '--distance_threshold',
    type=float,
    default=0.50,
    help='Distance threshold (default: 0.50)'
)

args = parser.parse_args()
h5ad_ref  = args.h5ad_ref
h5ad_query = args.h5ad_query
distance_threshold  = args.distance_threshold



adata_ref = anndata.read_h5ad(h5ad_ref) # Reference dataset
adata_query = anndata.read_h5ad(h5ad_query) # Query dataset
prefix_ref = os.path.splitext(os.path.basename(h5ad_ref))[0]
prefix_query = os.path.splitext(os.path.basename(h5ad_query))[0]

print(adata_ref); print(adata_query)

print('-------------------- 1. Preparing data for alignment ---------------------')
adata_ref.obs['time'] = adata_ref.obs['ct_pseudotime']
adata_query.obs['time'] = adata_query.obs['ct_pseudotime']
print(min(adata_ref.obs['time']), max(adata_ref.obs['time']))
print(min(adata_query.obs['time']), max(adata_query.obs['time']))

sb.kdeplot(adata_ref.obs['time'], fill=True, label=f'Reference - {prefix_ref}', color='forestgreen') 
sb.kdeplot(adata_query.obs['time'], fill=True, label=f'Query - {prefix_query}', color='midnightblue'); 
plt.xlabel('pseudotime'); plt.legend() 
plt.savefig(f'pseudotime_{prefix_ref}_vs_{prefix_query}.pdf', bbox_inches='tight')
plt.show()
plt.close('all')

from optbinning import ContinuousOptimalBinning

x = np.asarray(adata_ref.obs.time)
optb = ContinuousOptimalBinning(name='pseudotime', dtype="numerical")
optb.fit(x, x)
print(len(optb.splits))
n_bins = len(optb.splits) # Bins of Reference as a standard

x = np.asarray(adata_query.obs.time)
optb = ContinuousOptimalBinning(name='pseudotime', dtype="numerical")
optb.fit(x, x)
print(len(optb.splits))

VisualUtils.plot_pseudotime_dists_with_interpolation_points(adata_ref, adata_query, n_bins)
plt.savefig(f'pseudotime_point_{prefix_ref}_vs_{prefix_query}.pdf', bbox_inches='tight')
plt.close('all')

print('-----------------------2. G2G trajectory alignment -----------------------')
# define the gene list to align 必须两者都存在的基因
hv_ref   = adata_ref.var_names[adata_ref.var['highly_variable']]
hv_query = adata_query.var_names[adata_query.var['highly_variable']]
common_genes = hv_ref.intersection(hv_query)
gene_list = common_genes
print(len(gene_list),'genes')

aligner = Main.RefQueryAligner(adata_ref, adata_query, gene_list, n_bins) # aligner
aligner.align_all_pairs()

aligner.get_aggregate_alignment()
plt.savefig(f'aggregate_alignment_{prefix_ref}_vs_{prefix_query}.pdf', bbox_inches='tight')
plt.close('all')

df = aligner.get_stat_df() # ordered genes according to alignment similarity statistics 
plt.savefig(f'ranking_genes_{prefix_ref}_vs_{prefix_query}.pdf', bbox_inches='tight')
plt.close('all')

print(df)
print('Ten genes of the lowest similarity: ')
print(df['Gene'][1:10])
df.to_csv(f"ranking_genes__{prefix_ref}_vs_{prefix_query}.csv", index=False)

VisualUtils.plot_alignmentSim_vs_l2fc(df)
plt.savefig(f'ranking_genes_log2_{prefix_ref}_vs_{prefix_query}.pdf', bbox_inches='tight')
plt.close('all')

earliest_match_sorted_genes_list = aligner.show_ordered_alignments()
# with open('alignment_results.txt', 'w') as f:
#     for gene in earliest_match_sorted_genes_list:
#         gene_obj = aligner.results_map[gene]
#         alignment_str = gene_obj.alignment_str
#         f.write(f'{gene} {alignment_str}\n')

# ----------------- Gene-set overrepresentation analysis on the top dissimilar genes -------------
threshold_similarity = 0.3
topDEgenes = df[df['alignment_similarity_percentage'] <= threshold_similarity]['Gene']
# print(topDEgenes); print(len(topDEgenes))
#可以做一个enrich看最不相似的基因主要富集到什么功能
os.makedirs("topDEgenes", exist_ok=True)
with open('topDEgenes/topDEgenes.txt', 'w') as f:
    for gene in topDEgenes[:10]:
        gene_obj = aligner.results_map[gene]
        alignment_str = gene_obj.alignment_str
        f.write(f'{gene} {alignment_str}\n')
        # 1) 打印对齐字符串和彩色版本
        print(alignment_str)
        print(VisualUtils.color_al_str(alignment_str))
        print()
        print(gene_obj.al_visual)
        # 2) 画 alignment landscape
        gene_obj.landscape_obj.plot_alignment_landscape()
        plt.savefig(
            f'topDEgenes/plot_cost_{gene}_{prefix_ref}_vs_{prefix_query}.pdf',
            bbox_inches='tight'
        )
        plt.close('all')
        # 3) 画 time series（带细胞）
        VisualUtils.plotTimeSeries(gene, aligner, plot_cells=True)
        plt.savefig(
            f'topDEgenes/plotTimeSeries_{gene}_{prefix_ref}_vs_{prefix_query}.pdf',
            bbox_inches='tight'
        )
        plt.close('all')



print('----------------------------3. Clustering alignments ---------------------')
df = ClusterUtils.run_clustering(aligner, metric='levenshtein', experiment_mode=True)
plt.savefig(f'clustering_genes_{prefix_ref}_vs_{prefix_query}.pdf', bbox_inches='tight')
plt.close('all')

ClusterUtils.run_clustering(aligner, metric='levenshtein', DIST_THRESHOLD=distance_threshold)
ClusterUtils.visualise_clusters(aligner,n_cols = 4, figsize= (5,3))
plt.savefig(f'clustering_genes_{distance_threshold}_{prefix_ref}_vs_{prefix_query}.pdf', bbox_inches='tight')
plt.close('all')

VisualUtils.plot_distmap_with_clusters(aligner)
plt.savefig(
    f'clustering_distmap_{distance_threshold}_{prefix_ref}_vs_{prefix_query}.png',
    bbox_inches='tight',
    dpi=72          # 清晰度够用且文件小；再降可改成 100 或 72
)
plt.close('all')

# ClusterUtils.print_cluster_average_alignments(aligner)
def get_cluster_average_alignments(aligner, gene_set, deterministic=True):
            cluster_alobjs = []
            for g in gene_set:
                cluster_alobjs.append(aligner.results_map[g])
            i = aligner.results[0].fwd_DP.T_len
            j = aligner.results[0].fwd_DP.S_len
            avg_alignment = ''
            tracked_path = []
            tracked_path.append([i,j])
            while(True):
                if(i==0 and j==0):
                    break
                backtrack_states_probs = {}
                backtrack_states_probs['M'] = 0 
                backtrack_states_probs['W'] = 0 
                backtrack_states_probs['V'] = 0 
                backtrack_states_probs['D'] = 0 
                backtrack_states_probs['I'] = 0 
                # record the count of each state at this [i,j] cell across all alignments 
                for a in cluster_alobjs:
                    backtract_state = a.landscape_obj.L_matrix_states[i,j]
                    if(backtract_state=='0'):
                        backtrack_states_probs['M']+=1 
                    elif(backtract_state=='1'):
                        backtrack_states_probs['W']+=1 
                    elif(backtract_state=='2'):
                        backtrack_states_probs['V']+=1 
                    elif(backtract_state=='3'):
                        backtrack_states_probs['D']+=1 
                    elif(backtract_state=='4'):
                        backtrack_states_probs['I']+=1 
                # compute the proportion of the state for the [i,j] cell
                for state in backtrack_states_probs.keys(): 
                    backtrack_states_probs[state] = backtrack_states_probs[state]/len(cluster_alobjs) 
                if(deterministic):
                    # take the most probable state based on max frequent state of this [i,j] cell
                    cs = np.argmax(np.asarray(list(backtrack_states_probs.values())) )
                else:
                    # sample a state from the state frequency distribution
                    cs = Utils.sample_state(np.asarray(list(backtrack_states_probs.values()) ) )
                if(cs==0):
                    i = i-1
                    j = j-1
                    avg_alignment = 'M' + avg_alignment 
                elif(cs==1 or cs==3):
                    j= j-1
                    if(cs==1):
                        avg_alignment = 'W' + avg_alignment
                    else:
                        avg_alignment = 'D' + avg_alignment
                elif(cs==2 or cs==4):
                    i=i-1
                    if(cs==2):
                        avg_alignment = 'V' + avg_alignment
                    else:
                        avg_alignment = 'I' + avg_alignment
                tracked_path.append([i,j])
            return avg_alignment, tracked_path

def print_cluster_average_alignments(aligner):
    aligner.gene_clusters_average_alignments = {}
    for i in range(len(aligner.gene_clusters)):
        average_alignment, avg_path =  get_cluster_average_alignments(aligner, aligner.gene_clusters[i] )
        print('cluster: ', i, average_alignment, '(',len(aligner.gene_clusters[i]), 'genes)')
        aligner.gene_clusters_average_alignments[i] = average_alignment


print_cluster_average_alignments(aligner)

# # To access the genes in a particular cluster
# cluster_id = 0
# print(aligner.gene_clusters[cluster_id]) 

# # To print all gene alignments in the cluster
# aligner.show_cluster_alignment_strings(cluster_id)

# ---------------- Clustering genes with df -----
records = []
for cluster_id, gene_list in aligner.gene_clusters.items():
    for gene in gene_list:
        gene_obj   = aligner.results_map[gene]
        alignment  = gene_obj.alignment_str
        records.append({
            'gene': gene,
            'cluster': cluster_id,
            'alignment': alignment
        })

df = pd.DataFrame(records)      # 三列：gene、cluster、alignment
print(df.head())
df.to_csv('gene_cluster_alignment.csv', sep='\t', index=False)

# ------------------ subset ------
os.makedirs("cluster", exist_ok=True)
for cluster in df['cluster'].unique():
    print(f"Subset: {cluster}")
    GENE_SUBSET = df[df['cluster'] == cluster]['gene']
    # Average alignment of any given subset of genes
    aligner.get_aggregate_alignment_for_subset(GENE_SUBSET)
    plt.savefig(
        f'cluster/aggregate_alignment_{cluster}_{prefix_ref}_vs_{prefix_query}.pdf',
        bbox_inches='tight'
    )
    plt.close('all')
    

# ----------------------- Save log.txt ---------------------
import sys
from contextlib import redirect_stdout

# 打开一个追加模式文件
log_file = open('log.txt', 'a', buffering=1)  # buffering=1 行缓冲，实时写盘
with redirect_stdout(log_file):
    aligner.get_aggregate_alignment()
    print()
    df = aligner.get_stat_df()
    print()
    print_cluster_average_alignments(aligner)
    


log_file.close()

# ---------------------- How to save aligner file? -------------
import pickle

with open(f'aligner_{prefix_ref}_vs_{prefix_query}.pkl', 'wb') as f:
    pickle.dump(aligner, f)
    
# with open('aligner.pkl', 'rb') as f:
#     aligner = pickle.load(f)
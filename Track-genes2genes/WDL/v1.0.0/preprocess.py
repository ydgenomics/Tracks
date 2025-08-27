### Date: 250827

import scanpy as sc
import os
import argparse

parser = argparse.ArgumentParser(description="Preprocess an h5ad file.")
parser.add_argument("--input_h5ad", type=str, required=True,
                    help="Path to the input h5ad file.")
parser.add_argument("--batch_key", type=str, default="sample",
                    help="Batch key in adata.obs (default: 'sample').")
parser.add_argument("--n_hvg", type=int, default=2000,
                    help="Number of highly variable genes (default: 2000).")

args = parser.parse_args()
input_h5ad = args.input_h5ad
batch_key = args.batch_key
n_hvg = args.n_hvg


adata = sc.read_h5ad(input_h5ad)
prefix = os.path.splitext(os.path.basename(input_h5ad))[0]
print(adata.obs.columns)
if 'counts' in adata.layers:
    print("# Using raw data of adata.layers['counts']")
    adata.X = adata.layers['counts'].copy()
else: 
    print("# Using adata.X directly")

# Normalizing to median total counts
sc.pp.normalize_total(adata)
# Logarithmize the data
sc.pp.log1p(adata)

if batch_key in adata.obs.columns:
    sc.pp.highly_variable_genes(adata, n_top_genes=n_hvg, batch_key=batch_key)
else: 
    adata.obs[batch_key] = "single_batch"
    sc.pp.highly_variable_genes(adata, n_top_genes=n_hvg, batch_key=batch_key)

# sc.tl.pca(adata)
sc.pp.neighbors(adata, use_rep='X_pca')
sc.tl.umap(adata)
print(adata.X[1:10,1:10])
adata.write_h5ad(f"{prefix}.h5ad",compression='gzip')
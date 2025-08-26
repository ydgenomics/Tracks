input_h5ad="/data/users/yangdong/yangdong_faff775391984da0a355d4bd70217714/online/cotton/output/convert/merge/r0.5/cotton_K2.hr.rds.rh.h5ad"
batch_key="sample"
n_hvg=2000

import scanpy as sc
import os
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
### Ref: [monocle3推断发育轨迹](https://mp.weixin.qq.com/s/-EAaTE312J3Bnah7HDJDEA)
library(monocle3)
library(dplyr) # imported for some downstream data manipulation

# expression_matrix <- readRDS(url("https://depts.washington.edu:/trapnell-lab/software/monocle3/celegans/data/cao_l2_expression.rds"))
# cell_metadata <- readRDS(url("https://depts.washington.edu:/trapnell-lab/software/monocle3/celegans/data/cao_l2_colData.rds"))
# gene_annotation <- readRDS(url("https://depts.washington.edu:/trapnell-lab/software/monocle3/celegans/data/cao_l2_rowData.rds"))
seu <- readRDS("data/celegans_seurat.rds") # load the seurat object
expression_matrix <- GetAssayData(scRNAsub, layer="counts", assay ="RNA")
cell_metadata <- seuratObj@meta.data
gene_annotation <- data.frame(gene_short_name = rownames(expression_matrix))
rownames(gene_annotation) <- rownames(expression_matrix)

cds <- new_cell_data_set(expression_matrix,cell_metadata = cell_metadata,gene_metadata = gene_annotation) # create a monocle object
cds <- preprocess_cds(cds, method ="PCA",num_dim = 20)
plot_pc_variance_explained(cds)
cds <- reduce_dimension(cds) #cds <- reduce_dimension(cds,reduction_method='UMAP',preprocess_method = 'PCA')
plot_cells(cds)
plot_cells(cds, color_cells_by="cao_cell_type")
plot_cells(cds, genes=c("cpna-2", "egl-21", "ram-2", "inos-1"))

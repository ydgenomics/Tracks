library(CytoTRACE)
library(tidyverse)
library(reticulate)
library(Seurat)

input_rds=""
cluster_key="leiden_res_0.50"
n_cpu=4

seu <- readRDS(inpuut_rds)
table(seu$leiden_res_0.50)

# annotation info
phe <- seu@meta.data[[cluster_key]]
phe <- as.character(phe)
names(phe) <- rownames(seu@meta.data)
# expression matrix
mat <- as.matrix(seu$RNA@counts)
mat[1:4,1:4]

result <- CytoTRACE(mat, phe, ncores=n_cpu)
dev.off()

plotCytoTRACE(result)
dev.off()

plotCytoTRACE(result, gene = "", phenotype=phe)
dev.off()

# 可视化与CytoTRACE相关的基因
plotCytoTRACE(result, numofGenes = 20, phenotype=phe)
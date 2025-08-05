# 学习[cellrank2](https://cellrank.readthedocs.io/en/latest/about/version2.html)

[2024(Nature Method)_CellRank2 unified fate mapping in multiview single-cell data](https://www.nature.com/articles/s41592-024-02303-9)
[cellrank2_reproducibility](https://github.com/theislab/cellrank2_reproducibility)

kernel-transition_matrix-estimator
[CellRank’s key applications](https://cellrank.readthedocs.io/en/latest/index.html#cellrank-s-key-applications)
- Estimate differentiation direction based on a varied number of biological priors, including pseudotime, developmental potential, RNA velocity, experimental time points, and more.
- Compute initial, terminal and intermediate macrostates
- Infer fate probabilities and driver genes.
- Visualize and cluster gene expression trends.
- … and much more, check out our API.

kernel
- [CellRank Meets Pseudotime](https://cellrank.readthedocs.io/en/latest/notebooks/tutorials/kernels/300_pseudotime.html)





# 快速开始

# 配置环境
```shell
# Env: cellrank2
source /opt/software/miniconda3/bin/activate
conda create -n cellrank2 python=3.12 -y
conda activate cellrank2
conda install -c conda-forge cellrank -y
conda install conda-forge::scanpy -y
conda install conda-forge::moscot -y
conda install -c conda-forge -c bioconda palantir -y #python要求3.12
# pip install --user magic-impute
conda install conda-forge::certifi -y
conda install conda-forge::ipykernel -y


# 
python -m ipykernel install --user --name cellrank2 --display-name "Python (cellrank2)"
```
```python
from moscot.problems.time import TemporalProblem
import cellrank as cr
import scanpy as sc
from cellrank.kernels import RealTimeKernel
from cellrank.kernels import PseudotimeKernel
import anndata
import sys
import numpy as np
import scipy
import pandas as pd
import matplotlib
import seaborn
```

# 参考资料
[MAGIC](https://github.com/KrishnaswamyLab/MAGIC)
[Palantir](https://palantir.readthedocs.io/en/latest/notebooks/Palantir_sample_notebook.html)
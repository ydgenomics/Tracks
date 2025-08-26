# 学习[cellrank2](https://cellrank.readthedocs.io/en/latest/about/version2.html)

1. pseudotime: dpt-palantir-cellrank2(PseudotimeKernel)-estimators 起点识别的问题，我们可以用dpt来识别起点，然后再用该起点跑palantir拿到两个pseudotime信息，然后再用cellrank2的kernel拿到plot_projection图 √
2. velocity: scvelo(cr2)-cellrank2(VelocityKernel)-estimators(GPCCA) ×
3. similarity: cellrank2(ConnectivityKernel)
4. cytorace: cytorace(cr2)-cellrank2(CytoTRACEKernel)-estimators(GPCCA) √
5. realtime: moscot(cr2)-cellrank2(RealTimeKernel)-estimators(GPCCA)
6. metabolism


RNA velocity不依赖于起点，我们可以先用velocity kernel去拿到vk，然后用vk做estimator的estimator，estimator做起点和终点的预测，根据起点预测也可以再来跑pseudotime（但是感觉不建议）
CytoTRACE kernel
estimator的功能（起点和终点的识别；细胞命运和决定基因；可视化和基因分群）
- [CellRank Meets RNA Velocity](https://cellrank.readthedocs.io/en/latest/notebooks/tutorials/kernels/200_rna_velocity.html#cellrank-meets-rna-velocity)
- [CellRank Meets Pseudotime](https://cellrank.readthedocs.io/en/latest/notebooks/tutorials/kernels/300_pseudotime.html#cellrank-meets-pseudotime)
- [CellRank Meets CytoTRACE](https://cellrank.readthedocs.io/en/latest/notebooks/tutorials/kernels/400_cytotrace.html)
- [CellRank Meets Experimental Time](https://cellrank.readthedocs.io/en/latest/notebooks/tutorials/kernels/500_real_time.html#cellrank-meets-experimental-time)
- 
cellrank2提供了很好的pseudotime分析接口，我们应该先把这部分分析好。
h5ad--pseudotime(palantir/cytotrace/dpt)--kernerl(2+1)--multi_kernerls(optional)--estimator(GPCCA/)--g(Identify initial & terminal states/Compute fate probabilities and driver genes/Visualize expression trends)

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
# pip install rpy2
conda install conda-forge::rpy2 -y
# pip install fa2-modified
conda install conda-forge::fa2 -y #不支持安装在大于等于3.12python
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
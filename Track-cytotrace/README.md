[cytoTRACE拟时间分析](https://mp.weixin.qq.com/s/UzTKS64ZDtmYF67bzMp0nQ)
[cytotrace](https://cytotrace.stanford.edu/#shiny-tab-dev_cyto)
[cytotrace github](https://github.com/gunsagargulati/CytoTRACE)
```shell
# 复制于别人装好的环境，但是自己测试仍有报错
source /opt/software/miniconda3/bin/activate
conda create -n cytotrace -y
conda activate cytotrace
conda install -c conda-forge r-base==4.2.2 -y
conda install -c conda-forge libxml2-devel-cos7-x86_64 -y
conda install r-xml -y
conda install -c conda-forge libnetcdf -y
conda install conda-forge::r-biocmanager -y
Rscript -e 'BiocManager::install("sva")' -y
Rscript -e 'install.packages("HiClimR")' -y
Rscript -e 'install.packages("ccaPP")' -y
Rscript -e 'install.packages("egg")' -y
Rscript -e 'install.packages("https://cytotrace.stanford.edu/CytoTRACE_0.3.3.tar.gz", repos = NULL, type = "source")' -y
pip install scanoramaCT
pip install numpy

# source /opt/software/miniconda3/bin/activate
# conda create -n cytotrace r-base=4.2 -y
# conda activate cytotrace
# conda install conda-forge::r-devtools -y
# conda install conda-forge::r-pak -y
# wget https://cytotrace.stanford.edu/CytoTRACE_0.3.3.tar.gz
# Rscript -e 'devtools::install_local("CytoTRACE_0.3.3.tar.gz")' #在R=4.3时会报错，尝试4.2
# # ERROR: dependencies ‘sva’, ‘HiClimR’, ‘reticulate’, ‘ggplot2’, ‘egg’, ‘ggpubr’ are not available for package ‘CytoTRACE’
# # rm CytoTRACE_0.3.3.tar.gz
# # pip install scanoramaCT update #Runing below codes when this command error
# pip install --use-pep517 scanoramaCT update #`--use-pep517` | **强制使用 PEP 517 构建后端**。某些包（尤其是纯 pyproject.toml 项目）在不加该标志时可能退回到 legacy `setup.py install`，容易失败；加 `--use-pep517` 可以规避这类兼容性问题
# pip install numpy
# conda install conda-forge::r-optparse -y
# conda install conda-forge::r-seurat -y
# conda install conda-forge::r-reticulate -y
```

```R
library(CytoTRACE)
# library(export)
library(tidyverse)
library(reticulate)
# library(SeuratData) 
library(Seurat)
```

## 尝试安装cytotrace2
```R
cytotrace2
function (input, species = "mouse", is_seurat = FALSE, slot_type = "counts", 
    full_model = FALSE, batch_size = 10000, smooth_batch_size = 1000, 
    parallelize_models = TRUE, parallelize_smoothing = TRUE, 
    ncores = NULL, max_pcs = 200, seed = 14) 
# species只支持mouse和human，故不能用cytotrace2
```
[单细胞拟时序分析之CytoTRACE2：解决找不到分化起点的烦恼](https://mp.weixin.qq.com/s/AF-GJZKAttaU8t37BaL5ag)
```shell
# library(CytoTRACE2) #loading
source /opt/software/miniconda3/bin/activate
conda create -n cytotrace2 r-base=4.3 -y
conda activate cytotrace2
conda install conda-forge::r-seurat -y
conda install conda-forge::r-reticulate -y
conda install dnachun::r-cytotrace2 -y # R要大于4.2
```
# Pseudotime analysis with three methods
- **Brief** 使用三种方法做拟时序分析
- **Log**
  - v1.0.0
    - 250903 第一次提交Description
- **Related** Merge_Subset, Convert, Track-g2g

---
# Input
- **Variable**
  - **h5ad_subset** 某一细胞类群的h5ad文件，.X为原始数据或包含.layers['counts'], 包含亚群信息，是从h5ad_all取子集获得而来的
  - **batch_key** h5ad文件中储存潜在的批次的键，例如biosample等，用于scanpy标准化处理找hvg指定batch
  - **cluster_key** h5ad_subset储存亚群信息的键名，例如RNA_snn_res.0.5
  - **h5ad_all** 带有所有细胞类型的h5ad文件，h5ad_subset是从中取子集获得的
  - **cluster_key_all** 储存细胞分群信息的键，例如用于分群注释lenden_res_0.50
  - **tool4pseudotime** 选取用于pseudotime分析的工具，可选(cytotrace,dpt,palantir),如果想运行多个，就将其按,连接即可。例如想运行cytotrace和dpt则输入cytotrace,dpt
  - root_cluster 非必填项，如果运行**dpt**则这一个是必填项。早期细胞cluster信息
  - n_pc 非必填项，如果运行**dpt**则这一个是必填项。使用diffusion map的第几个pc(principal component)
  - use_argmin 非必填项，如果运行**dpt**则这一个是必填项。是否取n_pc的最小值为root细胞，填"yes" or "no"。
  - root_idx 非必填项，如果运行**palantir**则这一个是必填项。起点细胞的index，从dpt中获得
  - **mem_preprocess** preprocess所使用的内存资源GB
  - **mem_pseudotime** pseudotime所使用的内存资源GB

**Note:** cytotrace是无监督方法，使用的参数最少；dpt方法使用的参数很多，可以找到起点细胞；palantir依赖于起点细胞，可以通过多次运行dpt找到最佳的起点细胞后再跑palantir

- **Example** [download]()

|EntityID|h5ad_subset|batch_key|cluster_key|h5ad_all|cluster_key_all|tool4pseudotime|root_cluster|n_pc|use_argmin|root_idx|mem_preprocess|mem_pseudotime|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|test|/Files/yangdong/wdl/SCP/Convert/W202508270039982/cotton_G3.hr.rds.rh.h5ad|sample|RNA_snn_res.0.5|/Files/yangdong/wdl/Track-pseudotime/cotton_G3.h5ad|leiden_res_0.50|palantir||||294|4|8|

---
# Output
- **Frame**
```shell
tree /data/input/Files/yangdong/wdl/Track-pseudotime/W202508270146490
/data/input/Files/yangdong/wdl/Track-pseudotime/W202508270146490
├── input.json
└── pseudotime
    ├── cotton_G3.hr.rds.rh_palantir.h5ad
    └── palantir_cotton_G3.hr.rds.rh.h5ad_executed.ipynb

2 directories, 3 files
```
- **Interpretation**
  - palantir_*.ipynb palantir结果的notebook，可视化文件都在其中，同时也便于个性分析快速运行
  - *_palantir.h5ad 带有palantir_pseudotime键的h5ad文件
- **Next**
  - Enrich 对找到的时序差异基因做基因富集
  - Track-g2g 做时序比较分析
---
# Detail
- **Pipeline** 
  - preprocess 做scanpy标准化处理，保证.X是标准化处理的数据且具有高变基因信息，默认找2000 hvgs
  - pseudotime 做拟时序分析，根据tool4pseudotime判断要做那些拟时序 代码参加cellrank2[codes](https://github.com/theislab/cellrank2_reproducibility/tree/main/notebooks/cytotrace_kernel/embryoid_body)
- **Software**
  - CytoTRACE
  - DPT
  - palantir
- **Script**
  - [cytotrace.ipynb]()
  - [dpt.ipynb]()
  - [palantir.ipynb]()
- **Image**
  - cellrank2--04, cellrank2--03

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

---
# Reference & Citation
- Cytotrace [Gulati, G. S., Sikandar, S. S., Wesche, D. J., Manjunath, A., Bharadwaj, A., Berger, M. J., Ilagan, F., Kuo, A. H., Hsieh, R. W., Cai, S., Zabala, M., Scheeren, F. A., Lobo, N. A., Qian, D., Yu, F. B., Dirbas, F. M., Clarke, M. F., & Newman, A. M. (2020). Single-cell transcriptional diversity is a hallmark of developmental potential. Science (New York, N.Y.), 367(6476), 405–411. https://doi.org/10.1126/science.aax0249](https://drive.google.com/file/d/19JKGF93caIU1y7_HuktTCaCYnstRV7f3/view?usp=drive_link)
- DPT [Eraslan, G., Simon, L. M., Mircea, M., Mueller, N. S., & Theis, F. J. (2019). Single-cell RNA-seq denoising using a deep count autoencoder. Nature communications, 10(1), 390. https://doi.org/10.1038/s41467-018-07931-2](https://drive.google.com/file/d/17Wopxz0EEZAc6Tz4wQCL252E8dtBHERV/view?usp=drive_link)
- palantir [Setty, M., Kiseliovas, V., Levine, J., Gayoso, A., Mazutis, L., & Pe'er, D. (2019). Characterization of cell fate probabilities in single-cell data with Palantir. Nature biotechnology, 37(4), 451–460. https://doi.org/10.1038/s41587-019-0068-4](https://drive.google.com/file/d/1ipfm-YRt7OzPWHMtN5GarmB6SmfyNzb4/view?usp=drive_link)
- [文献解读｜CellRank2：单细胞命运图谱绘制的统一框架](https://mp.weixin.qq.com/s/1tqeR5j48GsYMcr20HLAJA)
- [单细胞轨迹分析九大王牌方法全解析](https://mp.weixin.qq.com/s/Jco8JWPHeZMCCTerR1MQgA)
- [单细胞拟时序分析方法汇总](https://mp.weixin.qq.com/s/ke0EUjRraAH6vGIPpVbYWg)
- [scRDEN：利用『基因对』秩差异，而不是『单个基因』差异的『稳健』细胞轨迹推断~](https://mp.weixin.qq.com/s/2r0uHDnfYn7eTRE_DK6PNQ)
- [Nat. Biotechnol. | 用于推断单细胞基因轨迹的GeneTrajectory方法](https://mp.weixin.qq.com/s/0YqUa2qEujG6r1L16OB4_g)
- [scMaSigPro—沿单细胞轨迹的差异表达分析](https://mp.weixin.qq.com/s/1P4UJPvpeToanG5bnqUyYg)

---
# Coder

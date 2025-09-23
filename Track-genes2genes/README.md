# Aligning single-cell trajectories of gene expression with [Genes2Genes](https://github.com/Teichlab/Genes2Genes.git)
- **Brief** 时序比较揭示时序差异基因
- **Log**
  - v1.0.0
    - 0923 判断pseudotime范围并适时做normalize
    - 250901 第一次提交Description
- **Related** Track-pseudotime

---
# Input
- **Variable**
  - **h5ad_ref** Array [File] 作为时序比较Reference的h5ad文件
  - **h5ad_query** Array [File] 作为时序比较Query的h5ad文件
  - **prefix** Array [String] 输出文件夹的名字，与上面的顺序一一对应
  - **pseudotime_key** String 储存拟时序信息的键
  - **annotation_colname** String 储存亚群信息的键
  - **mem_g2g** Int 运行g2g需要的内存资源GB

**Note:** Reference和Query所做的拟时序分析所用方法应该一致，例如用**Track-pseudotime**跑palantir

- **Example** [download](https://github.com/ydgenomics/Tracks/blob/main/Track-genes2genes/WDL/v1.0.0/Track-g2g_v1.0.0.csv)

|EntityID|h5ad_ref|h5ad_query|prefix|pseudotime_key|annotation_colname|mem_g2g|
|---|---|---|---|---|---|---|
|test|/Files/yangdong/wdl/Track-pseudotime/W202508270146180/pseudotime/cotton_K2.hr.rds.rh_palantir.h5ad|/Files/yangdong/wdl/Track-pseudotime/W202508270146318/pseudotime/cotton_D3.hr.rds.rh_palantir.h5ad|K2_vs_D3|palantir_pseudotime|RNA_snn_res.0.5|32|

---
# Output
- **Frame**
```shell
tree /data/input/Files/yangdong/wdl/Track-g2g/W202508270150778
/data/input/Files/yangdong/wdl/Track-g2g/W202508270150778
├── input.json
└── K2_vs_D3
    ├── aggregate_alignment_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    ├── aligner_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pkl
    ├── cluster
    │   ├── aggregate_alignment_0_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    │   ├── aggregate_alignment_1_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    │   ├── aggregate_alignment_2_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    │   └── aggregate_alignment_3_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    ├── clustering_distmap_0.57_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.png
    ├── clustering_genes_0.57_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    ├── clustering_genes_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    ├── g2g_cotton_K2.hr.rds.rh_palantir.h5ad_vs_cotton_D3.hr.rds.rh_palantir.h5ad.ipynb
    ├── gene_cluster_alignment.csv
    ├── log.txt
    ├── pseudotime_cotton_D3.hr.rds.rh_palantir_2.pdf
    ├── pseudotime_cotton_D3.hr.rds.rh_palantir.pdf
    ├── pseudotime_cotton_K2.hr.rds.rh_palantir_2.pdf
    ├── pseudotime_cotton_K2.hr.rds.rh_palantir.pdf
    ├── pseudotime_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    ├── pseudotime_point_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    ├── ranking_genes__cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.csv
    ├── ranking_genes_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    ├── ranking_genes_log2_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
    └── topDEgenes
        ├── gene_alignment_Ga01g00535_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── gene_alignment_Ga01g02528_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── gene_alignment_Ga05g02337_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── gene_alignment_Ga06g01195_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── gene_alignment_Ga07g01230_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── gene_alignment_Ga07g01598_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── gene_alignment_Ga09g00268_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── gene_alignment_Ga11g01779_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── gene_alignment_Ga12g01305_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── gene_alignment_Ga13g00463_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga01g00535_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga01g02528_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga05g02337_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga06g01195_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga07g01230_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga07g01598_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga09g00268_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga11g01779_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga12g01305_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plot_cost_Ga13g00463_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga01g00535_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga01g02528_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga05g02337_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga06g01195_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga07g01230_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga07g01598_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga09g00268_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga11g01779_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga12g01305_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        ├── plotTimeSeries_Ga13g00463_cotton_K2.hr.rds.rh_palantir_vs_cotton_D3.hr.rds.rh_palantir.pdf
        └── topDEgenes.txt

4 directories, 53 files
```
- **Interpretation**
  - .ipynb 主要看这个文件，用vscode看可以很好的整理结果
  - .pkl 是将比对结果变量`aligner`保存为文件，可以通过`with open('aligner.pkl', 'rb') as f: aligner = pickle.load(f)`重新读取该对象
  - topDEgenes目录是将相似性最低的十个基因做可视化
  - cluster目录是将基因分群后的模式进行展示
- **Next**
  - Enrich 对找到的时序差异基因做基因富集

---
# Detail
- **Pipeline** 对.X标准化后且具有pseudotime_key的共有hvg进行时序比较。Genes2Genes感觉跟Gene2Role有相似的思路，比的是共有基因，gene-level的比较。在Gene2Role，作者将目标基因的相关拓扑结构转换为行向量，通过行向量计算做定量和定性分析。在Genes2Genes中，作者将目标基因的表达按时序进行排列，分段进行比较(趋势和表达量)，大致分match & mismatch两大类，然后再通过five states machine去拿到不同的type。基于不同的type序列做相似性计算，将相似性高的具有同一表达模式的基因归为同一个群。传统的差异基因分析方法常常关注基因平均表达，而通过将拟时序和差异分析结合，可以揭示特异的时序差异基因。
*学习genes2genes的tutorial* [Tutorial.ipynb](https://github.com/Teichlab/Genes2Genes/blob/main/notebooks/Tutorial.ipynb)
  - 两个h5ad文件(一个reference，一个query)
  - .X是log1p之后的，非原始数据(提供检查，如若不是则报错！)
  - .obs['time']存储是pseudotime的结果，预计从cytotrace中获得，要求是[0,1]范围内，如果不是可以通过作者的处理(标准化)来实现
  - 可视化不同pseudotime下细胞的密度density/分布distribution
  - 选择可靠的pseudotime点来做两者的比对(分箱bin操作) `optbinning`这个包
  - 作者考虑到reference和query也是有`batch`的，这种batch应该是真时序，可以查看在不同的bin下面batch的分布，真时序的状态下肯定越早的分bin存在的真时序的数据越多；如果没有真时序，我们也可以尝试用细胞类型去解释，越早的分bin应该有更多具有分化潜力的细胞类型
  - 选择需要比的基因，比的这些基因必须都存在于两个数据集中，默认对两个数据集的`highly variable`取交集后作为`gene_list`
  - 使用`Main.RefQueryAligner()`做基因集合`gene_list`比对，其本质是比的是两个数据集的基因，所以其`gene_list`应该是两者都有的。另外我们应该关注的是重要的基因(高变基因，marker基因，转录因子等)(Example gene sets to align: all transcription factors, all highly variable genes, lineage-specific genes of interest, a specific pathway gene set etc.)，无论从计算效率还是从可解释性来讲，对小部分基因集来做比都是及其有意义的。
  - 也可以选择关注单个基因来做比对，使用`aligner.results_map()`，e.g. aligner.results_map['TNF']。`gene_obj.landscape_obj.plot_alignment_landscape()`显示其“Alignment cost landscape”,X,Y轴分别对应Reference和Query，匹配的越多颜色越深。
  - Aggregate (average) cell-level alignment across all aligned genes (The heatmap value gives the number of genes where the corresponding timepoints have been matched)
  - 对基因进行排序(rank)基于比对的相似性`get_stat_df()`
  - 根据相似性结果筛选出差异基因`threshold_similarity = 0.3 `
  - ...

```python
aligner = Main.RefQueryAligner(adata_ref, adata_query, gene_list, n_bins) #配置aligner
aligner.align_all_pairs() #启动aligner
aligner.get_aggregate_alignment #看整体趋势
df = aligner.get_stat_df #转化为df包括具体的similarity/cost/l2fc
df = ClusterUtils.run_clustering(aligner, metric='levenshtein', experiment_mode=True) #对aligner所有基因聚类测试，测试不同标准下分群数
ClusterUtils.run_clustering(aligner, metric='levenshtein', DIST_THRESHOLD=0.37) #根据上面测试选出来合适的分群策略
aligner.get_aggregate_alignment_for_subset(GENE_SUBSET) #根据Arrary属性的GENE_SUBSET来看关注基因群的整体趋势
```
pseudotime可以通过monocle3获得，然后用默认代码将其调整为范围[0,1]，并存储于`time`

- **Software**
  - [Genes2Genes](https://github.com/Teichlab/Genes2Genes)
- **Script**
  - [preprocess.py](https://github.com/ydgenomics/Tracks/blob/main/Track-genes2genes/WDL/v1.0.0/preprocess.py)
  - [g2g.ipynb](https://github.com/ydgenomics/Tracks/blob/main/Track-genes2genes/WDL/v1.0.0/g2g.ipynb)
- **Image**
  - g2g_env--01, g2g_env

```shell
source /opt/software/miniconda3/bin/activate
conda create --name g2g python=3.8 -y
conda activate g2g
# pip install genes2genes
# pip install git+https://github.com/Teichlab/Genes2Genes.git
pip install git+https://github.com/Teichlab/Genes2Genes.git -i https://mirrors.aliyun.com/pypi/simple/ 
pip install optbinning # https://gnpalencia.org/optbinning/installation.html
conda install conda-forge::ipykernel -y
conda install conda-forge::scanpy -y
# python -m ipykernel install --user --name g2g --display-name "Python (g2g)"
```

---
# Reference & Citation
- [Sumanaweera, D., Suo, C., Cujba, A. M., Muraro, D., Dann, E., Polanski, K., Steemers, A. S., Lee, W., Oliver, A. J., Park, J. E., Meyer, K. B., Dumitrascu, B., & Teichmann, S. A. (2025). Gene-level alignment of single-cell trajectories. Nature methods, 22(1), 68–81. https://doi.org/10.1038/s41592-024-02378-4](https://www.nature.com/articles/s41592-024-02378-4) [Google driver](https://drive.google.com/file/d/1e9bYDfZ0JzHhk8QcovzP7RW8DnHMck7G/view?usp=drive_link)
- [Nature Methods|| 2024 || Genes2Genes : 单细胞轨迹的基因水平比对](https://mp.weixin.qq.com/s/kcw_aqgHDg5Vd0G8GzM9aA)
- [scMaSigPro—沿单细胞轨迹的差异表达分析](https://mp.weixin.qq.com/s/1P4UJPvpeToanG5bnqUyYg)

---
# Coder
- **Editor:** yangdong (yangdong@genomics.cn)
- **GitHub:** [ydgenomics](https://github.com/ydgenomics)
- **Prospect:** Focused on innovative, competitive, open-source projects and collaboration
- **Repository:** [Tracks/Track-genes2genes](https://github.com/ydgenomics/Tracks/tree/main/Track-genes2genes)

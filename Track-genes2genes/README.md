# Detail
**Workflow**
  - preprocess 对h5ad文件做标准化并补充Hvg，仍然使用X_pca作为降维的键
  - pseudotime 拟时序分析，CytoTRACE, dpt, palantir (提供找起点的notebook)
  - g2g 对.X标准化后且具有pseudotime_key的共有hvg进行时序比较

**Related:** **Track-cytotrace, Track-dpt, Track-palantir, Track-g2g**
读懂Genes2Genes的原理
Genes2Genes感觉跟Gene2Role有相似的思路，比的是共有基因，gene-level的比较。在Gene2Role，作者将目标基因的相关拓扑结构转换为行向量，通过行向量计算做定量和定性分析。在Genes2Genes中，作者将目标基因的表达按时序进行排列，分段进行比较(趋势和表达量)，大致分match & mismatch两大类，然后再通过five states machine去拿到不同的type。

传统的差异基因分析方法常常关注基因平均表达，而通过将拟时序和差异分析结合，可以揭示特异的时序差异基因。
It will automatically detect the number of cores in the system: `aligner.align_all_pairs()`. 

```python
aligner = Main.RefQueryAligner(adata_ref, adata_query, gene_list, n_bins) #配置aligner
aligner.align_all_pairs() #启动aligner
aligner.get_aggregate_alignment #看整体趋势
df = aligner.get_stat_df #转化为df包括具体的similarity/cost/l2fc
df = ClusterUtils.run_clustering(aligner, metric='levenshtein', experiment_mode=True) #对aligner所有基因聚类测试，测试不同标准下分群数
ClusterUtils.run_clustering(aligner, metric='levenshtein', DIST_THRESHOLD=0.37) #根据上面测试选出来合适的分群策略
aligner.get_aggregate_alignment_for_subset(GENE_SUBSET) #根据Arrary属性的GENE_SUBSET来看关注基因群的整体趋势

```
学习genes2genes的tutorial[Tutorial.ipynb](https://github.com/Teichlab/Genes2Genes/blob/main/notebooks/Tutorial.ipynb)
- 两个h5ad文件(一个reference，一个query)
  - .X是log1p之后的，非原始数据(提供检查，如若不是则报错！)
  - .obs['time']存储是pseudotime的结果，预计从cytotrace中获得，要求是[0,1]范围内，如果不是可以通过作者的处理(标准化)来实现

- 可视化不同pseudotime下细胞的密度density/分布distribution
- 选择可靠的pseudotime点来做两者的比对(分箱bin操作) `optbinning`这个包
- 作者考虑到reference和query也是有`batch`的，这种batch应该是真时序，可以查看在不同的bin下面batch的分布，真时序的状态下肯定越早的分bin存在的真时序的数据越多；如果没有真时序，我们也可以尝试用细胞类型去解释，越早的分bin应该有更多具有分化潜力的细胞类型
- 使用`Main.RefQueryAligner()`做基因集合`gene_list`比对，其本质是比的是两个数据集的基因，所以其`gene_list`应该是两者都有的。另外我们应该关注的是重要的基因(高变基因，marker基因，转录因子等)(Example gene sets to align: all transcription factors, all highly variable genes, lineage-specific genes of interest, a specific pathway gene set etc.)，无论从计算效率还是从可解释性来讲，对小部分基因集来做比都是及其有意义的。
- 也可以选择关注单个基因来做比对，使用`aligner.results_map()`，e.g. aligner.results_map['TNF']。`gene_obj.landscape_obj.plot_alignment_landscape()`显示其“Alignment cost landscape”,X,Y轴分别对应Reference和Query，匹配的越多颜色越深。
- Aggregate (average) cell-level alignment across all aligned genes (The heatmap value gives the number of genes where the corresponding timepoints have been matched)
- 对基因进行排序(rank)基于比对的相似性`get_stat_df()`
- 根据相似性结果筛选出差异基因`threshold_similarity = 0.3 `


pseudotime可以通过monocle3获得，然后用默认代码将其调整为范围[0,1]，并存储于`time`  --似乎不太行，好像要指定root细胞

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
conda install conda-forge::papermill -y
python -m ipykernel install --user --name cellrank2 --display-name "Python (cellrank2)"

# conda create --name g2g python=3.8 -y
# conda activate g2g
# pip install git+https://github.com/Teichlab/Genes2Genes.git -i https://mirrors.aliyun.com/pypi/simple/ 
# pip install optbinning # https://gnpalencia.org/optbinning/installation.html
# conda install conda-forge::ipykernel -y
# python -m ipykernel install --user --name g2g --display-name "Python (g2g)"
```
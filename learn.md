cellrank2整合的功能强大，完全可以用cellrank2跑其它方法，应该要认真去学一下cellrank2和genes2genes

| 软件/包名               | 语言/接口       | 特点（无需指定起始细胞）                                         | 备注                           |
| ------------------- | ----------- | ---------------------------------------------------- | ---------------------------- |
| **SCORPIUS**        | R 包         | 基于主曲线（principal curve）自动推断线性轨迹，**无 root 参数**         | 轻量、速度快，适合简单线性发育              |
| **Slingshot**       | R 包         | 先聚类再构建最小生成树（MST），自动识别分支和终点，**不强制手动 root**            | 支持多分支，可后加已知端点校正              |
| **TSCAN**           | R 包 / Shiny | 先聚类后 MST，自动排序；Web 版可无参数运行                            | 图形界面友好，适合新手                  |
| **Monocle 2**       | R 包         | Reverse graph embedding 自动推断轨迹，**可选 root**（不强制）      | 引用率最高，默认流程无需提供 root          |
| **Monocle 3**       | R 包         | 图嵌入 + 最小生成树，自动选择端点，**不必指定 root**                     | 支持大样本、复杂拓扑                   |
| **dynverse 生态**     | R 包集合       | 封装 45+ TI 方法，多数算法内部自动推断 root（如 PAGA、Slingshot、MST 等） | 一键跑多种算法，统一评估                 |
| **scVelo / TFvelo** | Python      | RNA velocity 基于剪接动力学 **自动给出方向**，无需人工 root            | 需额外 pre-mRNA/spliced loom 文件 |



[单细胞实战之CytoTRACE2和monocle3——入门到进阶(高级篇2）](https://mp.weixin.qq.com/s/KGSoRx3klmliKPVL7ml28Q)
> monocle3需要指定起点细胞，而CytoTRACE2可以评估细胞的分化潜力，联用就可以实现将CytoTRACE2中拿到的最高分化潜力的细胞作为monocle3的起点细胞，基于这个思路的话，很多需要指定起点细胞的问题都可以得到解决

[单细胞轨迹分析九大王牌方法全解析](https://mp.weixin.qq.com/s/Jco8JWPHeZMCCTerR1MQgA)

[2024(Nature Method)_Gene-level alignment of single-cell trajectories](https://www.nature.com/articles/s41592-024-02378-4)
[Nature Methods || 1月封面 || Genes2Genes : 单细胞生长轨迹的基因匹配 || 代码更新](https://mp.weixin.qq.com/s/px92Esagli91WX6qVWtF6Q)


[单细胞拟时序分析方法汇总](https://mp.weixin.qq.com/s/ke0EUjRraAH6vGIPpVbYWg)
单细胞拟时序分析（Trajectory Inference, TI）作为解析细胞动态演化轨迹的核心计算框架，通过重构细胞转录组相似性网络，将离散的细胞状态投影至连续伪时间轴，为模拟细胞分化、周期调控及激活等动态过程提供了量化工具。

从方法论演进视角审视，轨迹推断工具经历了从线性模型到非线性网络重构的范式转变。早期工具（如Monocle 1/2）基于主成分分析或独立成分分析构建线性发育轨迹，适用于简单分化路径的解析；后续方法（如Slingshot、Wishbone）引入分支事件检测算法，初步实现对双线性分化轨迹的建模；而PAGA（Partition-based Graph Abstraction）通过图抽象策略构建细胞状态连接网络，RNA Velocity则整合未剪接/剪接mRNA丰度信息预测细胞瞬时动力学方向，二者共同突破了传统线性模型的局限，揭示了分化过程中普遍存在的网状转化及多稳态平衡现象。近期研究进一步将多组学数据整合纳入轨迹推断框架，例如通过耦合scRNA-seq与scATAC-seq数据构建表观-转录协同演化模型，或利用CITE-seq蛋白组信息校正转录组伪时间推断偏差，显著提升细胞状态识别的生物学解释。

[将细胞分化关系“一网打尽”的拟时分析软件：PAGA](https://mp.weixin.qq.com/s/s9GxMTpvWvFw2NJJs_21Zw)
[PAGA: Trajectory inference](https://scanpy.readthedocs.io/en/stable/tutorials/trajectories/paga-paul15.html)
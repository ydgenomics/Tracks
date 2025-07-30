[单细胞拟时序分析方法汇总](https://mp.weixin.qq.com/s/ke0EUjRraAH6vGIPpVbYWg)
单细胞拟时序分析（Trajectory Inference, TI）作为解析细胞动态演化轨迹的核心计算框架，通过重构细胞转录组相似性网络，将离散的细胞状态投影至连续伪时间轴，为模拟细胞分化、周期调控及激活等动态过程提供了量化工具。

从方法论演进视角审视，轨迹推断工具经历了从线性模型到非线性网络重构的范式转变。早期工具（如Monocle 1/2）基于主成分分析或独立成分分析构建线性发育轨迹，适用于简单分化路径的解析；后续方法（如Slingshot、Wishbone）引入分支事件检测算法，初步实现对双线性分化轨迹的建模；而PAGA（Partition-based Graph Abstraction）通过图抽象策略构建细胞状态连接网络，RNA Velocity则整合未剪接/剪接mRNA丰度信息预测细胞瞬时动力学方向，二者共同突破了传统线性模型的局限，揭示了分化过程中普遍存在的网状转化及多稳态平衡现象。近期研究进一步将多组学数据整合纳入轨迹推断框架，例如通过耦合scRNA-seq与scATAC-seq数据构建表观-转录协同演化模型，或利用CITE-seq蛋白组信息校正转录组伪时间推断偏差，显著提升细胞状态识别的生物学解释。

[将细胞分化关系“一网打尽”的拟时分析软件：PAGA](https://mp.weixin.qq.com/s/s9GxMTpvWvFw2NJJs_21Zw)
[PAGA: Trajectory inference](https://scanpy.readthedocs.io/en/stable/tutorials/trajectories/paga-paul15.html)
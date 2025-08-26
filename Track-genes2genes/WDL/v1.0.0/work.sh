#!/usr/bin/env bash
/opt/software/miniconda3/envs/cellrank2/bin/python -m ipykernel install --user --name cellrank2 --display-name "Python (cellrank2)"
jupyter kernelspec list

h5ad_subset="/data/work/test1/test2/cotton_K2.hr.rds.rh.h5ad"
cluster_key='RNA_snn_res.0.5'
h5ad_all="/data/users/yangdong/yangdong_faff775391984da0a355d4bd70217714/online/cotton/output/dataget/K2/cotton_K2.h5ad"
cluster_key_all="leiden_res_0.50"

# 1) 拆为数组
tool4pseudotime='cytotrace,dpt,palantir'
IFS=',' read -ra TOOLS <<< "$tool4pseudotime"   # 得到数组 TOOLS=(cytotrace dpt palantir)

# 2) 逐个判断
for tool in "${TOOLS[@]}"; do
    case "$tool" in
        cytotrace)
            echo "Run cytotrace ..."
            papermill /Tracks/Track-genes2genes/WDL/v1.0.0/cytotrace.ipynb cytotrace_executed.ipynb \
            --kernel cellrank2 -p h5ad_subset $h5ad_subset -p cluster_key $cluster_key \
            -p h5ad_all $h5ad_all -p cluster_key_all $cluster_key_all
            ;;
        dpt)
            echo "Run dpt ..."
            n_pc=~{n_pc}
            root_cluster='~{root_cluster}'
            use_argmin='~{use_argmin}' # 'yes' or 'no'
            papermill /Tracks/Track-genes2genes/WDL/v1.0.0/dpt.ipynb dpt_executed.ipynb \
            --kernel cellrank2 -p h5ad_subset $h5ad_subset -p cluster_key $cluster_key -p h5ad_all $h5ad_all -p cluster_key_all $cluster_key_all \
            -p n_pc $n_pc -p root_cluster $root_cluster -p use_argmin $use_argmin
            ;;
        palantir)
            echo "Run palantir ..."
            root_idx=~{root_idx}
            papermill /Tracks/Track-genes2genes/WDL/v1.0.0/palantir.ipynb palantir_executed.ipynb \
            --kernel cellrank2 -p h5ad_subset $h5ad_subset -p cluster_key $cluster_key \
            -p h5ad_all $h5ad_all -p cluster_key_all $cluster_key_all -p root_idx $root_idx
            ;;
        *)
            echo "Unknown tool: $tool"
            ;;
    esac
done
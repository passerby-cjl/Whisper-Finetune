#!/usr/bin/env bash

export LD_LIBRARY_PATH="/usr/lib64-nvidia" &&
export LIBRARY_PATH="/usr/local/cuda/lib64/stubs" &&
ldconfig /usr/lib64-nvidia &&
python -m pip install -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple &&
pip install triton==2.1.0 &&
CUDA_VISIBLE_DEVICES=0,1 torchrun --nproc_per_node=2 finetune.py --base_model=./distil-small-model/model --local_files_only=True --per_device_train_batch_size=4 --per_device_eval_batch_size=4 --eval_steps=3000 --save_steps=3000 

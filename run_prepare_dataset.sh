#!/usr/bin/env bash

pip install --upgrade Cython==0.29.35 &&
pip install pysptk --no-build-isolation &&
pip install modelscope[audio] -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html &&

python aishell.py --add_pun=True --target_dir=./dataaishell &&
python prepare_dataset.py
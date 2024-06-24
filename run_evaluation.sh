#!/usr/bin/env bash

python evaluation.py --model_path=./distil-small-model/model --test_data=./dataset/fleurs_test.json --local_files_only=False --batch_size=64 --metric=cer --remove_pun=True --num_workers=4

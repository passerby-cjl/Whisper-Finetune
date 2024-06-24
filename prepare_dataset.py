from datasets import load_dataset
import json

dataset = load_dataset("mozilla-foundation/common_voice_16_1", "zh-CN", token="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", split="train")
dataset.to_json("./dataset/common_voice_train.json") # 保存到该目录下

dataset = load_dataset("mozilla-foundation/common_voice_16_1", "zh-CN", token="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", split="test")
dataset.to_json("./dataset/common_voice_test.json") # 保存到该目录下


dataset = load_dataset("google/fleurs", "cmn_hans_cn", token="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", split="train")
# 遍历数据集中的每个样本
with open('./dataset/fleurs_train.json', 'w') as json_file:
    for sample in dataset:
        del sample['audio']['array']
        del sample['language']
        path_list = sample['path'].split('/')
        path_list.insert(-1,"train")
        sample['audio']['path'] = "/".join(path_list)
        sample['sentence'] = sample['raw_transcription']
        json_file.writelines(json.dumps(sample).replace('/','\\/')+'\n')

dataset = load_dataset("google/fleurs", "cmn_hans_cn", token="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", split="test")
# 遍历数据集中的每个样本
with open('./dataset/fleurs_test.json', 'w') as json_file:
    for sample in dataset:
        del sample['audio']['array']
        del sample['language']
        path_list = sample['path'].split('/')
        path_list.insert(-1,"test")
        sample['audio']['path'] = "/".join(path_list)
        sample['sentence'] = sample['raw_transcription']
        json_file.writelines(json.dumps(sample).replace('/','\\/')+'\n')

file1 = "./dataset/train0.json"
file2 = "./dataset/train1.json"
file5 = "./dataset/test0.json"
dataset_dir = "./dataaishell"
with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file5, 'r') as f5:
    data1 = f1.read()
    data2 = f2.read()
    data5 = f5.read()
    data1 = data1.replace("/mnt/d/dataset/audio", dataset_dir)
    data2 = data2.replace("/mnt/d/dataset/audio", dataset_dir)
    data5 = data5.replace("/mnt/d/dataset/audio", dataset_dir)
with open("./dataset/aishell_train.json", 'w') as f:
    f.write(data1+data2)
with open("./dataset/aishell_test.json", 'w') as f:
    f.write(data5)

import os
file1 = "./dataset/aishell_train.json"
file2 = "./dataset/common_voice_train.json"
file3 = "./dataset/fleurs_train.json"
file4 = "./dataset/aishell_test.json"
file5 = "./dataset/common_voice_test.json"
file6 = "./dataset/fleurs_test.json"
output_train_file = "./dataset/train.json"
output_test_file = "./dataset/test.json"
with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'r') as f3, open(file4, 'r') as f4, open(file5, 'r') as f5, open(file6, 'r') as f6:
    data1 = f1.read()
    data2 = f2.read()
    data3 = f3.read()
    data4 = f4.read()
    data5 = f5.read()
    data6 = f6.read()
if os.path.isfile(output_train_file):
    os.remove(output_train_file)
if os.path.isfile(output_test_file):
    os.remove(output_test_file)
with open(output_train_file, 'w') as f:
    f.write(data1 + data2 + data3)
with open(output_test_file, 'w') as f:
    f.write(data4 + data5 + data6)
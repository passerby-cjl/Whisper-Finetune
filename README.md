# 模型微调与验证
## 准备数据集
将run_prepare_dataset.sh文件中target_dir参数改为本地aishell数据集的文件夹目录
运行run_prepare_dataset.sh
## 微调模型
将run_finetune.sh文件中base_model参数改为本地模型文件夹目录
运行run_finetune.sh
## 合并模型
运行run_merge.sh文件
## 验证模型
将run_evaluation.sh文件中test_data参数改为相应的数据集json文件位置
运行run_evaluation.sh文件
## 模型推理
将run_inference.sh文件中的audio_path参数改为需要识别的音频文件
运行run_inference.sh文件
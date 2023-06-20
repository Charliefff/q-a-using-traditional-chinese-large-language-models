import os
 
# Path: alpaca-lora/Bash.py

os.sys("WORLD_SIZE=4 CUDA_VISIBLE_DEVICES=0,1,2,3 torchrun --nproc_per_node=4 --master_port=1234 lora_finetune.py")
os.sys("python lora_generate2.py")

#!/bin/bash
torchrun --standalone --nproc_per_node 4 scripts/train.py configs/opensora-v1-2/train/stage1.py --data-path /home/chloehjh/Open-Sora/NS_video_new.csv --wandb True


#!/usr/bin/env bash

SRC_FOLDER=$1
OUT_FOLDER=$2

proj_dir=""
tools_dir="${proj_dir}/tools"
local_dir="${proj_dir}/local"

echo "Extracting optical flow from videos in folder: ${SRC_FOLDER}"
python3 vid2img_ucf101.py ${SRC_FOLDER} ${OUT_FOLDER}
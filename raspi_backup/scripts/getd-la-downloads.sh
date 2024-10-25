#!/bin/bash

# 定义变量
REMOTE_SERVER="la"
REMOTE_DIR="$HOME/downloads/"
LOCAL_DIR="$HOME/downloads/"

# 确保本地目录存在
mkdir -p "$LOCAL_DIR"

# 使用 scp 将远程服务器上的文件下载到本地
scp -r "${REMOTE_SERVER}:${REMOTE_DIR}*" "$LOCAL_DIR"

# 检查 scp 命令是否成功执行
if [ $? -eq 0 ]; then
  echo "文件已成功下载到本地目录: $LOCAL_DIR"

  # 使用 ssh 在远程服务器上删除 /root/audio/ 目录中的所有文件
  ssh "$REMOTE_SERVER" "cd ${REMOTE_DIR} && rm -rf ./*"

  if [ $? -eq 0 ]; then
    echo "远程服务器的文件已成功删除。"
  else
    echo "远程服务器的文件删除失败。"
  fi
else
  echo "文件下载失败，请检查网络连接和服务器配置。"
fi


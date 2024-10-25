#!/bin/bash

# 检查是否提供了播放列表 URL
if [ -z "$1" ]; then
  echo "用法: $0 <播放列表URL>"
  exit 1
fi

# 播放列表 URL 来自命令行参数
links="$1"

# 保存目录
output_dir="$HOME/audio/"

# 创建保存目录
# mkdir -p "$output_dir"

# 使用 yt-dlp 下载播放列表中的音频
# yt-dlp -x --audio-format mp3 -o "$output_dir/%(title)s.%(ext)s" "$playlist_url"

yt-dlp -f 'bestaudio/best' -P "$output_dir" "$links"

echo "下载完成，所有音频已保存到 $output_dir 目录中。"


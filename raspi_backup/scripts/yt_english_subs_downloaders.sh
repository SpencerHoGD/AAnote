#!/bin/bash

# Name: yt_subtitle_extractor.sh

# Check if the required tools are installed
command -v yt-dlp >/dev/null 2>&1 || { echo >&2 "yt-dlp is required but not installed. Aborting."; exit 1; }

# Create the subtitles directory if it doesn't exist
SUBTITLE_DIR="$HOME/subtitles"
mkdir -p "$SUBTITLE_DIR"

# Prompt for the YouTube video URL
read -p "Enter the YouTube video URL: " VIDEO_URL

# Download English auto-generated subtitles and convert to plain text
yt-dlp --skip-download --write-auto-sub --sub-lang en \
       --output "$SUBTITLE_DIR/%(title)s.%(ext)s" \
       "$VIDEO_URL" 

echo "Subtitles have been downloaded and saved to $SUBTITLE_DIR"


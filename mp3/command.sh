#!/usr/bin/env bash

# Concatenate all mp3s into one file.
ffmpeg -f concat -i list.txt -c copy all_pages.mp3

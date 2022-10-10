#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H_%M_%S")

ffmpeg -framerate 60 -pattern_type glob -i "./*.jpg" -s:v 4056x3040 -c:v libx264 -crf 17 -pix_fmt yuv420p $DATE.mp4

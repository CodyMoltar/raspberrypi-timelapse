#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H_%M_%S")

ffmpeg -framerate 60 \
-pattern_type glob \
-i "./*.jpg" \
-s:v 4056x3040 \
-c:v prores_ks \
-profile:v 0 \
-vendor apl0 \
-bits_per_mb 8000 \
-pix_fmt yuv422p10le \
$DATE.mov

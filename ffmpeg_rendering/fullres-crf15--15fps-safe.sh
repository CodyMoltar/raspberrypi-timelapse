#!/bin/bash

CURRENT=`pwd`
BASENAME=`basename "$CURRENT"`


ffmpeg -framerate 15 -pattern_type glob -i "./*.jpg" -s:v 4056x3040 -c:v libx264 -crf 15 /mnt/safe/safe/Timelapses/raw/$BASENAME.mp4


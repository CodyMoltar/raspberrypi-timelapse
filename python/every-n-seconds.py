import subprocess

from time import sleep

while 1:
    subprocess.call(['sh', 'timelapse.sh'])
    
from io import BytesIO
from picamera import PiCamera
from datetime import datetime
from time import sleep
import paramiko
from scp import SCPClient
import os
from fractions import Fraction

password = 'Dingen1dingen2'
server = '192.168.0.105'
port = 22
user = 'pi'
target_location = '/mnt/storage/dump/timelapses/dingen'

###### CONNECT TO SSH #######

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())

###### SETUP CAMERA #######

camera = PiCamera()
camera.sensor_mode = 3
camera.resolution = camera.MAX_RESOLUTION
camera.iso = 100
sleep(2)
camera.exposure_mode = 'off'
camera.awb_mode = 'off'
camera.awb_gains = (Fraction(347, 128), Fraction(129, 64))
camera.shutter_speed = 4500
camera.vflip = False
camera.hflip = False

def take_picture(delay):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
    
    filename = 'photos/' + dt_string + '.jpg'
    print(filename)
    print(camera.awb_gains)

    camera.capture(filename)
#     scp.put(filename, recursive=True, remote_path=target_location)
#     os.remove(filename)
    sleep(delay)

try:
        
    while 1:
        
        take_picture(4)
        
        
except KeyboardInterrupt:
    camera.stop_preview()
    camera.close()
    print("exiting")
    



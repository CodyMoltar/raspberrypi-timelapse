from io import BytesIO
import paramiko
from scp import SCPClient
import os

password = 'your_password'
server = 'your_server_address'
port = 22
user = 'your_username'
target_location = '/path/to/folder'

###### CONNECT TO SSH #######
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())

# get all the files of the current directory
for img in os.listdir('./'):
    # check if the file has a .jpg extension
    if img.endswith("jpg"):
        print(img)
        # copy the file with ssh to the destination folder
        scp.put(img, recursive=True, remote_path=target_location)
        # remove the local file
        os.remove(img)


    



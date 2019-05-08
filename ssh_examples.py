# http://www.paramiko.org/
import paramiko

hostname = "ftp.myschool.org"
username = "techtalk"
password = "S3cur17y"

# Initiate SFTP client
transport = paramiko.Transport(hostname)
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)


def download(remote_file, local_file):
    sftp.get(remote_file, local_file)


def upload(remote_file, local_file):
    sftp.put(local_file, remote_file)


def list_server_dir(remote_directory):
    contents = sftp.listdir(remote_directory)
    print(f'Current contents of remote directory "{remote_directory}":')
    for item in contents:
        print(item)


# Close connection
sftp.close()
transport.close()

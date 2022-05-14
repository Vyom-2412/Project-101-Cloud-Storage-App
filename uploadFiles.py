import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BHixWLH4b0WHcu9YnEiQeYGpPBgOYgqITOx5QkcrQPv6cY9Zuxt1qFa34EXf1d3oFuIAAEB2WmtGF2yjWLj4aoSBUEI6g2A-6ZlhCX1KmATJrb4XTP0dB2G_PZZ3CRXtwmKIVFxg3Yo'
    transferData = TransferData(access_token)

    file_from = 'E:/Python/Data Sets/'
    file_to = '/'

    transferData.upload_file(file_from,file_to)
    print("file has been moved!")

main()

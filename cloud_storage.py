import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BHAm-NEwMeTCAEWhHvfovXplu16B_k5OmRAIkxEI_8lVNIuOf9tv1px0nzU7hek6hp9j5ESEX6aK4rC9BUApJMLNRNGeRFU7p3lHfCKmZx6ah526RGY-F_4iTHm3sqDe8bSFImbUDho'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")
    
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()

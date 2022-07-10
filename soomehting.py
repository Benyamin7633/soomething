import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files: 
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)



def main():
    access_token = 'sl.BKsiCLCZJKC6a9ooonn8bl7PARBcdcvkjUEzl5_VVC1GpZlymfyudF4-EmfpfEWJq049G4--Ry6TFWXsj-Rx8WMFjMydl-A987ZsO21CgbIh_facsMT_t1Msmk87BzSArputYeoTRLo'
    transferData = TransferData(access_token)
    file_from = input("enetr the file path to transfer:")
    file_to = input("enter the full path to upload the dropbox:")
    transferData.upload_file(file_from, file_to)
    print("file path has been moved")


main()
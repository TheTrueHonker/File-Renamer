import os
import os.path
import time
import eyed3
import datetime


class Prefixer:
    def __init__(self, folder_path):
        self.folder = folder_path
        self.files = os.scandir(folder_path)

    def _prefix(self, file, information):
        print(f'Renaming file: {file}')
        old_file_name = self.folder + file
        new_file_name = self.folder + information + "_" + file
        os.rename(old_file_name, new_file_name)

    def prefix_string(self, string):
        for file in self.files:
            if file.is_file():
                self._prefix(file.name, string)

    def prefix_cdate(self):
        for file in self.files:
            if file.is_file():
                created_date = datetime.datetime.utcfromtimestamp(os.path.getctime(self.folder + file.name))
                created_date_str = created_date.strftime('%Y%m%d')
                self._prefix(file.name, created_date_str)

    def prefix_mdate(self):
        for file in self.files:
            if file.is_file():
                modified_date = datetime.datetime.utcfromtimestamp(os.path.getctime(self.folder + file.name))
                modified_date_str = modified_date.strftime('%Y%m%d')
                self._prefix(file.name, modified_date_str)

    def prefix_track_num(self):
        for file in self.files:
            if file.is_file():
                if file.name[-4:] == '.mp3':
                    audiofile = eyed3.load(self.folder + file.name)
                    if audiofile.tag:
                        track_num = audiofile.tag.track_num
                        self._prefix(file.name, str(track_num[0]))

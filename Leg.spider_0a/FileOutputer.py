import os
from os import path
import downloader
import traceback

class FileOutputer(object):
    def __init__(self):
        self.downloader=downloader.Downloader()
        self.rootpath='d:\\HHaBeauty'

        if not path.exists(self.rootpath):
            os.mkdir(self.rootpath)

    def get_filename_by_url(self,filename):
        invalid_chars=[':', '/', '\\', '*', '?', '<', '>', '|']
        for char in invalid_chars:
            while char in filename:
                filename=filename.replace(char,'')
        return filename

    def out_file(self,new_imgs):
        sucessCount=0
        for img_url in new_imgs:
            try:
                binary_data=self.downloader.download_(img_url)
                filename=self.get_filename_by_url(img_url).replace('http','').replace('image.haha.mx','')
                filename_extention=filename[len-4:len-1]
                fout=open(self.rootpath+'\\'+filename+'\.'+filename_extention)
                fout.write(binary_data)
                fout.close()

                sucessCount+=1

                print('Sucess : %s' % img_url)
            except:
                traceback.print_exc()
                continue
        return sucessCount                
                
                
                

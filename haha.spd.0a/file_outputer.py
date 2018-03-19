import os
from os import path
import downloader
import traceback

class FileOutputer(object):
    def __init__(self):
        self.downloader = downloader.Downloader()
        self.rootpath = 'D:\HHaBeauty'
        if not path.exists(self.rootpath):
            os.mkdir(self.rootpath)


    def get_filename_by_url(self, filename):
        invalid_chars = [':', '/', '\\', '*', '?', '<', '>', '|']
        for char in invalid_chars:
            while char in filename:
                filename = filename.replace(char, '')

        return filename


    def output_file(self, new_imgs):
        saved_imgs=0
        for img_url in new_imgs:
            try:
                binary_data=self.downloader.download_('http:'+img_url)
                filename=self.get_filename_by_url(img_url).replace('http','').replace('image.haha.mx','').split('_')[2]
                filename_extention=filename[len(filename)-4:len(filename)]
                fout=open(self.rootpath+'\\'+filename,'wb')
                fout.write(binary_data)
                fout.close()
                saved_imgs+=1
                print('Sucess : %s' % img_url)
                '''
                binary_data = self.downloader.download_(img_url)
                filename = self.get_filename_by_url(img_url)
                fout = open(self.rootpath + '\\' + filename + '.png', 'wb')
                fout.write(binary_data)
                fout.close()
                successCount += 1
                print('图片下载成功：%s' % img_url)'''
            except:
                traceback.print_exc()
                continue
        return saved_imgs 
        

from bs4 import BeautifulSoup
import os

class HtmlParser(object):
    def __init__(self):
        self.rootpath='bw'

    def get_filename_by_url(self,filename):
        invalid_chars=[':', '/', '\\', '*', '?', '<', '>', '|']
        for char in invalid_chars:
            while char in filename:
                filename=filename.replace(char,'')
        return filename

    def get_new_img(self,soup):
        new_img=[]

        detail_wrappers=soup.find_all('div',class_='joke-main-content clearfix')

        for detail_wrapper in detail_wrappers:
            image=detail_wrapper.find('img',class_='joke-main-img')
            digg_good=detail_wrapper.find('a',class_='btn-icon-good')
            digg_bad=detail_wrapper.find('a',class_='btn-icon-bad')
            if int(digg_good.get_text)/int(digg_bad.get_text)>1.5:
                img_url_small=image.get('src')
                img_url=img_url_small.replace('small','big')
                filename=self.get_filename_by_url(img_url)
                
                jpbPath=self.rootpath+'\\'+filename+'.jpg'
                gifPath=self.rootpath+'\\'+filename+'.gif'

                if os.path.exists(jpbPath) or os.path.exists(gifPath):
                    continue
                else:
                    new_img.append(img_url)
        return new_img  

    def parse(self,html_content):
        if html_content is None:
            return
        soup=BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')

        new_img=self.get_new_img(soup)

        return new_img          



from bs4 import BeautifulSoup
import os

class HtmlParser(object):
    def __init__(self):
        self.rootpath = 'D:\\HHaBeauty'

    def get_filename_by_url(self, filename):
        invalid_chars = [':', '/', '\\', '*', '?', '<', '>', '|']
        for char in invalid_chars:
            while char in filename:
                filename = filename.replace(char, '').replace('image.haha.mx','')

        return filename

    def _get_new_imgs(self, soup):
        new_imgs = []
        # 获取每个item标签
        detail_wrappers=soup.find_all('div',class_='joke-list-item-main')

        for detail_wrapper in detail_wrappers:
            images=detail_wrapper.find_all('img',class_='joke-main-img')
            digg_good=detail_wrapper.find('a',class_='btn-icon-good')
            digg_bad=detail_wrapper.find('a',class_='btn-icon-bad')
            if int(digg_good.string)*int(digg_bad.string)!=0 and int(digg_good.string)/int(digg_bad.string)>1.5:
                for single_img in images:
                    img_url_small=single_img.get('src')
                    img_url=img_url_small.replace('small','big')
                    
                    filename=self.get_filename_by_url(img_url)
                                      
                    img_path=self.rootpath+'\\'+filename
                
                    if os.path.exists(img_path):
                        continue
                    else:
                        new_imgs.append(img_url)
        return new_imgs  
        '''
        detail_wrappers = soup.find_all('div', class_='detail-wrapper')
        for detail_wrapper in detail_wrappers:
            # 获取图片url
            image = detail_wrapper.find('img', id='groupImage', class_='upload-img')
            # 获取点赞数
            digg = detail_wrapper.find('span', class_='digg')
            if int(digg.get_text()) > 10000: # 点赞数需超过一万
                img_url = image.get('data-src')
                filename = self.get_filename_by_url(img_url)
                if os.path.exists(self.rootpath + '\\' + filename + '.png'):
                    continue
                else:
                    new_imgs.append(img_url)

        return new_imgs
    '''
        


    def parse(self, html_cont):
        if html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        new_imgs = self._get_new_imgs(soup)

        return new_imgs

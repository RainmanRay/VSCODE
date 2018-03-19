import datetime
import downloader, html_parser, file_outputer

class Spider():
    def __init__(self):
        self.downloader = downloader.Downloader()
        self.outputer = file_outputer.FileOutputer()
        self.parser = html_parser.HtmlParser()
        
    def craw(self,page_count):
        saved_img_count = 0 
        sumCount=1
        while sumCount < page_count:
            html_contentt=self.downloader.download_(start_url+str(sumCount))
                       
            new_imags=self.parser.parse(html_contentt)
            des_outs=file_outputer.FileOutputer()
            saved_img_count=des_outs.output_file(new_imags)
            print('Got %d pics' % (len(new_imags)))
            sumCount+=1
            
            '''html_cont = self.downloader.download_(start_url)
            visitCount += 1
            print('正在抓取网站：%s，总共已访问%d次' % (start_url, visitCount))
            new_imgs = self.parser.parse(html_cont)
            print('此次抓取到 %d 张图片，总共已抓取 %d 张' % (len(new_imgs), sumCount))
            sucCount = self.outputer.output_file(new_imgs)
            sumCount += sucCount'''

        return saved_img_count


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    start_url = 'https://www.haha.mx/topic/1/new/'
    spider_ = Spider()
    inputs=int(input('输入要抓取的页面数量 ：'))
    sumCount = spider_.craw(inputs)

    endtime = datetime.datetime.now()
    print('==========  抓取完成 ，总共抓取%d个页面，保存图片%d次，耗时：%s 秒 ==========' % (inputs,sumCount,str((endtime - starttime).seconds)))

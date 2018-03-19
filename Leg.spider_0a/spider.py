import datetime
import downloader
import HtmlParser
import FileOutputer

class Spider():
    def __init__(self):
        self.downloader=downloader.Downloader()
        self.outputer=FileOutputer.FileOutputer()
        self.parser=HtmlParser.HtmlParser()

    def craw(self):
        visitCount=0
        sumCount=0
        while sumCount<10000:
            html_contentt=self.downloader.download_(start_url+str(sumCount+1))
            visitCount+=1
            print('Current site is :%s, got %d images....' % (start_url,visitCount))
            new_imags=self.parser.parse(html_contentt)  
            print('Got %d pics, total count is %d' % (len(new_imags),sumCount))
            succCount=self.outputer.out_file(new_imags)
            sumCount+=succCount

        return sumCount 

if __name__=='__main__':
    startTime=datetime.datetime.now()
    start_url='https://www.haha.mx/topic/1/new/'
    spd=Spider()
    Sumcount=spd.craw()

    endTime=datetime.datetime.now()

    print('==========  抓取完成耗时：%s 秒 ==========' % (str((endtime - starttime).seconds)))


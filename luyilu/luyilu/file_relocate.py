import os
from itertools import count
from os import path
import shutil
import difflib



def relocate_file():
    src = r'D:\LuyiLuImages'
    dirs =os.listdir(src)
    dirs.sort()
    for x in dirs:
        if x.strip('').endswith('）'):
            continue
        for y in dirs[-(len(dirs)-1):]:
            if str(set(y).intersection(set(x))) == set(x):
                imgs = os.listdir(src + '\\' + y)
                for image in imgs:
                    shutil.move(src+'\\'+y+image,src+'\\'+x)

        # matchs = difflib.get_close_matches(x, dirs)
        # if len(matchs) < 2:
        #     continue
        # for each_mat in matchs[1:]:
        #     shutil.move(src+'\\'+each_mat, src+'\\'+x)




relocate_file()
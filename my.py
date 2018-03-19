'''s1=set('aadaaaaaaaaaaaa')
s2=set(tuple(('hha','ddd')))
#print(s1.remove('a'))
print(s2)
s3=('aaa',23,"adad")
print(s3.index(23))
print(s3)
for x in s3:
    print(x)'''

import re
import time
strs= "http://image.haha.mx/2018/01/30/small/2668424_02163cbf46ae6184591b6dd481acd1ee_1517294767.jpg"
mats=re.search(r"/2018/[0-9]*/[0-9]*",strs,re.M)   
print(mats.group(0))

print(time.localtime())
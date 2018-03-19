with open('data.txt','r+',encoding='utf-8') as f:
    line = f.readlines()
for x in line:
    print(x.split('|')[1])
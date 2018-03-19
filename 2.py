import os
import time

source=['c:\\lcow']

target_dir='e:\\bak'
target_name=target_dir+(os.sep+time.strftime('%Y%M%D%H%M%S')+'.zip').replace(r'/','')

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command='zip {0} {1}'.format(target_name,' '.join(source))

print('zip cmd running....')
print(zip_command)

if os.system(zip_command)==0:
    print('Done........')
else:
    print('Fail.......')
    
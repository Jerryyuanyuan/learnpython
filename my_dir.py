import os
import time

a = [x for x in os.listdir('.')]

for x in a:
    ctime = time.strftime('%Y-%m-%d',time.localtime(os.stat(x).st_ctime))
    hours = time.strftime('%H:%M:%S',time.localtime(os.stat(x).st_ctime))
    if os.path.isdir(x):
        dir_file = '<DIR>'
        sizes = ''
    else:
        dir_file=''
        sizes = os.stat(x).st_size
    print('%s\t%s\t%s\t%s\t%s' %(ctime,hours,dir_file,sizes,x))

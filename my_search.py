import os

def searchallDir1(paths,searchstr):
    '递归得到路径下的所有包含对应字符的文件'
    a = [x for x in os.listdir(paths)]
    for i in a:
        w = os.path.join(paths,i)
        if os.path.isdir(w):
            searchallDir1(w,searchstr)
        else:
            if searchstr in i:
                res.append(w)

def searchallDir2(paths):
    '递归得到路径下的所有文件'
    a = [x for x in os.listdir(paths)]
    for i in a:
        w = os.path.join(paths,i)
        if os.path.isdir(w):
            searchallDir2(w)
        else:
            res.append(w)

searchstr = input('请输入搜索内容：')
global res
res = []
searchallDir1('.',searchstr)


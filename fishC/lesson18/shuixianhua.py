import functools
def log(text = 'begin call function:'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            func(*args,**kw)
            print('end call')
            return
        return wrapper
    return decorator

@log('execute')
def shuixianhua():
    nums=100
    res = []
    while nums<1000:
        a = list(str(nums))
        sums = 0
        for i in a:
            sums = sums + int(i)**3;
        if nums == sums:
            res.append(nums)
        nums = nums + 1
    print(res)

def findStr():
    a = input("请输入目标字符串：")
    b = input("请输入子字符串（两个字符）：")
    x = a.split(b)
    print('子字符串在目标字符串中共出现 %d 次' % (len(x)-1))

shuixianhua()

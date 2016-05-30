def MyBin(a):
    '自己实现的十进制数转化为二进制数'
    res = "";
    if a==0:
        return '0b0'
    while a:
        res = str(a%2) + res;
        a = a//2
    res = '0b' + res;
    return res

print(MyBin(2))
        

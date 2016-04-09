def triangles():
##生成杨辉三角的生成器
    L = [1]
    yield L
    n = 1
    while True:
         if n==1:
            L = [1,1]
            n= n+1
         else:
            L = [1]+[L[l]+L[l+1] for l in range(n-1)]+[1]
            n=n+1
         yield L

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

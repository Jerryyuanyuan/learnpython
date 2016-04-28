import time
## 使用生成器
abc = ((a,b,c) for a in range(1,1001) for b in range(a+1,1001) for c in range(b+1,1001) if a+b+c==1000 and a**2+b**2==c**2)
##选出对的元组
timeon=time.clock()
ans = next(abc)
timeoff=time.clock()
print(ans)
print(ans[0]*ans[1]*ans[2])
print('总用时：',str(timeoff-timeon))

##while(True):
##    x = next(abc)
##    if x[0]**2+x[1]**2==x[2]**2:
##        print(x)
##        ans = x[0]*x[1]*x[2]
##        print(ans)
##        break





##abc = filter(lambda x:x[0]**2+x[1]**2==x[2]**2,abc)

##timeon=time.clock()
##ans=next(abc)
##print('a=%d,b=%d,c=%d'ans)
##print('三个数的乘积是：',str(ans[0]*ans[1]*ans[2]))

##timeoff=time.clock()
##print('总用时：',str(timeoff-timeon))

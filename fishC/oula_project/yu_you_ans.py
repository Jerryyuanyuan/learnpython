from time import clock
from math import sqrt
start = clock()
def prime(n):
    i = 0
    num = 2
    def check_prime(num):
        for i in range(2,int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
    while i<n:
        if check_prime(num):
            i +=1
        num += 1
    return i, num-1

(i,num) = prime(10001)
print('第%d个质数是：%d' %(i,num))
finish = clock()
print('用时%f秒'%(finish-start))

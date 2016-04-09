import time

def _allodds():
    a_odds = 3
    while True:
        yield a_odds
        a_odds = a_odds + 2

def prime(n):
    a_prime = 2
    if  n==1:
        return a_prime
    nums = 1
    sx = _allodds()
    while nums<n:
        a_prime = next(sx)
        sx = filter(lambda x,a_prime = a_prime: x % a_prime > 0,sx)
        nums = nums +1
    return(a_prime)

time_on = time.clock()
res=prime(10001)
time_off = time.clock()
print('用时：',str(time_off-time_on))

print(str(res),'is the 10001th prime')

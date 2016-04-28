def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    n = 2
    yield n
    it =  it = _odd_iter()#全部奇数
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

b = filter(lambda x: x<2000000,primes())
print(sum(b))

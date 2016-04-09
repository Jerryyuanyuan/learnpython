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
    print(str(a_prime),'is a prime')
    sx = _allodds()
    while nums<n:
        a_prime = next(sx)
        print(str(a_prime),'is a prime')
        sx = filter(lambda x,a_prime = a_prime: x % a_prime > 0,sx)
        nums = nums +1
    return(a_prime)

print(str(prime(10001)),'is the 10001th prime')

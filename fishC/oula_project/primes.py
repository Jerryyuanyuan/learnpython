def is_prime(x):
    flag = True
    sqrt_x = x**(0.5)
    i = 2
    while i<=sqrt_x:
        if x%i==0:
            flag = False
            break
        i += 1
    return flag

a = (2*i+1 for i in range(1,1000000) if is_prime(2*i+1))
print(sum(a)+2)

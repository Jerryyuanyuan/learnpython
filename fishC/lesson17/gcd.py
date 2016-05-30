def gcd(a,b):
    '辗转相除法求最大公约数'
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)

print(gcd(47,30))

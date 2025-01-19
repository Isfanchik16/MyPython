def gcd(m,n):
    if m<n:m,n=n,m
    rem = m % n
    if rem==0:
        return n
    return gcd(n,rem)

def factorical(number):
    if (number<=1):return 1
    return number*factorical(number-1)

def fibonacci_series(m):
    if m ==0 or m==1:return 1
    return fibonacci_series(m-1)+fibonacci_series(m-2)
print(gcd(26,12))
print(factorical(5))
print(fibonacci_series(5))

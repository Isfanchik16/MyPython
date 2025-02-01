# Greatest common divisor
def gcd(m,n):
    if m<n:m,n=n,m
    rem = m % n
    if rem==0:
        return n
    return gcd(n,rem)
print(gcd(26,12))

# Factorial
def factorical(number):
    if (number<=1):return 1
    return number*factorical(number-1)
print(factorical(5))

# Fibonacci Series
def fibonacci_series(m):
    if m ==0 or m==1:return 1
    return fibonacci_series(m-1)+fibonacci_series(m-2)

print(fibonacci_series(5))

# Bubble Sort Improvement
def bubble_1(lst): 
    len_lst = len(lst)-1
    sorted = False
    while not sorted:
        sorted = True
        for x in range(len_lst):
            if lst[x] > lst[x+1]:
                lst[x],lst[x+1] = lst[x+1],lst[x]
                sorted = False
    return lst
print(bubble_1([4,8,5,3,2,1]))

# Bubble Sort Implementation Implementation 
def bubble_2(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst
print(bubble_2([1,2,3,4,5]))


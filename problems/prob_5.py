""" Smallest multiple """

def div_by_n(a,n):
    # includes n
    for i in range(1,n+1):
        if a % i != 0:
            return False
    return True

def solve(n):
    c = 1
    while True:
        if div_by_n(c,n):
            break  
        c += 1
    return c

print('1-10:', solve(10))
print('1-15:', solve(15))
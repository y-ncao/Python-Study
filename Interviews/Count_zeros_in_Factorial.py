"""
From mitbbs for Facebook

"""

def count_zero_for_factorial(n):
    i = 1
    count = 0
    while i <= n:
        num = i
        while num % 5 == 0:
            count += 1
            num /= 5
        i += 1
    return count

def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

N = 51
print count_zero_for_factorial(N)
print fact(N)

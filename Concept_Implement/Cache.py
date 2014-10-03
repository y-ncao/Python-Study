def memcache(f):
    cache = {}
    def wrap(*xargs, **kargs):
        key = str(*xargs) + str(**kargs)
        if key in cache:
            return cache[key]
        else:
            result = f(*xargs, **kargs)
            cache[key] = result
            return result
    return wrap

@memcache
def fibo(n):
    if n <= 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print fibo(10)

# Note:
# 1. This will work for both xargs and kargs
# 2. remember you pass the func to the outter method, and return the wrap,
#    so the inner method is actually taking the arguments.

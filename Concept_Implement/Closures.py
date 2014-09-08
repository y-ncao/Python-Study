def make_closure(a):
    def inner():
        print a
    return inner

# This is a closure
closure = make_closure('lala')
print closure.__closure__
closure()

print '-' * 10

def make_not_closure(a):
    def inner(a=a):
        print a
    return inner

not_closure = make_not_closure('lala')
print not_closure.__closure__
not_closure()

# In sublime, use cmd B to run

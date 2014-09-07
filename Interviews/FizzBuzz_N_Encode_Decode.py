# Interview with Twice
# 1. FizzBuzz
# 2. Encode and decode

# FizzBuzz:
#
# 3 -> "Fizz"
# 5 -> "Buzz"
# 3 && 5 -> "FizzBuzz"
# i -> i

def FizzBuss(n):
    for i in range(1,101):
        if i % 15 == 0:
            print 'FizzBuss'
        elif i % 5 == 0:
            print 'Buzz'
        elif i % 3 == 0:
            print 'Fizz'
        else:
            print i
            

# String Encoding/Decoding
#
# Encode: ["foo", "bar", ...] -> ________
#                    ([a-z]+) -> ([a-z]+)
# Decode: ______ -> ["foo", "bar", ...]

foo, bar -> foobar -> foo, bar
'|'.join(list).lower()
split('')

[]

foobar

foobar oofarb

3 foo 3 bar
c foo c bar

def Encode(list):
    ret = []
    for word in list:
        extra = ord('a' + len(word))
        ret.append( extra + word)
    
    return ''.join(ret)
 0 1 234
# c foo c bar
def Decode(string):
    N = len(string)
    start = 0
    ret = []
    while start < N:
        length = string[start] - 'a'
        ret.append(string[start+1: start+1+length]
        start = start + length
    return ret

HTTP/1.1 GET

Content-length: 80

<body>
-HTTP/1.1 GET

-<headers>

-<body>
</body>


HTTP/1.1 GET

<headers>

<body>

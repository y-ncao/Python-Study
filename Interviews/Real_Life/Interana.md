####9/10/2014 Interview with Interana
3轮电面, 简直疯了...

#####First Round
A lot of single questions

#####Second Round
1. implement strstr
2. largest submatrix


input NxN matrix = 
     
0 1 0*0 0 0
0*0 0 0 0 0
0 0 0 0 1 0
1 0 0 0<0 0
0 0 1 0 0 1
0 0 0 1 1 0

line 3 
1->
dp (1,1)  (0,0)

2 -> 1
continue

3 ->

ie return 3 ^^

return size of largest sub-square matrix where all bits == 0. 

O(N^2)* O(N^2)
O(N^4)

lior@interana.com


def largestRect(matrix):
    row = len(matrix)
    col = len(matrix[0])
    # Until (x,y) what is the largest zero matrix
    dp = [ [ (0,0) for j in range(col)] for i in range(row)] ]
    max_area = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '1':
               contine
            if j == 0:
                x = 1
            else:
                x = dp[i][j-1][0] + 1
            if i == 0:
                y = 1
            else:
                y = dp[i-1][j][1] + 1
            dp[i][j] = (x, y)
            
            min_width = y
            for k in range(j-x+1, j+1)[::-1]:
                min_width = min(min_width, dp[i][k][1])
                max_area = max(max_area, min_width * (j-k+1))
     return max_area
     
     sorry think we got disconnected.
     yes, my phone's battery is out
     one moment it need to be awake, it's a old iphone,I just got it plugged
     
     VERRRRY SORRRY yes
     k let me know when i can call. still white apple. sorry about it
     it's back
     k :)
     k dialing in 5s
O(n^3)     

substring function. args = needle, and haystack. 

if needle is substr of haystack, return index of first, else return -1

needle[0] 

def substring(needle, haystack):
    H = len(haystack)
    N = len(needle)
    for i in range(H-N+1):
        if haystack[i] == needle[0]:
            start_H = i + 1
            start_N = 1
            while haystack[start_H] == needle[start_N]:
                start_H += 1
                start_N += 1
            if start_N == N:
                return True
    
    return False
    
O(N*H)

pppppppppppppppLpppppL          pppppp  


#####Last round

session

15min

check if session is in memecached
1 db hit

4 db hit per hour

deleted create

session_id user permission


userID userObj

getobjectbyID()

def func(userObj):
  print userObj.id, userObj.name

id = "001" # Channing
id2 = "002" # Yan

@getUserCached
getUser(id, func)  # return None
getUser(id2, func) # return None

# New Function Caches the result of getUser that behaves like getUser
getUserCached(id, func)


Class Cache()
    def __init__(self, size):
        self.size = size
        OrderedDict
def getUserCached(f, ):
    cache = {}
    counter = 0
    def helper(x):
        if counter a
        if x not in cache:
            counter += 1
            cache[x] = f(x)
        return cache[x]
    return helper
    def get():
        if key in cache:
            value = cache[key]
            return value
    
    def set():
       if key not in self.cache and len(self.cache) >= self.size:
           self.cache.popItem(last=False)
       elif key

    queue.remove(key)
    
    queue.append(key)
send data client

hash(object)

copy cache
key cache
copy user
key user

1. update in db
   1. time to live
   2. just check hash key same object

reduce traffic

cost too much process data server 
    -> cache
update



# 001 Channing
# 002 Yan

# OR

# 002 Yan
# 001 Channing
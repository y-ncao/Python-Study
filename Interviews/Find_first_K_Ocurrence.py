"""
#####Interview with Pocket Gem 9/15/2014
1. strstr
2. Find Highest K Occurrence
"""

"""
strstr

input:
   basestring,
   patternstring

output
  index in basestring where pattern occurs first
  else -1


example:
  'pineapple', 'eap'-> 3
  'pineapple', 'orange' -> -1

  'pineapple', 'apple'

    pineappl   apple

  ppppppSppppppSpppppp.....     ppppppp
   |
str1.find(str2)

O(B*P)
"""

def strstr(basestring, patternstring):
    B = len(basestring)     # B = 9
    P = len(patternstring)  # P = 5
    if P > B:
        return -1
    for i, char in enumerate(basestring[:B-P+1]): # 9-5+1 = 5 p i n e a
        if patternstring[0] == char:              # a 
            start_b = i+1                         # basestring[start_b] = 'p'
            start_p = 1                           # 'p'
            while start_p < P and patternstring[start_p] == basestring[start_b]:
                start_b += 1
                start_p += 1
            if start_p == P:
                return i

    return -1

"""
List of integers and value of K,
return K most occurring numbers from list

example :
  [1,5,3,2,6,6,2,2,2,6,1,2,89]
k = 1
[2]
k = 2
[2, 6]
k = 3
[2, 6, 1]

priorityQueue( (ocurr, value) )
sort by ocurr

(ocurr, value) update ocurr push again.
"""

def findKmost(list, K):
    pq = []
    d = {}
    for el in list:
        if get_ocurr(pq, el) > 0:
            ocurr = get_ocurr(pq,el)
            update(pq, el)
            # removeEl(pq, el)
            # heappush(pq, (ocurr+1, el)) /// what is heappush?
        else:
            heappush(pq, (1, el))
    ret = []
    for i in range(k):
        ocurr, el = heappop(pq)
        ret.append(el)
    return ret
"""
list = []
                key   value
heappush(list, (arg1, arg2))

list = [1,2,3,4,1]

maxheap
             (2,1)
         (1,4)  (1,2)
       (1,3)
O(nlg(n)+K)
"""

def update(pq, el):
    for i in pq:
        if i[1] == el:
            i[0] +=1

def get_ocurr(pq, el):
    for i in pq:
        if i[1] == el:
            return i[0]
    return 0

def removeEl(pq, el):
    for i in pq:
        if i[1] == el:
            del i

# Should do:
def find_k_ocurrance(list, k):
    d = {}
    for el in list:
        if el not in d:
            d[el] = 0
        d[el] += 1
    occur_list = []
    for el, occur in d.iteritems():
        occur_list.append((occur, el))

    occur_list.sort(key=lambda x: x[0], reverse=True)    # WO ZHEN SHI SHA BI. Use list.sort instead of sorted(list). sorted(list) wont sort in place. need to assign

    ret = []
    for i in range(k):
        ret.append(occur_list[i][1])
    return ret

a = [1,5,3,2,6,6,2,2,2,6,1,2,89]
print find_k_ocurrance(a, 2)

# Note
# import heapq
# 1. heappush(pq, (value, key))
# 2. heappop()
# 3. Don't think too complicated
# 4. the way to sort, and use lambda
# 5. sorted(key=lambda x: x[0], reverse=True)

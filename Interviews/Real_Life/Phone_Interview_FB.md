#####9/15/2014 Interview with Facebook
1. zip a *
2. Level Order Traversal for a Tree


      7
    4    2
  9  5  8  3


output:
7\n
42\n
9583\n

BFS

O(n)

array
get_by_index

O(1)
[]

-1

[0,1,2,3,4,5]


collections.deque()

def BFS(root):
    queue = [root,]
    
    while len(queue) > 0:
        size = len(queue)
        level = []
        for i in range(size):
            node = queue.pop()
            level.append(node.val)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        print ''.join(level), '\n'
        
        
     ' '.join([a b c])
    









A = [1, 0, 4, 2]
B = [3, 1, 0, 4]

A dot B = 1*3 + 0*1 + 4*0 + 2*4 = 3 + 8 = 11

C = [x*y for (x, y) in zip(A, B)]

A' = [[0, 1], [2, 4], [3, 2]]# [1,0]
B' = [[0, 3], [1, 1], [3, 4]]

A [1, 0]
B [1, 1] = 0

start_A [2, 4]
start_B [1, 1]


start_B += 1

m = len(A)
n = len(B)

O(m+n)
def produce_dot(A, B):
    start_A = 0
    start_B = 0
    res = 0
    while start_A < len(A) and start_B < len(B):
        if A[start_A][0] == B[start_B][0]:
            res += A[start_A][1] * B[start_B][1]
            start_A += 1
            start_B += 1
        elif A[start_A][0] > B[start_B][0]:
            start_B += 1
        else:
            start_A += 1
    
    return res
         
search for index_B in A
Binary search B[index_B][0]

O(n*logm)
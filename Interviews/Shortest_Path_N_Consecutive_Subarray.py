'''
2D array of characters
1 1 1 1 1
S 1 X 1 1
1 1 1 1 1
X 1 1 E 1
1 1 1 1 X

S is the starting point
E is the ending point
X means you cannot traverse to that point

1. #Find the shortest path from S to E given the above matrix
2. Find if there is a path from S to E

Restriction: Move to 8 positions
*/
'''

# Divide and conquer
def find_shortest_path(matrix, C, E, visited):
    if C == E:
        return 0
    x, y = C
    if x < 0 or y < 0 or x > len(matrix) or y > len(matrix[0]):
        return INT_MAX
    if matrix[x][y] == 'X':
        return INT_MAX
    # 考虑visited
    
    return min(find_shortest_path(matrix, (x+1, y), E, visited)



visited = {}
# BFS (没考虑X路障)
def find_shortest_path(matrix, S, E):
    M = len(matrix)
    N = len(matrix[0])
    visited = {}
    start_path = [S,]
    queue = [(S, start_path)]
    while len(queue) > 0:
        cur_node, cur_path = queue.pop()
        x, y = cur_node
        if x < 0 or y < 0 or x >= M or y >= N or matrix[x][y] == 'X':
            continue
        if cur_node in visited:
            continue
        else:
            visited[cur_node] = True
        new_path = cur_path[:].append(cur_node)
        if cur_node == E:
            return new_path

        queue.insert(0, ((x+1, y), new_path))
        queue.insert(0, ((x+1, y+1), new_path))
        queue.insert(0, ((x+1, y-1), new_path))
        queue.insert(0, ((x-1, y), new_path))
        queue.insert(0, ((x-1, y-1), new_path))
        queue.insert(0, ((x-1, y+1), new_path))
        queue.insert(0, ((x, y+1), new_path))
        queue.insert(0, ((x, y-1), new_path))


def find_shortest_path(matrix):
    M = len(matrix)
    N = len(matrix[0])
    S, E = find_start_end(matrix)
    if not S or not E:
        return -1
    visited = {}
    queue = [S,]
    while len(queue) > 0:
        cur = queue.pop()
        if cur == E:
            return True
        x, y = cur
        if matrix[x][y] == 'X':
            continue
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix):
            continue
        if cur not int visited:
            visited[cur] = True
        else:
            continue
        queue.insert(0, (x+1, y))
        queue.insert(0, (x+1, y+1))
        queue.insert(0, (x+1, y-1))
        queue.insert(0, (x-1, y))
        queue.insert(0, (x-1, y-1))
        queue.insert(0, (x-1, y+1))
        queue.insert(0, (x, y+1))
        queue.insert(0, (x, y-1))

def find_start_end(matrix):
    M = len(matrix)
    N = len(matrix[0])
    S = None
    E = None
    for i in range(M):
        for j in range(N):
            if matrix[i][j]  == 'S':
                S = (i, j)
            if matrix[i][j] == 'E':
                E = (i, j)
    return (S,E)

'''
# Prob 2:
[1, 4, 20, 10, 3, 5, 9] # (20, 10, 3) Sum=33 Also the subarray must be consecutive
Note: All elements are positive integers exception: array can include 0
Note: You cannot sort the array
1
4
20
'''

# This is O(n^2)
def find_consecutive(num, sum):
    N = len(num)
    for i in range(N-1):
        cur_sum = 0
        for j in range(i, N):
            cur_sum += num[j]
            if cur_sum == sum:
                return (i, j)
            elif cur_sum > sum:
                break
    return -1

# This is O(n), very similar to KMP
def find_consecutive(num, sum):
    N = len(num)
    cur_sum = 0
    i = 0
    j = 0
    while j < N:
        if cur_sum + num[j] == sum:
            return num[i:j+1]
        elif cur_sum + num[j] < sum:
            cur_sum += num[j]
            j += 1
        else:
            cur_sum -= num[i]
            i += 1
    return -1

num = [9, 1, 4, 20, 10, 3, 5]
sum = 33
print find_consecutive(num, sum)


def add(x):
    def temp(y):
        return add(x+y)
    return temp

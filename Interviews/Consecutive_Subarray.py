"""
#####Interview With Cyan
1. Shortest Path
2. Consecutive Subarray

#####Prob 2:
[1, 4, 20, 10, 3, 5, 9] # (20, 10, 3) Sum=33 Also the subarray must be consecutive
Note: All elements are positive integers exception: array can include 0
Note: You cannot sort the array
1
4
20
"""

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

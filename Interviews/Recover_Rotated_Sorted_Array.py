"""
Given a rotated sorted array, recover it to sorted array in-place.

Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

NC Class 2, slides 32
Solution three way reverse
"""

def recover_rotated_sorted_array(A):
    N = len(A)
    rotate_start = -1
    for i in range(1, N):
        if A[i-1] > A[i]:
            rotate_start = i
            break
    first_part = A[:rotate_start]
    second_part = A[rotate_start:]
    total = first_part[::-1] + second_part[::-1]
    return total[::-1]

A = [4, 5, 1, 2, 3]
print recover_rotated_sorted_array(A)

# I really have no idea why I need to reverse every time, but basically this works

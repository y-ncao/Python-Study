"""
#####From [Geeksforgeeks](http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/)

Similar to CC150, just allow coin with 1, 3, 5 right now

Several ways to ask
1. How many ways?
2. What are the ways?
3. Minimum coin number?
"""

# This is same to Combination Sum I
def coin_change(value):
    res = [0, 0, 0]                     # [num_5, num_3, num_1]
    ret = []
    coin_change_helper(0, value, res, ret)
    return ret

def coin_change_helper(cur_face_value, rest_value, res, ret):
    if rest_value == 0:
        ret.append(res[:])

    for i in range(cur_face_value, 3):
        if rest_value - [5, 3, 1][i] < 0:
            continue
        res[i] += 1
        coin_change_helper(i, rest_value - [5, 3, 1][i], res, ret)
        res[i] -= 1

print coin_change(5)

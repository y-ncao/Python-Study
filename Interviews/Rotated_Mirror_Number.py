"""
####From Alec's email, someone's onsite interview with Facebook for finding rotated mirrow number like 808 which is less than N

"""

def rotated_mirror_number(n):
    length = 0
    while n - 10**length > 0:
        length += 1
    ret = []
    rotated_helper(n, length, [], ret)
    return ret

def rotated_helper(n, length, res, ret):
    num = convert_to_num(res)
    if num > n or len(res) > length:
        return
    if len(res) > 0 and res[0] != 0:
        ret.append(num)
    if len(res) == 0:
        for i in range(10):
            res.append(i)
            rotated_helper(n, length, res, ret)
            res.pop()

    for i in range(10):
        res.append(i)
        res.insert(0,i)
        rotated_helper(n, length, res, ret)
        res.pop()
        res.pop(0)

def convert_to_num(int_list):
    res = 0
    for digit in int_list:
        res = res*10 + digit
    return res


print rotated_mirror_number(10000)

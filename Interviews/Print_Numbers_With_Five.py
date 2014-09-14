"""
##### 9/7/2014 From [mitbbs](http://www.mitbbs.com/article_t/JobHunting/32651839.html) for Groupon
写一个function，对于参数n，输出从0到n之间所有含5的数字。
func(30) 应该输出5，15，25
"""

def find_five(n):
    ret = []
    helper(ret, [], n)
    return ret

def helper(ret, res, n):
    if len(res) > 0 and ( int(''.join(res)) > n or len(res) > len(str(n)) ):
        return
    if '5' in res and int(''.join(res)) not in ret:
        ret.append(int(''.join(res)))

    for i in range(10):
        res.append(str(i))
        helper(ret, res, n)
        res.pop()

print find_five(60)

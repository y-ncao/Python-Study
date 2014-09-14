"""
#####First round interview with Quantcast
1. How to get 100 largest numbers from 1 million nums?  
   By using __min_heap__
   注意这里的重点是必须用的是min heap
   方法是, 先建立一个大小为100的min heap, 然后iterate剩下的数字, 如果小于minheap里的min就discard, 如果大于minheap里的min就push, 最后pop所有在里面的,  剩下的前100就是前100

2. How to get uni7() from uni5()
"""

def uni7():
    # 先通过uni5()得到 0 ~ 24的随机数
    while True:
        random = uni5() * 5 + uni5()
        if random < 21:
            break
    return random % 7
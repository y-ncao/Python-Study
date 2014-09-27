"""
#####From [mitbbs](http://www.mitbbs.com/article_t/JobHunting/32782345.html) for Amazon Interview
Given three arrays A,B,C containing unsorted numbers. Find three numbers a,
b, c from each of array A, B, C such that |a-b|, |b-c| and |c-a| are minimum
Please provide as efficient code as you can.

Note:
if a > b > c:
|a-b| + |b-c| + |c-a| = 2(a-c)
so this will always equals 2(max_num - min_num)

"""

def get_min_distance(A1, A2, A3):
    A1.sort()
    A2.sort()
    A3.sort()

    index_1 = 0
    index_2 = 0
    index_3 = 0

    min_distance = sys.maxint

    while True:
        min_num = min(A1[index_1], A2[index_2], A3[index_3])
        max_num = max(A1[index_1], A2[index_2], A3[index_3])
        distance = 2(max_num - min_num)
        min_distance = min(min_distance, distance)
        if min_distance == 0:
            break

        if min_num == A1[index_1] and index_1 < len(A1):
            index_1 += 1
        elif min_num == A2[index_2] and index_2 < len(A2):
            index_2 += 1
        elif min_num == A3[index_3] and index_3 < len(A3):
            index_3 += 1
        else:
            break
    return

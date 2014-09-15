"""
From [mitbbs](http://www.mitbbs.com/article_t/JobHunting/32760941.html) for facebook
"""

def is_one_edit_distance(s1, s2):
    M = len(s1)
    N = len(s2)
    if abs(M-N) >= 2:
        return False
    if M != N:
        if M > N:
            longer = s1
            shorter = s2
        else:
            longer = s2
            shorter = s1
        i = 0
        j = 0
        counter = 0
        while i < len(shorter) and j < len(shorter):
            if longer[i] != shorter[j]:
                j += 1
                counter += 1
            else:
                i += 1
                j += 1
            if counter > 1:
                return False
        return True

    else:
        counter = 0
        for i in range(M):
            if s1[i] != s2[i]:
                counter += 1
                if counter > 1:
                    return False
        return True

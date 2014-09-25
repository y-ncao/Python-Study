"""
From [Career Cup](http://www.careercup.com/page?pid=pinterest-interview-questions) Pinterest

Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. You need to output the minimum number of words. For example, input: "aaaisaname"
dict: ("a", "aaa", "is", "name")

output: "aaa is a name"

Wrong output: "a a a is a name"
"""
import sys

def print_min_num_words(str, d):
    N = len(str)
    dp = [ N for i in range(N+1)]
    dp[0] = 0
    d.append('')
    for i in range(1, N+1):
        if str[:i] in d:
            dp[i] = 1
        for j in range(i)[::-1]:
            #print i, j, str[j:i], dp
            if str[j:i] in d and dp[j] != sys.maxint:
                dp[i] = min(dp[i], dp[j]+1)

    # Use dp to get the min_num words
    cur = dp[N]
    last = N+1
    res = []
    for i in range(N)[::-1]:
        if dp[i] == cur - 1:
            res.insert(0, str[i:last])
            last = i
            cur -= 1
    return res

str = 'aaaisaname'
d = ["a", "aaa", "is", "name"]

print print_min_num_words(str, d)

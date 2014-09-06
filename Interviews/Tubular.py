# 9/4/2014 Interview with Tubular

# 1. Subset(秒了)
# 2. LCS

#This is the text editor interface. 
# Anything you type or change here will be seen by the other person in real time.
# "abc", "zyabcbcyz" -> "abc"
'''
len(a) -> m
len(b) -> n

m!

1 substring for
1 m    m+1
2 m-1
3 m-2

(1+m) * m / 2 

m^2



1 ->m
2 ->m/2

0 m
log(m)

dp 
# state: dp[i][j] ith char in a and jth char in b, the len of LCS is dp[][]
# function dp[i][j] = 0 if a[i-1] != b[i-1]
#                     dp[i-1][j-1] + 1
#          max(dp[i][j]) for each i and j
'''

def longest_common_substring(a,b):
    m = len(a)
    n = len(b)
    dp = [ [ 0 for i in range(n+1)] for j in range(m+1) ]
    res = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0
    return res
    
    

# "abcdefg"
print(longest_common_substring("abc", "abz"))
print(longest_common_substring("abcdefgabyzzkabcde", "zzzzzzgabyzzabcabcdefg"))
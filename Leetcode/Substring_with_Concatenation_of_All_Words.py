"""
You are given a string, S, and a list of words, L, that are all of the same length.
Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        len_word = len(L[0])
        len_L = len(L)
        len_S = len(S)
        ret = []
        for i in range(len_S - len_word * len_L + 1):
            list_S = [ S[j:j+len_word] for j in range(i, i + len_L*len_word, len_word)]
            found = True
            for word in L:
                if word in list_S:
                    list_S.remove(word)
                else:
                    found = False
                    break
            if found:
                ret.append(i)
        return ret

    # Note
    # 1. The idea is to slice S to S[i: i+len_L*len_word: len_word] and compare S's substring list with L
    #    Can improve it with i. replacing the list to dict increase search. ii. KMP
    # 2. This is good enough. Can use KMP but it's too complicated.
    #    See http://c4fun.cn/blog/2014/03/20/leetcode-solution-02/#Substring_with_Concatenation_of_All_Words
    #    for KMP solution
    # 3. Notice line 23, wrapping everything in the range is fast than calculate them in list comprehension

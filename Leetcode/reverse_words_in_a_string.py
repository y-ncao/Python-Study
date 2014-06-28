"""
Given an input string, reverse the string word by word.

For example,
Given s = 'the sky is blue',
return 'blue is sky the'.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return self.reverse_words_in_str_2(s)

    def reverse_words_in_str_1(self, str):
        return ' '.join(str.split()[::-1])

    def reverse_words_in_str_2(self, str):
        res = ''
        word = ''
        for char in str:
            if char != ' ':
                word += char
            elif len(word) > 0:
                if res != '':
                    res = ' ' + res
                res = word + res
                word = ''

        if len(word) > 0:
            if res != '':
                res = ' ' + res
            res = word + res
        return res

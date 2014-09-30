"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
"""

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        cur_len = 0
        res = []
        ret = []
        for word in words:
            if cur_len + len(word) + len(res) <= L:
                res.append(word)
                cur_len += len(word)
            else:
                if len(res) == 1:
                    ret.append(self.fill_spaces(res[0], L))
                else:
                    extra_spaces = L - cur_len - (len(res) - 1)
                    each_extra = extra_spaces / (len(res) - 1) + 1
                    rest_spaces = extra_spaces % (len(res) - 1)
                    for i in range(rest_spaces):
                        res[i] += ' '
                    line = (' ' * each_extra).join(res)
                    ret.append(line)
                res = []
                res.append(word)
                cur_len = len(word)
        ret.append(self.fill_spaces(' '.join(res), L))
        return ret

    def fill_spaces(self, string, L):
        length = len(string)
        string += ' ' * (L - length)
        return string

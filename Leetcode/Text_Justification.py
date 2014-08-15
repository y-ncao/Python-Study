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
        return self.fullJustify_1(words, L)

    def fullJustify_1(self, words, L):
        ret = []
        N = len(words)
        i = 0
        while i < N:
            length = len(words[i])
            j = i + 1
            while j < N and length + len(words[j]) + j - i < L:
                length += len(words[j])
                j += 1

            # start to build a line
            is_last_line = (j == N)
            is_single = (j == i + 1)
            if is_last_line or is_single:
                average = 0
                extra = L - length
            else:
                average = (L - length) / (j-i-1)
                extra = (L - length) % (j-i-1)
            for k in range(extra):       # Note its j not j+1
                words[i+k] += ' '
            ret.append((' '*average).join(words[i:j-1]))
            i = j
            print ret
        return ret


    def fullJustify_2(self, words, L):
        ret = []
        N = len(words)
        i = 0
        res = []
        counter = 0
        while i < N:
            if len(words[i]) + len(res) + counter <= L: # Need to consider space between words
                res.append(words[i])
                counter += len(words[i])
                i += 1
            else:
                if len(res) == 1:
                    last = ' '.join(res)
                    last += ' ' * (L - len(last))
                    ret.append(last)
                else:
                    spaces = L - counter
                    least_fill = spaces / (len(res)-1)
                    rest = spaces % (len(res)-1)
                    for j in range(rest):
                        res[j] += ' '
                    ret.append((' '*least_fill).join(res))
                counter = 0
                res = []
            #assert(len(res) < 4)
        if len(res) > 0:
            last = ' '.join(res)
            last += ' ' * (L - len(last))
            ret.append(last)
        return ret

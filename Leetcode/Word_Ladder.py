"""
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([(start, 1)])
        N = len(start)
        while len(queue) > 0:
            word, depth = queue.popleft()
            if word == end:
                return depth
            for i in range(N):
                before = word[:i]
                after = word[i+1:]
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char != word[i]:
                        new_word = before+char+after
                        if new_word in dict:
                            queue.append((new_word, depth+1))
                            dict.remove(new_word)
        return 0

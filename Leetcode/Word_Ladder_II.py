"""
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        trace_back = { word: [] for word in dict}
        prev_level = set([start])
        found = False
        while len(prev_level) > 0 and not found:
            cur_level = set([])
            size = len(prev_level)
            for word in prev_level:
                dict.remove(word)
            for word in prev_level:
                if word == end:
                    found = True
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in dict:
                            trace_back[new_word].append(word)
                            cur_level.add(new_word)
            prev_level = cur_level
        paths = []
        if found:
            self.find_traceback(end, trace_back, [], paths)
        return paths

    def find_traceback(self, word, trace, cur_path, paths):
        if len(trace[word]) == 0:
            paths.append([word] + cur_path)
            return
        for prev_word in trace[word]:
            self.find_traceback(prev_word, trace, [word] + cur_path, paths)

    # Note:
    # 1. while loop is doing a BFS
    # 2. find_traceback is doing a DFS from the end traceback to start

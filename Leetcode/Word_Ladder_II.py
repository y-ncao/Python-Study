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
        ret     = []
        prevMap = {}
        length  = len(start)
        for i in dict:
            prevMap[i] = []
        candidates = [set(),set()]
        current    = 0
        previous   = 1
        candidates[current].add(start)
        while True:
            current, previous=previous, current
            for i in candidates[previous]: dict.remove(i)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(length):
                    part1=word[:i]; part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword=part1+j+part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)
            if len(candidates[current])==0:
                return ret
            if end in candidates[current]: break
        self.buildpath([], end, prevMap, ret)
        return ret

    def buildpath(self, path, word, prevMap, ret):
        if len(prevMap[word])==0:
            path.append(word)
            currPath=path[:]
            currPath.reverse()
            ret.append(currPath)
            path.pop();
            return
        path.append(word)
        for prev in prevMap[word]:
            self.buildpath(path, prev, prevMap, ret)
        path.pop()

"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        path_list = path.strip('/').split('/')
        ret = []
        jump = 0
        for p in path_list[::-1]:
            if p == '.' or p == '':
                continue
            elif p == '..':
                jump += 1
            else:                       # p is a valid path
                if jump > 0:
                    jump -= 1
                else:
                    ret.insert(0, p)
        return '/'+'/'.join(ret)
    # Note:
    # 1. Remove dup '/', if using split(), // will become '', remove it
    # 2. Keep in mind those two [::-1]
    # 3. Don't forget to attach the first '/'

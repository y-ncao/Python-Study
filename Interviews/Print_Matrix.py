"""
####From [mitbbs](http://www.mitbbs.com/article_t/JobHunting/32570751.html) for Pinterest

Print a N x M matrix in diagonal from the upper left to lower right. However, with the following caveat. It's easy to just show the input and expect output.
```
matrix:
a b c d
e f g h
i j k l
m n o p

output:
a f k p
b g l
c h
d
e j o
i n
m
```
"""

def print_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        start = 0
        while start + i < N:
            print matrix[start][i+start],
            start += 1
        print '\n'

    for i in range(1, N):
        start = 0
        while start + i < N:
            print matrix[i+start][start],
            start += 1
        print '\n'

matrix = ['abcd', 'efgh', 'ijkl', 'mnop']
print_matrix(matrix)

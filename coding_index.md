## Coding Summary by Keywords and Type

###Permutation & Combination Type
* [x] Permutations
* [x] Permutations II
* [x] Next Permutation
* [x] Permutation Sequence

-----

* [x] Combinations
* [x] Combination Sum
* [x] Combination Sum II
* [x] Letter Combination of a Phone Number

-----

######Note:
做Permutation, Combination和Subset的感觉非常像，注意

1. 结束条件都是用完所有可用的char, 也就是i == len(n). 然后在ret.append(res[:]), 这里千万别忘了要return cancel函数
2. 做for循环的时recursion函数的输入会有差别(记得这里用enumerate会方便好多)
  1. Permutation传入剩余num_list 是 num[:i] + num[i+1], 因为只是除去当前数字, permute剩余
  2. Combination传入剩余num_list 是 num[i+1:],  因为除去比当前数字之前的数, combine剩余
  3. Subsets其实也应该是S[i+1:],除去之前可能的set. 但是与前两者不同的是循环的内容不同， Subset只有存在和不存在两种情况，所以等于是loop一个恒为2的循环，而第一种情况还有特殊条件，这个一定要仔细看好。
  4. Permutation&Combination两者相同的地方都是
    1. res.append(n)
    2. do combine_rec/permute_rec
    3. res.pop()
3. 仔细观察这三道题就会发现, 其实I都是输入没有重复, 而II都是输入有重复,但输出不能有重复的题目.

-----

* [x] Gray Code

-----

* [x] Subset
* [x] Subset II

-----

* [x] Generate Parentheses
* [x] Valid Parentheses
* [x] Longest Valid Parentheses

-----

* [x] Palindrome Number
* [x] Valid Palindrome
* [x] Palindrome Partitioning
* [x] Palindrome Partitioning II

###Tree Traversal
* [x] Binary Tree Inorder Traversal
* [x] Binary Tree Preorder Traversal
* [x] Binary Tree Postorder Traversal
* [x] Binary Tree Level Order Traversal
* [x] Binary Tree Level Order Traversal II
* [x] Binary Tree Zigzag Level Order Traversal

_____

* [x] Construct Binary Tree from Preorder and Inorder Traversal (Redo)
* [x] Construct Binary Tree from Inorder and Postorder Traversal (Redo)

-----

* [x] Same Tree
* [x] Balanced Binary Tree
* [x] Symmetric Tree
* [x] Maximum Depth of Binary Tree
* [x] Minimum Depth of Binary Tree

###Binary Search Tree
* [x] Convert Sorted Array to Binary Search Tree
* [x] Unique Binary Search Trees
* [x] Unique Binary Search Trees II
* [x] Validate Binary Search Tree (Redo)
* [x] Recover Binary Search Tree (Redo)

###类Tree(以tree作为Data Structure的题目)
* [x] Path Sum
* [x] Path Sum II
* [x] Populating Next Right Pointers in Each Node
* [x] Populating Next Right Pointers in Each Node II
* [x] Sum Root to Leaf Numbers
* [x] Flatten Binary Tree to Linked List
* [x] Binary Tree Maximum Path Sum

###Array(意义不大)
* [x] Maximum Subarray
* [x] Convert Sorted Array to Binary Search Tree
* [x] Merge Sorted Array
* [x] Remove Duplicates from Sorted Array
* [x] Remove Duplicates from Sorted Array II
* [x] Search in Rotated Sorted Array
* [x] Search in Rotated Sorted Array II
* [x] Median of Two Sorted Arrays

* [x] Remove Element

###List(意义不大)
* [x] Linked List Cycle
* [x] Linked List Cycle II
* [x] Remove Duplicates from Sorted List
* [x] Remove Duplicates from Sorted List II
* [x] Merge Two Sorted Lists
* [x] Remove Nth Node From End of List
* [x] Partition List
* [x] Reverse Linked List II (Why only II??)
* [x] Insertion Sort List (Insertion Sort)
* [x] Copy List with Random Pointer
* [x] Merge k Sorted Lists
* [x] Rotate List
* [x] Sort List (Merge Sort)
* [x] Reorder List
* [x] Reverse Nodes in k-Group

######Dup with tree
* [x] Flatten Binary Tree to Linked List
* [x] Convert Sorted List to Binary Search Tree

###Matrix
* [x] Search a 2D Matrix
* [x] Spiral Matrix
* [x] Spiral Matrix II
* [x] Set Matrix Zeroes
* [x] Valid Sudoku
* [x] Sudoku Solver

###Play With Math
* [x] Reverse Integer
* [x] Roman to Integer
* [x] Intger to Roman
* [x] Pascal's Triangle
* [x] Pascal's Triangle II

-----

###Dynamic Programming
* [x] Climbing Stairs
* [x] Maximum Subarray
* [x] Minimum Path Sum
* [x] Unique Binary Search Tree
* [x] Container With Most Water
* [x] Unique Paths
* [x] Unique Paths II
* [x] Unique Binary Search Trees
* [x] Unique Binary Search Trees II
* [x] Best Time to Buy and Sell Stock III
* [x] Jump Game
* [x] Jump Game II
* [x] Longest Consecutive Sequence
* [x] Triangle
* [x] Edit Distance
* [x] Distinct Subsequences
* [x] Maximal Rectangle (DP isn't the best way)
* [x] Longest Palindromic Substring
* [x] Scramble String
* [x] Palindrome Partitioning II
* [x] Interleaving String
* [x] Word Break
* [x] Decode Ways

现在对于dp的理解还是差一些，小总结下：

我觉得dp的思路大概是这样的

1. 思考问题，确定需要用dp解决，然后确定需要用几维的dp，dp的每个值的意思是什么
2. 确定转移方程
3. 思考边界条件，还有dp的长度，有的时候是N, 有的时候是N+1
4. 看是否可以简化dp，二维简化成一维，一般来说如果是
```python
for i in range(A):
    for j in range(B):
        transfer dp[i][j] to dp[i-1][j-1]
```
这种情况的话， 由于j每次都在使用dp[j-1], 这种情况没必要储存dp[j-1],只需要把dp[i][0] 确认之后每行从1开始遍历前一项即可。

-----

##From class

###模板
* 状态 state: 灵感, 创造力, 储存小规模问题的结果
* 转移方程 transfer function: 状态之间的联系, 怎么通过小的状态来算大的状态
* 初始化 initialization: 最极限的小状态是什么
* 答案 answer: 最大的那个状态是什么

###Clues
1. Cannot sort, or swap
2. Satisfy:
  * Find a maximum/minimum result
  * Decide whether something is possible or not
  * Count all possible solutions(Doesn't care about solution details, only care about the count or possibility)

###Types of DP

####1. Matrix DP 20% (Triangle, Unique Path)
* state: ```dp[x][y]```表示从起点走到坐标 (x,y) 的xxx
* function: 研究下一步怎么走
* initialize: 起点
* answer: 终点

#####[Unique Path](./Leetcode/Unique_Paths.py)
* state: ```dp[x][y]```表示从起点走到 (x,y) 的path数
* function: ```dp[x][y] = dp[x-1][y] + dp[x][y-1]```
* initialize: ```dp[0][y] = 1, dp[x][0] = 1```
* answer: ```dp[n-1][m-1]```

#####[Unique Path II](./Leetcode/Unique_Paths_II.py)
* function: ```if 障碍, dp[x][y] = 0```

#####[Minimum Path Sum](./Leetcode/Minimum_Path_Sum.py)
* state: ```dp[x][y]```表示从起点走到x,y的minimum path sum
* function: ```dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x][y]```
* initialize: ```dp[0][0] = grid[0][0], dp[x][0] = dp[x-1][0] + grid[x][0], dp[0][y] = dp[0][y-1] + grid[0][y]```
* answer: ```dp[m-1][n-1]```

-----

####2. One Sequence DP 40%
* state: dp[i]表示前i个位置/数字/字母，以第i个为...
* function: ```dp[i] = dp[j] ...j``` 是i之前的一个位置
* initialize: ```dp[0] = ...```
* answer: ```dp[n-1]```

######[Climbing Stairs](./Leetcode/Climbing_Stairs.py)
* state: dp[i]表示爬到第i个台阶时的方法数
* function: ```dp[i] = dp[i-1] + dp[i-2]```
* initialize: ```dp[0] = 1, dp[1] = 1```
* answer: ```dp[n]```


######[Jump Game](./Leetcode/Jump_Game.py) | [Jump Game II](./Leetcode/Jump_Game_II.py)
* state: dp[i]表示能否跳到第i个位置 | dp[i]表示跳到这个位置最少需要多少步.
* function: ```dp[i] = or(dp[j], j < i and j能跳到i)``` | ```min(dp[j] + 1, j < i and j能跳到i)```
* initialize: ```dp[0] = True``` | ```dp[0] = 0```
* answer: ```dp[n-1]```

######[Palindrom Partitioning II](./Leetcode/Palindrome_Partitioning_II.py)
* state: dp[i]表示前i个字符组成的字符串需要最少几次cut
* function: ```dp[i] = min( dp[j]+1, j<i and j+1 ~ i 这一段是一个palindrome```) (这里需要用另外一个数组来储存是否是palindrome))
* initialize: ```dp[0] = -1```
* answer: ```dp[len(s)]```

######[Word Break](./Leetcode/Word_Break.py)
* state: dp[i]表示前i个字符能否被完美切分
* function： ```dp[i] = or( dp[j], j<1 ,j+1 ~ i是一个字典中的单词)```
* initialize: ```dp[0] = True```
* answer: ```dp[len(s)]```

  注意j的枚举 -> 枚举单词长度
  O(NL) N: 字符串长度  L:最长单词的长度


######[Longest Increasing Subsequence 最长上升子序列](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/) (Not in Leetcode)
* state: ~~dp[i] 表示前i个数字中最长的LIS长度(错误)~~
       dp[i] 表示第i个数字结尾的LIS长度(正确)
* function: ```dp[i] = max(dp[j]+1, j<i and a[j] <= a[i])```
* initialize: ```f[0..n-1] = 1```
* answer: ```max(f[0..n-1])```
任何一个位置都可能为开始, 所以所有都要初始化为1, 因为最少LIS是1

-----

####3. Two Sequences DP 40%
* state: dp[i][j] 代表了第一个sequence的前i个数字/字符配上第二个的sequence的前j个...
* function: dp[i][j] = 研究第i个和第j个的匹配关系
* initialize: dp[i][0] and dp[0][j]
* answer: dp[len(s1)][len(s2)]

######[Longest Common Subsequence](http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/)
* state: dp[i][j]表示前i个字符配上前j个字符的LCS的长度
* function: 
```
dp[i][j] = dp[i-1][j-1]              # if a[i]  = b[j]
         = max(dp[i][j-1],dp[i-1][j] # if a[i] != b[j]
```
* initialize: ```dp[i][0] = 0```
              ```dp[0][j] = 0```
* answer: ```dp[len(a)][len(b)]```

######[Longest Common Substring](http://www.geeksforgeeks.org/longest-common-substring/) (Not in Leetcode)
* state: dp[i][j]表示前i个字符配上前j个字符的LCS的长度(一定以第i个和第j个结尾的LCS)
* function: 
```
dp[i][j] = dp[i-1][j-1] + 1 # a[i] == b[j]
         = 0                # a[i] != b[j]
```
* initialize: ```dp[i][j] = 0
                 dp[0][j] = 0```
* answer: ```max(dp[0...len(a)][0...len(b)])

######[Edit Distance](./Leetcode/Edit_Distance.py)
* state: dp[i][j] a的前i个字符配上b的前j个字符最少要用几次编辑使得他们相等
* function: 
```
dp[i][j] = dp[i-1][j-1]                                    # a[i] == b[j]
         = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1)  # a[i] != b[j]
```
* initialize: ```dp[i][0] = i, dp[0][j] = j```
* answer: ```dp[len(a)][len(b)]

######[Distinct Subsequence](./Leetcode/Distinct_Subsequences.py)
To be continued

######[Interleaving String](./Leetcode/Interleaving_String.py)
To be continued

-----

####4. Interval DP
* state: dp[i][j] 代表从i到j这一段区间...
* function: dp[i][j] = max/min/sum(dp[i][k], dp[k+1][j])
* initialize: dp[i][i] = ?
* answer: dp[1][n]

######[Merge Stone 石子归并](http://wikioi.com/problem/1048/)

重点必须把握__LIS__, __LCS__

-----

####5. Tree DP
######Binary Tree Maximum Path Sum

-----

####6. States Compressing DP(不需要知道)
####7. Knapsack

-----
####复杂度
* 一个变量 O(n)
* 两个变量 O(n^2)

-----

#### Two Pointer
The basic template of doing 'Sums'
* [x] Two Sum
* [x] 3Sum
* [x] 3Sum Closest
* [x] 4Sum

####Cannot Classify(记住思路)
* [x] Search Insert Position
* [x] Container With Most Water (In Two pointers)
* [x] Count and Say
* [x] Implement strStr() (KMP)


##Definetly Redo
* Recover_Binary_Search_Tree
* Validate_Binary_Search_Tree
* Order Traversal Recover
* __Find last ancestor__ of node x
* Rotate List
* Trapping Water (especially the way to think)
* 3Sum closest
* Sqrt(x)
* Pow(x,n)
* Longest Substring Without Repeating Characters
* Largest Rectangle in Histogram (The O(n) way is the hardest one I've ever seen)
* Maximal Rectangle (Same to above)

##### Below Two Looks Similar, seems all use DFS
* Palindrome Partitioning
* Binary Tree Maximum Path Sum

Not good, seems I need to redo every questions AC rate below 25%

##Still Cannot Understand
* Edit Distance
* Distinct Subsequences(I'm too bad at DP, need to find out a way to understand these)


##From Class
###Binary Search
* Find First Occurance in Sorted Array (Basic)
* Find Last Occurance in Sorted Array
* Search Insert Position (Same as search for kth big)
* Search for a Range (My way is wrong, should use binary for both bounds)
* Search in Rotated Sorted Array
* Search in Rotated Sorted Array II
* Search a 2D Matrix
* Search a 2D Matrix II (prev[-1] may larger than cur[0])
* [x] Median of Two Sorted Arrays (Need to look back for annie's answer, she has three solutions)
* -> Find kth in two Sorted Arrays

######From zz
* [x] Divide Two Integers (This is not binary search since not allowed to use multiply. Bit calculation)
* Pow(x, n)
* Sqrt(x)

####Three steps reverse
* Recover Rotated Array
* -> Recover Rotated String
* -> Rotate String
* -> Reverse Sentence

```python
def binary_search(target, A):
    if len(A) == 0:
        return -1
    start = 0
    end = len(A) - 1
    while start + 1 < end:
        mid = start + (end - start) / 2    # Avoid stack overflow
        if A[mid] == target:
            end = mid
        elif A[mid] > target:
            start = mid
        else:
            end = mid
    # Check start and end
    if A[start] == target:
        return start
    if A[end] == target:
        return end
    return -1
```

###Divide & Conquer (Most BT Problem)
* Merge Sort
* Quick Sort
* Tree Traverse
* Maximum Depth of Binary Tree
* Balanced Binary Tree
* Binary Tree Maximum Path Sum

This will require extra space

把一个任务划分成几个小任务
一般来说分治是有return的，但是Recursion一般是没有的

Binary Tree Level Order Traversal 3 ways
* 2 Queues
* 1 Queue + dummy node
* 1 Queue 双重循环 (Best)

Check BFS and DFS template

####Not in Leetcode
* Print BST Keys in Give Range
* __Implement Iterator of BST__
* Insert a Node in a Binary Search Tree
* Delete a Node in a Binary Search Tree
* Least Common Ancestor
这个和CC150不太一样, 是从底走, NC答案是Divide an Conquer, CC150是recursion
* (tarjan算法)

###DFS
主要想法是先搜索到不能再底层然后再往上走
#####复杂度问题
* 组合的话就是O(n^2)
* 排列的话就是(n!)


* [Permutations](./Leetcode/Permutations.py)
尝试把DFS的

* [Subsets](./Leetcode/Subsets.py)
* [N Queens](./Leetcode/N-Queens.py)
* [Palindrome Partitioning](./Leetcode/Palindrome_Partitioning.py)
* [Combinations Sum](./Leetcode/Combination_Sum.py)
* [Word Ladder](./Leetcode/Word_Ladder.py)
  __无向图求最短路径用BFS, 用Level Order搜索法__
  注意, 因为是单词, 所以做搜索的时候是按字母变化来



#####[Word Ladder II](./Leetcode/Word_Ladder_II.py)
1. 最短的是什么
2. 所有最短的是啥

1. 对所有点进行分层BFS
2. 对DFS层进行搜索

###Graph
* 图上的BFS需要用HashTable去重

#####[Clone Graph](./Leetcode/Clone_Graph.py)

#####[拓扑排序Topological sorting](http://www.geeksforgeeks.org/topological-sorting/)
主要是入度为零
```
Q.offer(....)
while (!Q.empty()) {
    Node head = Q.poll();
    for (int i = 0; i < head.neighbors.size(); i++) {
        inDegree[neighbor] --;
        if ( .. == 0) {
            Q.offer(.xxx)
        }
    }
}
```

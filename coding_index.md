## Coding Summary by Keywords and Type

###Permutation & Combination Type
* [x] Permutations
* [x] Permutations II
* [x] Permutation Sequence
* [x] Next Permutation

-----

* [x] Combinations
* [x] Combination Sum
* [x] Combination Sum II
* [x] Letter Combination of a Phone Number
* [x] 找零钱 == Combination Sum I

-----

* [x] Subset
* [x] Subset II

-----

#####总结
[Permutations](./Leetcode/Permutations.py) [II](./Leetcode/Permutations_II.py),
[Combinations](./Leetcode/Combinations.py),
[Combinations Sum](./Leetcode/Combination_Sum.py) [II](./Leetcode/Combination_Sum_II.py)
和[Subset](./Leetcode/Subsets.py) [II](./Leetcode/Subsets_II.py)都是DFS， 区别在于:

1. 将```res```放入```ret```的条件不一样  
   * Permu - ```len(res) = len(S)```
   * Combin - ```len(res) == k```
   * Combin Sum - ```target == 0```
   * Subsets - 只要生成新的res就要存一次  
   前三种题存过结果只后程序应该return

2. 循环内call recursion时的输入变量不一样  
   * Permu - ```permu_helper(num[:i] + num[i+i:], res, ret)```(除了S[i])
   * Combin - ```comb_helper(i+1, n, k, res, ret)```(S[i+1:])
   * Combin Sum - ```comb_sum_helper(num[i:], target - n, res, ret)```(S[i:])
   * Subsets - ```sub_helper(S[i+1:], res, ret)```(S[i+1:])  
   S[i+1:]决定了res内是不会有重复项的(除非S本身就有重复), S[i:]让当前元素可以重复使用
   
######Note
* II类去重题相比较I类题唯一的差别就是在循环的第一行需要check```if i > 0 and S[i] == S[i-1]: continue```
* 注意II类题都需要先```sort```, 因为去重是判断前项相等否
* 普通题目看情况如果要求输入时```res```内的元素有序那也需要```sort```
* Comb Sum题有一点点特殊在于在循环内需要判断```target - num < 0: continue```
* Comb Sum II和I比题目有点点变化在于，数字不能无限重取，只能有限重取,  
  所以是```comb_sum_II_helper(num[i+1:], target - n, res, ret)```
* 记得尽量用```enumerate```

复杂度O(n)??

-----

* [x] Gray Code

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
* [ ] Binary Tree Inorder Traversal
* [ ] Binary Tree Preorder Traversal
* [ ] Binary Tree Postorder Traversal
* [x] Binary Tree Level Order Traversal
* [x] Binary Tree Level Order Traversal II
* [x] Binary Tree Zigzag Level Order Traversal

_____

* [x] Construct Binary Tree from Preorder and Inorder Traversal
* [x] Construct Binary Tree from Inorder and Postorder Traversal

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
* [ ] Populating Next Right Pointers in Each Node
* [ ] Populating Next Right Pointers in Each Node II
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
* [ ] Insertion Sort List (Insertion Sort)
* [x] Copy List with Random Pointer
* [x] Merge k Sorted Lists
* [x] Rotate List
* [ ] Sort List (Merge Sort)
* [x] Reorder List
* [x] Reverse Nodes in k-Group

######Dup with tree
* [ ] Flatten Binary Tree to Linked List
* [ ] Convert Sorted List to Binary Search Tree

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
* [x] Unique Paths
* [x] Unique Paths II
* [x] Minimum Path Sum
* [x] Triangle

-----
* [x] Climbing Stairs
* [x] Jump Game
* [x] Jump Game II
* [x] Palindrome Partitioning II
* [x] Word Break
* [x] Decode Ways
* [x] Maximum Subarray(勉强)
* [x] LIS
* [x] Longest Palindrome Substring(上课题没用)

-----

* [x] LCS * 2
* [x] Edit Distance
* [x] Distinct Subsequences
* [x] Interleaving String

-----

* [x] Container With Most Water
* [x] Unique Binary Search Trees
* [x] Unique Binary Search Trees II
* [x] Best Time to Buy and Sell Stock III
* [x] Maximal Rectangle (DP isn't the best way)
* [x] Scramble String (别用)

-----

##From NC DP Class

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

####1. Matrix DP 20% (Triangle, Unique Path, ...)
* state: ```dp[x][y]```表示从起点走到坐标 (x,y) 的xxx
* function: 研究下一步怎么走
* initialize: 起点
* answer: 终点
* 复杂度一般为O(n^2)

#####[Triangle](./Leetcode/Triangle.py)
* status: ```dp[x][y]```表示从bottom走到top每个坐标的最短路径
* function: ```dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]```
* initialize: ```dp[-1][j] = triangle[-1][j]```
* answer: ```dp[0][0]``` (比较奇怪，因为是由下至上)

#####[Unique Path](./Leetcode/Unique_Paths.py) | [Unique Path II](./Leetcode/Unique_Paths_II.py)
* state: ```dp[x][y]```表示从起点走到 (x,y) 的path数
* function: ```dp[x][y] = dp[x-1][y] + dp[x][y-1]``` | ```if 障碍, dp[x][y] = 0```
* initialize: ```dp[0][y] = 1, dp[x][0] = 1```
* answer: ```dp[M-1][N-1]```

#####[Minimum Path Sum](./Leetcode/Minimum_Path_Sum.py)
* state: ```dp[x][y]```表示从起点走到x,y的minimum path sum
* function: ```dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x][y]```
* initialize: ```dp[0][0] = grid[0][0], dp[x][0] = dp[x-1][0] + grid[x][0], dp[0][y] = dp[0][y-1] + grid[0][y]```
* answer: ```dp[M-1][N-1]```

-----

####2. One Sequence DP 40%
* state: ```dp[i]```表示前i个位置/数字/字母，以第i个为...
* function: ```dp[i] = dp[j] ...j``` 是i之前的一个位置
* initialize: ```dp[0] = ...```
* answer: ```dp[N-1]```
* 复杂度一般为O(n^2)

######[Climbing Stairs](./Leetcode/Climbing_Stairs.py)
* state: ```dp[i]```表示爬到前i个台阶时的方法数
* function: ```dp[i] = dp[i-1] + dp[i-2]```
* initialize: ```dp[0] = 1, dp[1] = 2```
* answer: ```dp[N-1]```

######[Jump Game](./Leetcode/Jump_Game.py) | [Jump Game II](./Leetcode/Jump_Game_II.py)
* state: ```dp[i]```表示能否跳到第i个位置O(n^2) (还有一种O(n)的dp, 见方法2) | dp[i]表示跳到这个位置最少需要多少步.
* function: ```dp[i] = for j in (i-1 ... 0) if dp[j] and j能跳到i)``` | ```min(dp[j] + 1, j < i and j能跳到i)```
* initialize: ```dp[0] = True``` | ```dp[0] = 0```
* answer: ```dp[N-1]```

######[Palindrome Partitioning II](./Leetcode/Palindrome_Partitioning_II.py)
* state: ```dp[i]```表示前i-1个字符组成的字符串需要最少几次cut
* function: ```dp[i] = min( dp[j]+1, j<i and j+1 ~ i 这一段是一个palindrome```) (这里需要用另外一个数组来储存是否是palindrome))
* initialize: ```dp[0] = N-1```最少N-1次cut就行了
* answer: ```dp[N]-1```(这里有些不一样，主要原因是)

######[Word Break](./Leetcode/Word_Break.py)
* state: ```dp[i]```表示前i-1个字符能否被完美切分
* function： ```dp[i] = for j in (i-1 ... 0) if dp[j] and j ~ i是一个字典中的单词)```
* initialize: ```dp[0] = True```
* answer: ```dp[N]``` (这里也是比较特殊，因为是i-1个字符，不能从0算起)

  注意j的枚举 -> 枚举单词长度
  O(NL) N: 字符串长度  L:最长单词的长度

######[Longest Increasing Subsequence 最长上升子序列](./Interviews/Longest_Increasing_Subsequence.py) [(Not in Leetcode)](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)
* state: ~~```dp[i]```表示前i个数字中最长的LIS长度(错误)~~ ```dp[i]```表示第i个数字结尾的LIS长度(正确)
* function: ```dp[i] = max(dp[j]+1, j<i and a[j] <= a[i])```
* initialize: ```dp[0..n-1] = 1```
* answer: ```max(dp[0..n-1])```
任何一个位置都可能为开始, 所以所有都要初始化为1, 因为最少LIS是1

######[Decode Ways](./Leetcode/Decode_Ways.py)
* state: ```dp[i]```表示前i-1个数字的DW
* function:  

  ```python
  dp[i]   = 0        # if A[i] == 0 and A[i-1] not in [1,2]
         += dp[i-1]  # if A[i] != 0
         += dp[i-2]  # if 10 <= int(A[i-2:i]) <= 26
  ```
* initialize: ```dp[0] = 1```
* answer: ```dp[N]``` (这里比较特殊，因为是前i-1个数字，且dp[0]只是作为一个起始数字来的)

-----

####3. Two Sequences DP 40%
* state: ```dp[i][j]```代表了第一个sequence的前i个数字/字符配上第二个的sequence的前j个...
* function: ```dp[i][j] =``` 研究第i-1个和第j-1个的匹配关系
* initialize: ```dp[i][0], dp[0][j]```
* answer: ```dp[len(s1)][len(s2)]```
* 复杂度一般为O(m*n)

######[Longest Common Subsequence](./Interviews/Longest_Common_Subsequence.py) [(Not in Leetcode)](http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/)
* state: ```dp[i][j]```表示前i个字符配上前j个字符的LCS的长度
* function:  

  ```python
  dp[i][j] = dp[i-1][j-1] + 1           # if a[i-1] == b[j-1]
           = max(dp[i][j-1],dp[i-1][j]) # if a[i-1] != b[j-1]
  ```
* initialize: ```dp[i][0] = 0, dp[0][j] = 0```
* answer: ```dp[M][N]```

######[Longest Common Substring](./Interviews/Longest_Common_Substring.py) [(Not in Leetcode)](http://www.geeksforgeeks.org/longest-common-substring/)
* state: ```dp[i][j]```表示前i个字符配上前j个字符的LCS的长度(一定以第i个和第j个结尾的LCS)
* function:  

  ```python
  dp[i][j] = dp[i-1][j-1] + 1 # if a[i-1] == b[j-1]
           = 0                # if a[i-1] != b[j-1]
  ```
* initialize: ```dp[i][j] = 0, dp[0][j] = 0```
* answer: ```max(dp[0...len(a)][0...len(b)])```

######[Edit Distance](./Leetcode/Edit_Distance.py)
* state: dp[i][j] a的前i个字符配上b的前j个字符最少要用几次编辑使得他们相等
* function:  

  ```python
  dp[i][j] = dp[i-1][j-1]                                    # if a[i] == b[j]
           = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])) + 1  # if a[i] != b[j]
  ```
* initialize: ```dp[i][0] = i, dp[0][j] = j```
* answer: ```dp[M][N]```

######[Distinct Subsequence](./Leetcode/Distinct_Subsequences.py)(需要再领会一下)
* state: ```dp[i][j]```表示T的前i个字符和S的前j个字符的DS个数
* function:  

  ```python
  dp[i][j] = dp[i][j-1] + dp[i-1][j-1] # if T[i-1] == S[j-1]
           = dp[i][j-1]                # if T[i-1] != S[j-1]
  ```
* initialize: ```dp[i][0] = 0, dp[0][j] = 1```
* answer: ```dp[M][N]```

  大概意思就是， 因为算的是S的子串和T匹配的方法， 所以一旦S[:j-1]和T[:i]有x种匹配方法时  
  S[:j]必定也至少和T[:i]有x种匹配方法，但尤其当S[j-1]==T[i-1]的时候，需要再加上S[:j-1]和T[:i-1]的匹配方法数  
  注意分清M,i和N,j对应T和S，这个很特殊因为必须是S的子串和T相同

######[Interleaving String](./Leetcode/Interleaving_String.py)
* state: ```dp[i][j]```表示s1的前i个字符配上s2的前j个字符在s3的前i+j个字符是不是IS
* function:  

  ```python
  dp[i][j] = True  # if dp[i-1][j] and s1[i-1] == s3[i-1+j]
           = True  # if dp[i][j-1] and s2[j-1] == s3[i+j-1]
           = False # else
  ```
* initialize: ```dp[0][0] = True```
* answer: ```dp[M][N]```

-----

####4. Interval DP
* state: ```dp[i][j]``` 代表从i到j这一段区间...
* function: ```dp[i][j] = max/min/sum(dp[i][k], dp[k+1][j])```
* initialize: ```dp[i][i] = ?```
* answer: ```dp[1][n]```

######[Merge Stone 石子归并](http://wikioi.com/problem/1048/)

-----

####5. Tree DP
######Binary Tree Maximum Path Sum

-----

####6. States Compressing DP(不需要知道)
####7. Knapsack


###总结

####复杂度
直接看循环嵌套层数

####关于取dp[N]还是dp[N-1]还有dp[N]-1
1. 首先先分析dp维度，Matrix和Two Sequence dp都是二维，One Sequence是一维
2. Matrix dp一般都是初始(0,0)跳到(M-1,N-1)所以取的是```dp[M-1][N-1]```
3. 如果dp[i]或者dp[i][j]表示前i个什么的时候，需要以N/MN作为结尾，主要原因是这种情况下前0个字符串是没有意义的，至少从1开始，所以取dp的时候也是从dp[1]开始才有意义，所以dp[i]的含义是前i-1个东西的性质，而```dp[0] or dp[0][0]```需要强制赋值
4. 至于dp[N] - 1纯粹是因为Palindrome题目比较特殊，实际我们算的cut-1才是结果

####已知dp问题然后回问满足dp条件的结果
一般这种情况就是根据已知的dp matrix和结论，从最后开始往前回溯，满足的就挑进去，不满足的就不放来解决.

-----

#### Array Two Pointers
The basic template of doing 'Sums'
* [x] Two Sum
* [x] 3Sum
* [x] 3Sum Closest
* [x] 4Sum

* [x] Trapping Water (especially the way to think)
* [x] Container With Most Water
* [x] Stock 系列
* [x] Candy


####Cannot Classify(记住思路)
* [x] Search Insert Position
* [x] Container With Most Water (In Two pointers)
* [x] Count and Say
* [x] Candy

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

###DFS vs BFS
#####DFS - O(2^n), O(n!)
1. Find all solutions
2. Permutations / Subsets

#####BFS - O(m) O(n)
1. Graph Traversal(每个点都遍历一次)
2. Find shorted path in a simple graph

-----

###Data Structure

####Stack implement
* [Min Stack](./Interview/Min_Stack.py)
* [Queue by Two Stacks](./Interview/Queue_by_Two_Stacks.py)
* Mid Stack
* Sort Stack

####Heap
#####Median Number(应该是CC150)里的题
* 要求插入一个数
* 要求return median number


####Interval Tree(线段树)

-----

####增加一个jumble的算法，跟permutation和combination还有subset一起做简算。

-----

#####XOR ( 不进位加法 )

#####Majority Number
__去想关于数据结构的题目的时候, 只需要考虑数据结构里处理的次数就行了__

#####99%的数据处理

-----

##System Design

* Concurrency
   * Thread
   * Deadlock
   * Sync vs Async
     同步: blocking
     异步：callback，
     AJAX，Asynchronized IO
     Websever: nginx Linux epoll内核级别的轮训, single process 比thread pool更加高效 context switch需要很多开销
* Network
  * Http 协议属于applicatin，1.1版本，1.0区别：
    1. host ，实现虚拟主机
    2. 长链接
    3. chunk传输
  * 访问google
    __Client Side__
    1. DNS: 把domain name转化成ip address, use cache
    2. HTTP: 80, GET/POST, request header, response header, content-length, accept type, etag, cookie-session
    3. 7 layer, 封包 解包 过程，tcp 3次握手协议
    4. rendering. html  
    __Server Side__
    GET /index.jsp?username=xxx, cookie (client端叫cookie, server端叫session)
    static, dynamic区分
    cdn(content delivery network)：
    jsp, aspx, php: cgi, template + data => html
* Abstraction, OOP
  1. Elevator  
     调度算法：先来先到，或者最短路径，轮训，基于人群多少计算cost
  2. Book library  
     static resource, class, action->method, db table, schema, order table, 数据库设计范式 norm
  3. News Feed  
     poll, push model  
     last visit time  
     cache: hot/cold  
     count limit: 100
  4. Amazon  
     product, customer, shopping cart, order  
     partition: veritcal, horizontal  
     consistent hashing
  5. Game  
     init game  
     game start, record status, feedback  
     end game, success/fail

* Distributed System (Avoid single failure point) Majority Win
  * Consistency, eventually consistent, Amazon DynamicDB
  * Availability(尽量选)
  * Partition tolerance(尽量选)  
    2PC  
    Gossip  
    Paxos  
    解决办法:  
    1. 时间戳
    2. 你来选
* Performance

* Estimation(估算)  
  1PB = 2^10 TB = 2^20 GB .. = 2^50 B (bype)  
  1 integer = 4 bytes
* Big Data  
  1. 大数据算法
  http://www.icourse163.org/learn/hit-10001
  2. TinyURL:  
     1. orig url: http://collabedit.com/nt4qp  
        tiny url: http://t.cn/12345  
        tinyUrl->origUrl  
        origUrl->tinyUrl  
        2 memory tables, db table  
        1. md5(origUrl) -> abced  
           a-zA-Z0-9 64 differ chars  
           num%64;  
        2. auto increase key  
           id++ -> 64 chars
     2. Cache  
        LRU, LFU, frequent from logs
     3. Load blance:  
        qps: 1000, router: round robin  
        storage: consistant hashing: http://www.programering.com/a/MzN2MjMwATI.html  
     4. Locale: router

##Definetly Redo
* [ ] Regular Expression Matching
* [ ] Wildcard Matching
* [ ] Max Points on a Line
* [ ] Word Ladder II
* [ ] Word Break II
* [ ] Text Justification
* [ ] String to Integer (atoi)
* [ ] Substring with Concatenation of All Words
* [ ] Minimum Window Substring
* [ ] Sum系列
* [ ] Longest Valid Parentheses
* [ ] Word Search (简单)
* [ ] Simplify Path
* [ ] Restore IP Addresses
* [ ] Insert Interval
* [ ] Implement strStr() (KMP再写一遍)
* [ ] Count and Say (Linkedin面经)

* [x] Rotate List
* [x] Longest Substring Without Repeating Characters


* [x] Maximum Path Sum(BT)

* [x] decode ways
* [x] Longest Palindrome Substring

* [ ] Next Permutation

* [x] Rotate Image
* [x] Spiral Matrix * 2
* [ ] Gray Code

* [x] LRU
* [x] Surrounded Regions
* [x] Gas Station
* [ ] Permutation Sequence
* [ ] Next Permutation
* [ ] Maximum Subwindow
* [x] Max Product of Subarray
* [ ] First Missing Positive

* [ ] 还有前面tree的一些
* [x] Validate Binary Search Tree (Redo)
* [x] Recover Binary Search Tree (Redo)
* [ ] Populating Next Right Pointers in Each Node
* [ ] Populating Next Right Pointers in Each Node II
* [ ] Construct Binary Tree from Inorder and Postorder Traversal
* [ ] Construct Binary Tree from Preorder and Inorder Traversal
* [ ] Recover Binary Search Tree
* [ ] Validate Binary Search Tree
* [ ] Order Traversal Recover
* [ ] BFS every traversal
* [ ] Flatten BST to doubly linkedlist
* [ ] Flatten BST to Linked List

* [x] Median of Two Sorted Arrays

* [x] Trapping Water (especially the way to think)
* [x] Container With Most Water
* [x] Stock 系列
* [x] Candy

##Need Understand
* [ ] Largest Rectangle in Histogram
* [ ] Maximal Rectangle
* [x] Divde two integers
* [x] Single Number II


##New
* [x] [Absolut Minimum](./Interviews/Absolute_Minimum.py)


##Some Note
1. 一定要看清题，比如这次就被问了find all palindrome，但是理解成palindrome partitioning了，所以错了
2. 再仔细确认下怎么算recursion的big O

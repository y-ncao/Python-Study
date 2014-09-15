##[1. 3Sum](https://oj.leetcode.com/problems/3sum/)

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

```python

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num = sorted(num)
        N = len(num)
        ret = []
        for i in range(N-2):
            if i > 0 and num[i] == num[i-1]:
                continue
            l = i + 1
            r = N - 1
            while l < r:
                if num[i] + num[l] + num[r] < 0:
                    l += 1
                elif num[i] + num[l] + num[r] > 0:
                    r -= 1
                else:
                    ret.append([num[i], num[l], num[r]])
                    l += 1
                    r -= 1
                    while l < r and num[l] == num[l-1]:
                        l += 1
                    while l < r and num[r] == num[r+1]:
                        r -= 1
        return ret

    # Notice:
    # 1. This is almost the same to 3 Sum Closest.
    # 2. remember to remove duplicate result by doing l += 1 and r -= 1, also the continue on line 22
```
-----

##[2. 3Sum Closest](https://oj.leetcode.com/problems/3sum-closest/)

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

```python

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        return self.threeSumClosest_1(num, target)

    # Since it assume each input only have one result, there's no need to check dup
    def threeSumClosest_1(self, num, target):
        N = len(num)
        num = sorted(num)
        ret = num[0]+num[1]+num[2]
        i = 0
        for i in range(N-2):
            l = i + 1
            r = N - 1
            while l < r:
                threesum = num[i] + num[l] + num[r]
                if abs(threesum-target) < abs(ret-target): # Need to check this before changing threesum
                    ret = threesum
                if threesum == target:
                    return target
                elif threesum < target:
                    l += 1
                else:
                    r -= 1
        return ret

    # time exceeded
    def threeSumClosest_2(self, num, target):
        N = len(num)
        if N < 3:
            return 0
        closest_sum = num[0]+num[1]+num[2]
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    sum = num[i] + num[j] + num[k]
                    if sum == target:
                        return target
                    elif abs(target-sum) < abs(closest_sum):
                        closest_sum = sum
        return closest_sum
```
-----

##[3. 4Sum](https://oj.leetcode.com/problems/4sum/)

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

```python

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        return self.fourSum_1(num, target)

    # This is kitt's way, using dictionary
    def fourSum_1(self, num, target):
        N = len(num)
        if N < 4:
            return []
        num.sort()
        res = set()
        d = {}
        # Convert 4Sum to 2Sum, store every i+j result
        for i in range(N):
            for j in range(i + 1, N):
                if num[i] + num[j] not in d:
                    d[ num[i] + num[j] ] = [(i,j)]
                else:
                    d[ num[i] + num[j] ].append( (i,j) )
        # Solve 2Sum
        for i in range(N):
            for j in range(i + 1, N - 2):
                T = target - num[i] - num[j]
                if T in d:
                    for k in d[T]:
                        if k[0] > j: res.add( ( num[i], num[j], num[k[0]], num[k[1]] ) )
        return [ list(i) for i in res ]

    # Won't pass because this is O(n^3)
    def fourSum_2(self, num, target):
        num.sort()
        N = len(num)
        ret = []
        for i in range(N-3):
            if i > 0 and num[i] == num[i-1]:
                continue
            for j in range(i+1, N-2):
                if j > i+1 and num[j] == num[j-1]:
                    continue
                l = j + 1
                r = N - 1
                while l < r:
                    sum = num[i] + num[j] + num[l] + num[r] < target
                    if sum < target:
                        l += 1
                    elif sum > target:
                        r -= 1
                    else:
                        ret.append([num[i], num[j], num[l], num[r]])
                        l += 1
                        r -= 1
                        while l < r and num[l] == num[l-1]:
                            l += 1
                        while l < r and num[r] == num[r+1]:
                            r -= 1
        return ret
```
-----

##[4. Add Binary](https://oj.leetcode.com/problems/add-binary/)

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

```python

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        A = len(a)
        B = len(b)
        res = []
        carry = 0
        i = 1
        while i <= max(A,B):            # using sum at first, then add bit if exist, this is good
            sum = carry
            if i <= A:
                sum += int(a[-i])
            if i <= B:
                sum += int(b[-i])
            bit = sum % 2
            carry = sum / 2
            i += 1
            res.insert(0, str(bit))
        if carry > 0:
            res.insert(0, '1')
        return ''.join(res)
    # Nothing would be better than this
```
-----

##[5. Add Two Numbers](https://oj.leetcode.com/problems/add-two-numbers/)

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        carry = 0
        cur = dummy
        while l1 is not None or l2 is not None or carry > 0:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            cur.next = ListNode(sum % 10)
            carry = sum / 10
            cur = cur.next
        return dummy.next
```
-----

##[6. Anagrams](https://oj.leetcode.com/problems/anagrams/)

Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.

```python

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            d.setdefault(key,[]).append(s)
        ret = []
        for key in d:
            if len(d[key]) > 1:
                ret.extend(d[key])
        return ret
    # Note:
    # 1. Need to use extend here, return those len(d[key]) > 1
    # 2. Need to remember the definition of Anagrams
    
    Input:      ["tea","and","ate","eat","dan"]
    Output:     ["and","dan"]
    Expected:   ["and","dan","tea","ate","eat"]
    
```
-----

##[7. Balanced Binary Tree](https://oj.leetcode.com/problems/balanced-binary-tree/)

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.isBalanced_1(root)

    def isBalanced_1(self, root):
        if root is None:
            return True
        if self.get_height(root) == -1:
            return False
        return True

    def get_height(self, root):
        if root is None:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def isBalanced_2(self, root):
        if root is None:
            return True
        if abs(self.get_max_height(root.left) - self.get_max_height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_max_height(self, root):
        if root is None:
            return 0
        return max(self.get_max_height(root.left), self.get_max_height(root.right)) + 1

    # First way is a little bit hard to think
    # Using -1 as return to sign if height diff > 1
    # First way has better performance
```
-----

##[8. Best Time to Buy and Sell Stock](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

```python

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        max_profit = 0
        low_price = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - low_price)
            low_price = min(low_price, price)
        return max_profit
```
-----

##[9. Best Time to Buy and Sell Stock II](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

```python

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                max_profit += prices[i] - prices[i-1]
        return max_profit
```
-----

##[10. Best Time to Buy and Sell Stock III](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

```python

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        N = len(prices)
        if N <= 1:
            return 0
        dp_1 = [0 for i in range(N)]
        dp_2 = [0 for i in range(N)]
        min_price = prices[0]
        i = 1
        while i < N:
            min_price = min(min_price, prices[i])
            dp_1[i] = max(dp_1[i-1], prices[i]-min_price)
            i+= 1

        max_price = prices[-1]
        i = N-2
        while i >= 0:
            max_price = max(max_price, prices[i])
            dp_2[i] = max(dp_2[i+1], max_price-prices[i])
            i -= 1
        res = 0
        for i in range(N):
            res = max(res, dp_1[i] + dp_2[i])
        return res
    # Very similart to trapping rain water, from left to right then right to left
```
-----

##[11. Binary Tree Inorder Traversal](https://oj.leetcode.com/problems/binary-tree-inorder-traversal/)

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
```
   1
    \
     2
    /
   3
```
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        return self.inorderTraversal_1(root)

    def inorderTraversal_1(self, root):
        stack = []
        current = root
        res = []
        while current is not None or len(stack) > 0:
            if current is not None:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                current = stack.pop()
                res.append(current.val)
                current = current.right
        return res

    def inorderTraversal_2(self, root):
        res = []
        self.inorderTraversal_rec(root, res)
        return res

    def inorderTraversal_rec(self, root, res):
        if root is None:
            return
        self.inorderTraversal_rec(root.left, res)
        res.append(root.val)
        self.inorderTraversal_rec(root.right, res)
```
-----

##[12. Binary Tree Level Order Traversal](https://oj.leetcode.com/problems/binary-tree-level-order-traversal/)

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
```
    3
   / \
  9  20
    /  \
   15   7
```
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        res = []
        if root is None:
            return res
        queue = [root, ]
        while len(queue)>0:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop()
                level.append(node.val)
                if node.left is not None:
                    queue.insert(0, node.left)
                if node.right is not None:
                    queue.insert(0, node.right)
            res.append(level[:])
        return res

    # Note
    # 1. Try to use double loop to do this
    # 2. Other ways are: a. use dummy node(None) b. use two queues
```
-----

##[13. Binary Tree Level Order Traversal II](https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/)

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
```
    3
   / \
  9  20
    /  \
   15   7
```
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        res = []
        if root is None:
            return res
        queue = []
        level = []
        queue.append(root)
        queue.append(None)
        while len(queue)>0:
            node = queue.pop(0)
            if node is None:
                res.append(level[:])
                level = []
                if len(queue)>0:
                    queue.append(None)
            else:
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return res[::-1]
```
-----

##[14. Binary Tree Maximum Path Sum](https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/)

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

```
       1
      / \
     2   3
```
Return 6.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        max_sum = [-9223372036854775808]
        self.maxPathSum_helper(root, max_sum)
        return max_sum[0]

    def maxPathSum_helper(self, root, max_sum):
        if root is None:
            return 0

        left = self.maxPathSum_helper(root.left, max_sum)
        right = self.maxPathSum_helper(root.right, max_sum)

        root_max = max(root.val, max(left, right)+root.val)
        max_sum[0] = max(max_sum[0], root_max, left+right+root.val)

        return root_max
    # Almost there
```
-----

##[15. Binary Tree Postorder Traversal](https://oj.leetcode.com/problems/binary-tree-postorder-traversal/)

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
```
   1
    \
     2
    /
   3
```
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        return self.postorderTraversal_1(root)

    # I prefer this way
    def postorderTraversal_1(self, root):
        if root is None:
            return []
        stack = [root]
        output = []
        while len(stack)>0:
            node = stack.pop()
            output.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return output[::-1]

    # I don't like this way
    def postorderTraversal_2(self, root):
        stack = []
        current = root
        res = []
        last = None
        while current is not None or len(stack)>0:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                peak = stack[-1]
                if peak.right is not None and last != peak.right:
                    current = peak.right
                else:
                    last = stack.pop()
                    res.append(last.val)
        return res

    def postorderTraversal_3(self, root):
        res = []
        self.postorderTraversal_rec(root, res)
        return res

    def postorderTraversal_rec(self, root, res):
        if root is None:
            return
        self.postorderTraversal_rec(root.left, res)
        self.postorderTraversal_rec(root.right, res)
        res.append(root.val)
```
-----

##[16. Binary Tree Preorder Traversal](https://oj.leetcode.com/problems/binary-tree-preorder-traversal/)

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
```
   1
    \
     2
    /
   3
```
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        return self.preorderTraversal_1(root)

    def preorderTraversal_1(self, root):
        stack = []
        current = root
        res = []
        while current is not None or len(stack)>0:
            if current is not None:
                res.append(current.val)
                stack.append(current)
                current = current.left
            elif len(stack)>0:
                current = stack.pop()
                current = current.right
        return res

    def preorderTraversal_2(self, root):
        res = []
        self.preorderTraversal_rec(root, res)
        return res

    def preorderTraversal_rec(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.preorderTraversal_rec(root.left, res)
        self.preorderTraversal_rec(root.right, res)
```
-----

##[17. Binary Tree Zigzag Level Order Traversal](https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
```
    3
   / \
  9  20
    /  \
   15   7
```
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        ret = []
        if root is None:
            return ret
        queue = [root, None]
        res = []
        zig = False                     # Because we start from very root, so no reverse at that point
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                if zig:
                    ret.append(res[::-1])
                else:
                    ret.append(res[:])
                res = []
                if len(queue) == 0:     # Break here, otherwise will append another None
                    break
                zig = not zig
                queue.append(None)
            else:
                res.append(node.val)    # Remember this, need to do this in node, not node.left/right
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return ret
```
-----

##[18. Candy](https://oj.leetcode.com/problems/candy/)

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

```python

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        N = len(ratings)
        candy = [1 for i in range(N)]
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
        return sum(candy)
```
-----

##[19. Climbing Stairs](https://oj.leetcode.com/problems/climbing-stairs/)

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```python

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        return self.climbStairs_2(n)

    def climbStairs_1(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs_2(self, n):
        if n <= 1:
            return n
        dp = [ 0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

    # Note:
    # 1. dp[i] means from 0 to i-1 stair, how many ways to go
    # 2. dp[0] = 1, dp[1] = 2
    # 3. dp[i] = d[i-1] + dp[i-2]
    # 4. dp[N-1]

    def climbStairs_3(self, n):
        if n <= 2:
            return n
        fn_1 = 1
        fn_2 = 2
        for i in range(3, n+1):
            fn = fn_1 + fn_2
            fn_1 = fn
            fn_2 = fn_1
        return fn

    # Note:
    # DP way is the best, and no need to check if n <= 2 or not.
```
-----

##[20. Clone Graph](https://oj.leetcode.com/problems/clone-graph/)

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

```
       1
      / \
     /   \
    0 --- 2
         / \
         \_/

```
```python

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        # Use oldNode as the oldGraph, newNode as the newGraph. Use tuple (oldNode, newNode) to store relation
        newNodeHead = UndirectedGraphNode(node.label)
        queue = collections.deque()
        queue.append((node,newNodeHead))
        map_dict = {}
        while len(queue) > 0:
            (oldNode,newNode) = queue.popleft()
            if oldNode in map_dict:
                continue
            map_dict[oldNode] = 'Visited'
            newNode.neighbors = []
            for oldNeighbor in oldNode.neighbors:
                newNeighbor = UndirectedGraphNode(oldNeighbor.label)
                queue.append((oldNeighbor, newNeighbor))
                newNode.neighbors.append(newNeighbor)
        return newNodeHead

    # Another way to this is like Nine Chapter, no need to do like level order BFS
    # Finally add all neighbors
```
-----

##[21. Combination Sum](https://oj.leetcode.com/problems/combination-sum/)

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

```python

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        ret = []
        self.combinationSum_helper(sorted(candidates), target, [], ret) # Look into the question, need sorted
        return ret

    def combinationSum_helper(self, candidates, target, res, ret):
        if target == 0:
            ret.append(res[:])
            return
        for i, num in enumerate(candidates):
            if target >= num:
                res.append(num)
                self.combinationSum_helper(candidates[i:], target - num, res, ret)
                res.pop()

    # Improvements: only continue when target > num ,else stop
```
-----

##[22. Combination Sum II](https://oj.leetcode.com/problems/combination-sum-ii/)

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]

```python

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        ret = []
        self.combinationSum_helper(sorted(candidates), target, [], ret) # Look into the question, need sorted
        return ret

    def combinationSum_helper(self, candidates, target, res, ret):
        if target == 0:
            ret.append(res[:])
            return
        for i, num in enumerate(candidates):
            if target < num or ( i>0 and num == candidates[i-1] ):
                continue
            res.append(num)
            self.combinationSum_helper(candidates[i+1:], target - num, res, ret)
            res.pop()

    # Finally pass
    # Serveral improvements:
    # 1. if target < num, no need to continue
    # 2. Need to check dup candidates
```
-----

##[23. Combinations](https://oj.leetcode.com/problems/combinations/)

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

```python

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        ret =[]
        self.combine_helper(1, n, k, [], ret)
        return ret

    def combine_helper(self, cur, n, k, res, ret):
        if len(res) == k:
            ret.append(res[:])
            return
        for i in range(cur, n+1):
            res.append(i)
            self.combine_helper(i+1, n, k, res, ret)
            res.pop()
```
-----

##[24. Construct Binary Tree from Inorder and Postorder Traversal](https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder.pop())
        index = inorder.index(root.val)
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root
    # Only difference if pop(0) or pop()
    # In this case need to do right first
```
-----

##[25. Construct Binary Tree from Preorder and Inorder Traversal](https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder.pop(0))
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])
        return root
    # Too much detail, looks simple but hard to do
```
-----

##[26. Container With Most Water](https://oj.leetcode.com/problems/container-with-most-water/)

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

```python

class Solution:
    # @return an integer
    def maxArea(self, height):
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] <= height[r]:
                res = max(res, (r-l) * height[l])
                l += 1
            else:
                res = max(res, (r-l) * height[r])
                r -= 1
        return res

    # Two pointer problem
```
-----

##[27. Convert Sorted Array to Binary Search Tree](https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None
        return self.sortedArrayToBSTRec(num, 0, len(num)-1)

    def sortedArrayToBSTRec(self, num, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(num[mid])
        node.left = self.sortedArrayToBstRec(num, start, mid-1)
        node.right = self.sortedArrayToBstRec(num, mid+1, end)
        return node
```
-----

##[28. Convert Sorted List to Binary Search Tree](https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None:                # No need to check if head has only 1 or 2 nodes
            return None
        mid = head
        end = head
        prev = None
        while end.next is not None and end.next.next is not None:
            prev = mid                  # Very good way to keep record of last
            mid = mid.next
            end = end.next.next         # Doesn't matter what fast is, so no need to push to end
        if head == mid:
            head = None                 # This will ensure that we wouldn't create dup node to the left child
        if prev is not None:
            prev.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

    # Important thing here:
    # Actually we only care about the mid of the Node
    # Annie is using pre-order traversal way, which is different.
```
-----

##[29. Copy List with Random Pointer](https://oj.leetcode.com/problems/copy-list-with-random-pointer/)

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

```python

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        cur = head
        while cur is not None:
            newNode = RandomListNode(cur.label)
            newNode.next = cur.next
            cur.next = newNode
            cur = newNode.next
        cur = head
        while cur is not None:
            newNode = cur.next
            if cur.random is not None:  # random pointer may not exist
                newNode.random = cur.random.next
            cur = newNode.next
        cur = head
        newNodehead = head.next
        while cur is not None:
            newNode = cur.next
            cur.next = newNode.next
            if newNode.next is not None:
                newNode.next = newNode.next.next
            cur = cur.next
        return newNodehead
```
-----

##[30. Count and Say](https://oj.leetcode.com/problems/count-and-say/)

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

```python

class Solution:
    # @return a string
    def countAndSay(self, n):
        num = '1'
        while n > 1:
            prev = num[0]
            count = 1
            new_num = ''
            for bit in num[1:]:
                if bit == prev:
                    count += 1
                else:
                    new_num += str(count) + str(prev)
                    count = 1
                prev = bit
            new_num += str(count) + str(prev)
            num = new_num
            n -= 1
        return num
```
-----

##[31. Decode Ways](https://oj.leetcode.com/problems/decode-ways/)

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

```python

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        N = len(s)
        if N == 0 or s[0] == '0':
            return 0
        dp = [0 for i in range(N+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, N+1):
            if s[i-1] == '0' and s[i-2] not in ['1', '2']:
                return 0
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2: i]) <= 26:
                dp[i] += dp[i-2]
        return dp[N]

    # Note:
    # 1. State: dp[i] means from char 0 to char i-1 how many decode ways
    # 2. Init: dp[0] = 1; dp[1] = 1
    # 3. Function:
    #      dp[i] = if s[i-1] == 0 and s[i-2] not in ['1', '2'] : return 0
    #              if s[i-1] != 0                              : += dp[i-1]
    #              if 10 <= int(s[i-2:i]) <= 26                : += dp[i-2]
    # 4. Result: dp[N]

    # i.   dp size is len(s)+1
    # ii.  10 <= x <= 26
    # iii. use if += instead of if dp = xx else dp = xx

    # Another idea
    def numDecodings_2(self, s):
        if s == '' or s[0] == '0': return 0
        dp = [1, 1]
        length = len(s)
        for i in xrange(2, length + 1):
            if 10 <= int(s[i-2:i]) <= 26 and '1' <= s[i-1] <= '9':
                dp.append(dp[i-1] + dp[i-2])
            elif 10 <= int(s[i-2:i]) <= 26: # s[i-1] == '0'
                dp.append(dp[i-2])
            elif '1' <= s[i-1] <= '9':
                dp.append(dp[i-1])
            else:  # s[i] == '0'
                return 0
        return dp[length]
```
-----

##[32. Distinct Subsequences](https://oj.leetcode.com/problems/distinct-subsequences/)

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

Note:
The answer is three rabbit by removing the first, second, third 'b'

```python

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        M = len(T)
        N = len(S)
        dp = [ [0 for j in range(N+1)] for i in range(M+1)]
        for i in range(M+1):
            dp[i][0] = 0
        for j in range(N+1):
            dp[0][j] = 1
        for i in range(1, M+1):
            for j in range(1, N+1):
                if S[j-1] == T[i-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[M][N]
    # !!!!分清M,i和N,j分别对应T和S哪个
    # Note:
    # dp[i][j]表示S的前i个字符配上T的前j个字符的DS
    # [i][0] = 0, dp[0][j] = 1
    # dp[i][j] = dp[i][j-1] + dp[i-1][j-1] # if T[i-1] == S[j-1]
    #          = dp[i][j-1]                # if T[i-1] != S[j-1]
    # dp[M][N]
    # Need to draw this pic when solving this problem
    # 大概意思就是， 因为算的是S的子串和T匹配的方法， 所以一旦S[:j-1]和T[:i]有x种匹配方法时
    # S[:j]必定也至少和T[:i]有x种匹配方法，但尤其当S[j-1]==T[i-1]的时候，需要再加上S[:j-1]和T[:i-1]的匹配方法数
    #     r a b b b i t
    #   1 1 1 1 1 1 1 1
    # r 0 1 1 1 1 1 1 1
    # a 0 0 1 1 1 1 1 1
    # b 0 0 0 1 2 3 3 3
    # b 0 0 0 0 1 3 3 3
    # i 0 0 0 0 0 0 3 3
    # t 0 0 0 0 0 0 0 3
    # No matter T[i-1] ?= S[j-1],  dp[i][j] = dp[i][j-1]
    # But    if T[i-1] == S[j-1], we can add another one which is dp[i-1][j-1]
```
-----

##[33. Divide Two Integers](https://oj.leetcode.com/problems/divide-two-integers/)

Divide two integers without using multiplication, division and mod operator.

```python

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if ( dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend = abs(dividend)
        divisor  = abs(divisor)
        ret = 0
        while dividend >= divisor:
            k = 0
            tmp = divisor
            while dividend >= tmp:
                ret += 1 << k
                dividend -= tmp
                tmp <<= 1
                k += 1
        return ret * sign
```
-----

##[34. Edit Distance](https://oj.leetcode.com/problems/edit-distance/)

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

```python

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        M = len(word1)
        N = len(word2)
        dp = [ [ 0 for j in range(N+1)] for i in range(M+1)]
        for i in range(M+1):
            for j in range(N+1):
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min( dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[M][N]
    # Note:
    # 1. dp[i][j] is Edit Distance of first i-1 chars in word1 with first j-1 chars in word2
    # 2. dp[0][j] = j, dp[i][0] = i
    # 3. dp[i][j] = dp[i-1][j-1]                                   # if word[i-1] == word[j-1]
    #             = min( dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1 # if word[i-1] != word[j-1]

    # Note:
    # 1. This dp is a bit diff, the length of dp is A+1, B+1
    # 2. Others are the same, remember how to initiate the dp matrix
    # 3. When comparing the i, it compares with word[i-1] and word[j-1]
    #    This is not hard to think, since we start loop from 1
    # 4. Initial value of DP: add N chars for word1

    # Transfer function:
    # Target somestr1c -> somestr2d
    # 1. Assume somestr1  -> somestr2  dp[i][j]
    # 2.        somestr1  -> somestr2d dp[i-1][j]
    # 3.        somestr1c -> somestr2  dp[i][j-1]
    # 4. i.   replace c with d: somestr1  -> somestr2 + 1  :    dp[i-1][j-1] + 1
    #    ii.  append d to c   : somestr1c -> somestr2 + 1  :    dp[i][j-1] + 1
    #    iii. delete c        : somestr1  -> somestr2d + 1 :    dp[i-1][j] + 1
```
-----

##[35. Evaluate Reverse Polish Notation](https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/)

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

```python

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        operators = '+-*/'
        for i, token in enumerate(tokens):
            if token in operators:
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(self.calculate(num_1, num_2, token))
            else:
                stack.append(int(token))
        return stack[0]

    def calculate(self, num_1, num_2, token):
        if token == '+':\
            return num_1 + num_2
        if token == '-':
            return num_1 - num_2
        if token == '*':
            return num_1 * num_2
        if token == '/':
            return int(num_1 * 1.0 / num_2) # This is the trick part, need to notice
```
-----

##[36. First Missing Positive](https://oj.leetcode.com/problems/first-missing-positive/)

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

```python

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i < n:
            if A[i] != i+1 and A[i] >= 1 and A[i] <= n and A[A[i]-1] != A[i]: # The last check is important
                self.swap(A, i, A[i]-1)
            else:
                i += 1

        for i, num in enumerate(A):
            if num != i+1:              # The check here is also very important
                return i+1
        return n + 1

    def swap(self, A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    # Way to think
    # O(n) imply that we need to use hashtable
    # But it ask for constant space, so need to use the index as hashtable to store the num
```
-----

##[37. Flatten Binary Tree to Linked List](https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/)

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

```
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
```
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    last_node = None
    def flatten(self, root):
        if not root:
            return
        if self.last_node:
            self.last_node.left = None
            self.last_node.right = root
        self.last_node = root
        right = root.right              # Because root.right has changed
        self.flatten(root.left)
        self.flatten(right)
    # The above way is preferred
    # Notice line 48 need to store the state of right

    def flatten(self, root):
        if root is None:
            return None
        self.flatten_helper(root)

    def flatten_helper(self, root):
        if root.left is None and root.right is None:
            return root
        rhead = None                    # This declare is nessary
        if root.right is not None:
            rhead = self.flatten_helper(root.right)
        lend = root                     # Need this here
        if root.left is not None:
            lhead = self.flatten_helper(root.left)
            root.right = lhead
            lhead.left = None
            root.left = None
            while lend.right is not None: # Get the lend from root
                lend = lend.right

        if rhead is not None:
            lend.right = rhead
        return root

    # Non-recursion way
    def flatten(self, root):
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

    # Another diao zha way
    # This is the reverse way of above
    last = None
    def flatten(self, root):
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.last
            root.left = None
            self.last = root
```
-----

##[38. Gas Station](https://oj.leetcode.com/problems/gas-station/)

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

```python

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        N = len(gas)
        diff = []
        for i in range(N):
            diff.append(gas[i]-cost[i])
        sum = 0
        start_node = 0
        left_gas = 0
        for i in range(0, N):
            left_gas += diff[i]
            sum += diff[i]
            if sum < 0:
                start_node = i+1
                sum = 0
        if left_gas < 0:
            return -1
        else:
            return start_node
```
-----

##[39. Generate Parentheses](https://oj.leetcode.com/problems/generate-parentheses/)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

```python

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        ret = []
        self.generateParenthesis_helper(n, n, '', ret)
        return ret

    def generateParenthesis_helper(self, left, right, res, ret):
        if left == 0 and right ==0:
            ret.append(res[:])
            return
        if left > 0:
            self.generateParenthesis_helper(left-1, right, res+'(', ret)
        if right > left:
            self.generateParenthesis_helper(left, right-1, res+')', ret)
```
-----

##[40. Gray Code](https://oj.leetcode.com/problems/gray-code/)

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

```python

# Tip: you can use bin(x) to check the binary form of a num

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        ret = []
        i = 0
        while i < 2**n:
            ret.append(i>>1^i)
            i+=1
        return ret

# But these two won't pass because they return binary form string not the gray code in int

    def grayCodeGen(self, n, reverse=False):
        if n == 1:
            if reverse:
                yield "1"
                yield "0"
            else:
                yield "0"
                yield "1"
        else:
            if reverse:
                # all the "1"s start first
                gcprev = self.grayCodeGen(n-1, False)
                for code in gcprev:
                    yield "1" + code
                gcprev = self.grayCodeGen(n-1, True)
                for code in gcprev:
                    yield "0" + code
            else:
                # all the "0" start first
                gcprev = self.grayCodeGen(n-1, False)
                for code in gcprev:
                    yield "0" + code
                gcprev = self.grayCodeGen(n-1, True)
                for code in gcprev:
                    yield "1" + code

    # This is even better, no need to use iterator
    def grayCodeGen_2(n):
        if n == 1:
            return ['0', '1']
        else:
            ret = []
            code_list = grayCodeGen_2(n-1)
            for code in code_list:
                ret.append('0' + code)
            for code in code_list[::-1]:
                ret.append('1' + code)
        return ret

```
-----

##[41. Implement strStr](https://oj.leetcode.com/problems/implement-strstr/)

Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.

```python

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        return self.strStr_2(haystack, needle)

    def strStr_1(self, haystack, needle):
        M = len(haystack)
        N = len(needle)
        if N == 0:
            return haystack             # Note here
        for i in range(M-N+1):
            if haystack[i] != needle[0]:
                continue
            else:
                ret = True
                for j in range(N):
                    if haystack[i+j] != needle[j]:
                        ret = False
                        break
                if ret:
                    return haystack[i:]
        return None
    # O(m*n) way

    # KMP way, which is my final way
    def strStr_2(self, haystack, needle):
        H = len(haystack)
        N = len(needle)
        if N == 0:
            return haystack
        i = 0
        while i < H - N + 1:
            if haystack[i] == needle[0]:
                start = None            # Use None here
                j = 1
                while j < N:
                    if haystack[i+j] != needle[j]:
                        break
                    elif start is None and haystack[i+j] == needle[0]: # Find first dup occurance
                        start = i + j
                    j += 1
                if j == N:
                    return haystack[i:]
                if start is not None:
                    i = start - 1       # Detail, need to check start - 1
                else:
                    i = i + j - 1
            i += 1
        return None
    # Note:
    # 1. Note line 53 and 54, minus one there, but in interview, probably do i += 1 in else will be better
    # 2. Both ways will pass
```
-----

##[42. Insert Interval](https://oj.leetcode.com/problems/insert-interval/)

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

```python

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        res = []
        inserted = False
        for inter in intervals:
            if not inserted and inter.start > newInterval.end:
                res.append(newInterval)
                res.append(inter)
                inserted = True
            elif inter.start > newInterval.end or inter.end < newInterval.start:
                res.append(inter)
            else:
                newInterval.start = min(newInterval.start, inter.start)
                newInterval.end   = max(newInterval.end, inter.end)
        if not inserted:
            res.append(newInterval)
        return res

    # Note:
    # 1. Line 29, the if not inserted check is very important
    # 2. Three conditions very important
 This works, but leetcode require a sorted result
    def insert(self, intervals, newInterval):
        res = []
        for i, inter in enumerate(intervals):
            if inter.start > newInterval.end or inter.end < newInterval.start:
                res.append(inter)
                continue
            if newInterval.start >= inter.start and newInterval.start <= inter.end:
                newInterval.start = min(inter.start, newInterval.start)
            if newInterval.end >= inter.start and newInterval.end <= inter.end:
                newInterval.end = max(inter.end, newInterval.end)
        res.append(newInterval)
        return res



 To complicated
    def insert(self, intervals, newInterval):
        if newInterval.end < intervals[0].start:
            intervals.insert(0, newInterval)
            return intervals
        elif newInterval.start > intervals[-1].end:
            intervals.append(newInterval)
            return intervals
        i = 0
        ret = []
        while i < len(intervals):
            if intervals[i].start <= newInterval.start and intervals[i].end >= newInterval.start:
                break
            else:
                ret.append(intervals[i])
        newInterval.start = min(intervals[i].start, newInterval.start)
        while i < len(intervals):
            i += 1
            if intervals[i].start <= newInterval.end and intervals[i].end >= newInterval.end:
                break
        newInterval.end = max(intervals[i].end, newInterval.end)
        ret.append(newInterval)
        i += 1
        while i < len(intervals):
            ret.append(intervals[i])
        return ret

```
-----

##[43. Insertion Sort List](https://oj.leetcode.com/problems/insertion-sort-list/)

Sort a linked list using insertion sort.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        dummy = ListNode(-9223372036854775807-1)
        dummy.next = head
        cur = dummy
        while cur.next is not None:
            if cur.val < cur.next.val:
                cur = cur.next
            else:
                insert = cur.next
                cur.next = insert.next
                start = dummy
                while start.val < insert.val:
                    prev = start
                    start = start.next
                prev.next = insert
                insert.next = start
        return dummy.next

    # Write everything in one func MAY increase the speed of processing
    # Made a mistake here, pasted the code to Sort List and coulnd't pass...
    # 1. The insertion sort shown in wiki, will check from back to front. It's the same to check from front-back
```
-----

##[44. Integer to Roman](https://oj.leetcode.com/problems/integer-to-roman/)

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

```python

class Solution:
    # @return a string
    def intToRoman(self, num):
        digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD' ),
                  (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                  (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ""
        for digit in digits:
            while num >= digit[0]:
                result += digit[1]
                num -= digit[0]
            if num == 0:
                break
        return result
```
-----

##[45. Interleaving String](https://oj.leetcode.com/problems/interleaving-string/)

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

```python

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        return self.isInterleave_1(s1, s2, s3)

    def isInterleave_1(self, s1, s2, s3):
        M = len(s1)
        N = len(s2)
        K = len(s3)
        if M + N != K:
            return False
        dp = [ [ False for j in range(N+1)] for i in range(M+1) ]
        for i in range(M+1):
            for j in range(N+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i > 0 and dp[i-1][j] and s1[i-1] == s3[i-1+j]:
                    dp[i][j] = True
                elif j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[M][N]

    # Note:
    # 1. dp[i][j] means whether s1[:i] and s2[:j] is interleave with s3[:i+j]
    # 2. dp[0...M][0...N] = False
    # 3. dp[i][j] = True   # if dp[i-1][j] == True and s1[i-1] == s3[i-1+j] or
    #                           dp[i][j-1] == True and s2[j-1] == s3[i+j-1]
    #             = False  # else
    # 4. dp[M][N]

    # Will TLE
    def isInterleave_2(self, s1, s2, s3):
        return self.isInterleave_re(s1, 0, s2, 0, s3, 0)

    def isInterleave_re(self, s1, i1, s2, i2, s3, i3):
        if i1 >= len(s1) and i2 >= len(s2) and i3 >= len(s3):
            return True
        if i3 >= len(s3):
            return False
        if i1 >= len(s1):
            return s2[i2:] == s3[i3:]
        if i2 >= len(s2):
            return s1[i1:] == s3[i3:]

        return (s1[i1] == s3[i3] and self.isInterleave_re(s1, i1+1, s2, i2, s3, i3+1)) or (s2[i2] == s3[i3] and self.isInterleave_re(s1, i1, s2, i2+1, s3, i3+1))
```
-----

##[46. Jump Game](https://oj.leetcode.com/problems/jump-game/)

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

```python

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        return self.canJump_1(A)

    # Real DP way, but TLE. This is a O(n^2)'s solution
    def canJump_3(self, A):
        if A[0] == 0:
            return False
        N = len(A)
        dp = [False for i in range(N)]
        dp[0] = True
        for i in range(1, N):
            for j in range(i)[::-1]:
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break
        return dp[N-1]
    # Note:
    # 1. dp[i] means whether we can jump to i
    # 2. dp[0] = True
    # 3. dp[i] = True if from i-1 ... 0 if we can jump to i
    # 4. dp[N-1]

    # Constant DP
    def canJump_1(self, A):
        pre_max = A[0]
        for i in range(1, len(A)):
            max_jump = max(pre_max-1, A[i-1]-1)
            if max_jump < 0:            # Note this is < 0 but not <= 0
                return False
            pre_max = max_jump
        return True

    # Another DP
    def canJump_2(self, A):
        dp = [0 for i in range(len(A))]
        dp[0] = A[0]
        for i in range(1, len(A)):
            dp[i] = max(dp[i-1]-1, A[i-1]-1)
            if dp[i] < 0:
                return False
        return True
    # Note:
    # 1. dp[i] means at i, we can jump to where
    # 2. dp[0] = A[0]
    # 3. dp[i] = max(A[i-1]-1, dp[i-1]-1), if dp[i] < 0: then return False
    # return True if we can finish the loop
```
-----

##[47. Jump Game II](https://oj.leetcode.com/problems/jump-game-ii/)

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

```python

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        N = len(A)
        dp = [N for i in range(N)]
        dp[0] = 0
        for i in range(N):
            for j in range(i)[::-1]:
                if A[j] + j >= i:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[N-1]
    # Note:
    # 1. dp means jump to i, the min jump steps
    # 2. dp[0] = 0
    # 3. dp[i] = min(dp[i],dp[j]+1) if A[j] + j >= i

    def jump(self, A):
        n = len(A)
        if n == 1:
            return 0
        res = 0
        start = 0
        while start < n-1:
            res += 1
            if start + A[start] >= n-1:
                return res
            max_step = start
            for i in range(start+1, start+A[start]+1):
                if i + A[i] >= max_step + A[max_step]: # Here doesn't have to be >=
                    max_step = i
            start = max_step
```
-----

##[48. LRU Cache](https://oj.leetcode.com/problems/lru-cache/)

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

```python

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.cache and len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        elif key in self.cache:
            del self.cache[key]
        self.cache[key] = value

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    # @return an integer
    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.cache) >= self.capacity:
            remove = self.queue.pop(0)
            self.cache.pop(remove)

        self.queue.append(key)
        self.cache[key] = value

    # Checked online, so changed to use python's ordered dictionary
    # So obsoleted queue
    # Also, there was some understanding mistake
    # When get a key, it won't delete the key, but just reorder it to highier rank
    # Just like a cache. Don't think it as a dict
```
-----

##[49. Largest Rectangle in Histogram](https://oj.leetcode.com/problems/largest-rectangle-in-histogram/)

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

```python

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        return self.largestRectangleArea_2(height)

    # Only calculate when decrease
    def largestRectangleArea_1(self, height):
        N = len(height)
        max_area = 0
        for i in range(N):
            if i+1 < N and height[i] <= height[i+1]:
                continue
            min_height = height[i]
            j = i
            while j >= 0:
                min_height = min(min_height, height[j])
                max_area = max(max_area, min_height * (i-j+1))
                j -= 1
        return max_area

    # Use stack to merge the blocks
    def largestRectangleArea_2(self, height):
        height.append(0)                # append 0 to the end, used to find the last
        N = len(height)
        stack = []
        max_area = 0
        i = 0
        while i < N:
            if len(stack) == 0 or height[i] >= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                index = stack.pop()
                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, width * height[index])
        return max_area
    # 维护一个递增序列
```
-----

##[50. Length of Last Word](https://oj.leetcode.com/problems/length-of-last-word/)

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

```python

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return self.lengthOfLastWord_3(s)

    def lengthOfLastWord_1(self, s):
        if len(s.strip()) == 0:                   # Need to check if len(s) is 0
            return 0
        return len(s.strip().split()[-1])         # Python way

    def lengthOfLastWord_2(self, s):              # My way
        n = len(s) - 1
        while n >= 0 and s[n] == ' ':
            n -= 1
        i = 0
        while n >= 0 and s[n] != ' ':
            n -= 1
            i += 1
        return i

    def lengthOfLastWord_3(self, s):              # Annie way
        n = len(s) - 1
        res = 0
        while n >= 0:
            if s[n] != ' ':
                res += 1
            elif res > 0:
                break
            n -= 1
        return res
```
-----

##[51. Letter Combinations of a Phone Number](https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/)

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

```python

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.digit_map = { '2': 'abc',
                           '3': 'def',
                           '4': 'ghi',
                           '5': 'jkl',
                           '6': 'mno',
                           '7': 'pqrs',
                           '8': 'tuv',
                           '9': 'wxyz'
                           }
        return self.letterCombinations_2(digits)

    def letterCombinations_1(self, digits):
        ret = ['']
        for digit in digits:
            res = []
            for comb in ret:
                for digit_char in self.digit_map[digit]:
                    res.append(comb+digit_char)
            ret = res
        return ret

    # Recursion way to do this
    def letterCombinations_2(self, digits):
        ret = []
        self.letterCombinations_rec(0, digits, '', ret)
        return ret

    def letterCombinations_rec(self, i, digits, res, ret):
        if i == len(digits):
            ret.append(res[:])
            return
        for char in self.digit_map[digits[i]]:
            self.letterCombinations_rec(i+1, digits, res + char, ret)
```
-----

##[52. Linked List Cycle](https://oj.leetcode.com/problems/linked-list-cycle/)

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
```
-----

##[53. Linked List Cycle II](https://oj.leetcode.com/problems/linked-list-cycle-ii/)

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow = head.next
        fast = head.next.next
        while slow!=fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
        fast = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow

    # Remember to set slow = head.next and fast = head.next.next before entering the loop
```
-----

##[54. Longest Common Prefix](https://oj.leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings.

```python

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        N = len(strs)
        compare = strs[0]
        for i in range(len(compare)):
            for str in strs[1:]:
                if len(str) == i or str[i] != compare[i]:
                    return compare[:i]
        return compare
```
-----

##[55. Longest Consecutive Sequence](https://oj.leetcode.com/problems/longest-consecutive-sequence/)

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

```python

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        return self.longestConsecutive_2(num)

    # Using dict
    def longestConsecutive_1(self, num):
        num_dict = {}
        for i in num:
            if i not in num_dict:
                num_dict[i] = True
        ret = 1
        for i in num:
            if i not in num_dict:
                continue
            length = 1
            j = i
            while j + 1 in num_dict:
                length += 1
                num_dict.pop(j+1, None)
                j += 1
            j = i
            while j - 1 in num_dict:
                length += 1
                num_dict.pop(j-1, None)
                j -= 1
            ret = max(ret, length)
            num_dict.pop(i, None)
        return ret

    # Not using dict
    def longestConsecutive_2(self, num):
        ret = 1
        for i in num[:]:
            if i not in num:
                continue
            length = 1
            j = i
            while j+1 in num:
                length += 1
                num.remove(j+1)
                j += 1
            j = i
            while j-1 in num:
                length += 1
                num.remove(j-1)
                j -= 1
            ret = max(ret, length)
            num.remove(i)
        return ret


# This is correct but exceeded the time limit
# This should be done in finding the num for both directions, need to remember this

    def longestConsecutive_1(self, num):
        if len(num) <= 1:
            return len(num)
        dp_dict = {}
        ret = 1
        for i in num:
            j = i
            length = 1
            while j+1 in num:
                if j+1 in dp_dict:
                    length = length + dp_dict[j+1]
                    break
                length += 1
                j += 1
            ret = max(ret, length)
            dp_dict[i] = length
        return ret

```
-----

##[56. Longest Palindromic Substring](https://oj.leetcode.com/problems/longest-palindromic-substring/)

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

```python

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        N = len(s)
        dp = [ [ False for j in range(N)] for i in range(N)]
        max_length = 0
        ret = s[0]
        # dp[i][j] means s[i:j] is palindrome
        for j in range(N):
            for i in range(j):
                dp[i][j] == (s[i] == s[j] and ( j - i < 2 or dp[i+1][j-1]))
                if dp[i][j] and max_length < j-i+1:
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        ret = s[i:j]
            dp[j][j] = True
        return ret


    def longestPalindrome(self, s):
        longest, mid = "", (len(s) - 1) / 2
        i, j = mid, mid
        while i >= 0 and j < len(s):
            args = [(s, i, i), (s, i, i + 1), (s, j, j), (s, j, j + 1)]
            for arg in args:
                tmp = self.longestPalindromeByAxis(*arg)
                if len(tmp) > len(longest):
                    longest = tmp
            if len(longest) >= i * 2:
                return longest
            i, j = i - 1, j + 1
        return longest

    def longestPalindromeByAxis(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return s[left + 1 : right]

    def longestPalindrome(self, s):
        arr = ['$', '#']
        for i in range(len(s)):
            arr.append(s[i])
            arr.append('#')
        p = [0] * len(arr)
        mx, pos, ansp = 0, 0, 0
        for i in range(1, len(arr)):
            p[i] = min(mx - i, p[2 * pos - i]) if mx > i else 1
            while p[i] + i < len(arr) and arr[i + p[i]] == arr[i - p[i]]:
                p[i] += 1
            if p[i] + i > mx:
                mx, pos = p[i] + i, i
            if p[i] > p[ansp]:
                ansp = i
        st = (ansp - p[ansp] + 1) // 2
        return s[st:st + p[ansp] - 1]

```
-----

##[57. Longest Substring Without Repeating Characters](https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

```python

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        max_len = 0
        d = {}
        for i, char in enumerate(s):
            if char in d:
                start = max(start,d[char] + 1)
            d[char] = i
            max_len = max(max_len, i-start+1)
        return max_len

    # I did this totally by myself. Previous solution was wrong.

    
    This is not incorrect, but waste too much time
    def lengthOfLongestSubstring(self, s):
        N = len(s)
        if N <= 1:
            return N
        d = {}
        max_len = 0
        cur = 0
        i = 0
        while i < N:
            if s[i] not in d:
                d[s[i]] = i
                cur += 1
                max_len = max(max_len, cur)
                i += 1
            else:
                i = d[s[i]] + 1
                d = {}
                cur = 0
        return max_len
    
```
-----

##[58. Longest Valid Parentheses](https://oj.leetcode.com/problems/longest-valid-parentheses/)

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

```python

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        N = len(s)
        if N <= 1:
            return 0
        ret = 0
        stack = []
        last = -1
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    last = i
                else:
                    index = stack.pop()
                    if len(stack) == 0:
                        ret = max(ret, i - last)
                    else:
                        ret = max(ret, i - stack[-1])
        return ret
```
-----

##[59. Max Points on a Line](https://oj.leetcode.com/problems/max-points-on-a-line/)

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

```python

# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        N = len(points)
        if N <= 2:
            return N
        ret = 2
        for i, p1 in enumerate(points[:-1]):
            slots = {}
            same = 0
            vertical = 1
            current_max = 0
            for j, p2 in enumerate(points[i+1:]):
                if p1.x == p2.x and p1.y == p2.y:
                    same += 1
                elif p1.x == p2.x:
                    vertical += 1
                    #print vertical
                else:
                    k = (p1.y - p2.y) * 1.0 / (p1.x - p2.x)
                    if k not in slots:
                        slots[k] = 2
                    else:
                        slots[k] += 1
            for slot in slots.keys():
                current_max = max(current_max, slots[slot] + same) # Here need to check twice
            ret = max(ret, current_max, vertical+same)             # Cuz slot might be empty
        return ret
```
-----

##[60. Maximal Rectangle](https://oj.leetcode.com/problems/maximal-rectangle/)

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

```python

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        return self.maximalRectangle_2(matrix)

    def maximalRectangle_1(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [ [ (0,0) for j in range(col)] for i in range(row) ]
        max_area = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    continue
                if j == 0:
                    x = 1
                else:
                    x = dp[i][j-1][0] + 1
                if i == 0:
                    y = 1
                else:
                    y = dp[i-1][j][1] + 1

                dp[i][j] = (x, y)
                min_width = y
                for k in range(j-x+1,j+1)[::-1]:
                    min_width = min(min_width, dp[i][k][1])
                    max_area = max(max_area, min_width * (j-k+1))
        return max_area
    # From Annie's way
    # Need to note that i -> y and j -> x
    # dp[i][j] means the consecutive length to matrix[i][j]

    # Use the historical problem's O(n) way to solve once we have the dp
    def maximalRectangle_2(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return 0
        h = [0 for i in range(col+1)]
        max_area = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    h[j] = 0
                else:
                    h[j] += 1
            max_area = max(max_area, self.largestRectangleArea(h))

        return max_area

    def largestRectangleArea(self, h):
        stack = []
        max_area = 0
        for i in range(len(h)):
            count = 0
            while len(stack) > 0 and stack[-1] > h[i]:
                count += 1
                max_area = max(max_area, count * stack.pop())
            count -= 1
            while count > 0:
                stack.append(h[i])
            stack.append(h[i])
        return max_area
```
-----

##[61. Maximum Depth of Binary Tree](https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/)

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        return max( self.maxDepth(root.left), self.maxDepth(root.right) ) + 1
```
-----

##[62. Maximum Subarray](https://oj.leetcode.com/problems/maximum-subarray/)

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

```python

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        return self.maxSubArray_2(A)

    def maxSubArray_1(self, A):
        max_sum = A[0]
        cur_sum = 0
        for num in A:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

    # dp way
    # dp[i] = max(A[i], dp[i-1]+A[i])
    # Because we don't need to store dp[i], so simplify to dp
    def maxSubArray_2(self, A):
        res = A[0]
        dp = A[0]
        for num in A[1:]:
            dp = max(num, dp+num)
            res = max(res, dp)
        return res
```
-----

##[63. Median of Two Sorted Arrays](https://oj.leetcode.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

```python

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        if length % 2 == 0:
            return ( self.findKth(A, 0, B, 0, length / 2) + self.findKth(A, 0, B, 0, length / 2 + 1) ) / 2.0
        else:
            return self.findKth(A, 0, B, 0, length / 2 + 1)

    def findKth(self, A, A_start, B, B_start, k):
        if A_start >= len(A):
            return B[B_start + k - 1]
        if B_start >= len(B):
            return A[A_start + k - 1]

        if k == 1:
            return min(A[A_start], B[B_start])

        if A_start + k/2 -1 < len(A):
            A_key = A[A_start + k/2 -1]
        else:
            A_key = 9223372036854775807

        if B_start + k/2 -1 < len(B):
            B_key = B[B_start + k/2 -1]
        else:
            B_key = 9223372036854775807

        if A_key < B_key:
            return self.findKth(A, A_start + k / 2, B, B_start, k - k/2)
        else:
            return self.findKth(A, A_start, B, B_start + k / 2, k - k/2)

        # So manny details:
        # 1. last line is k - k/2
        # 2. Line 10, divided by 2.0 to make it float
        # 3. don't forget to -1 or +1 on some index
```
-----

##[64. Merge Intervals](https://oj.leetcode.com/problems/merge-intervals/)

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

```python

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        N = len(intervals)
        if N <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        ret = []
        prev = intervals[0]
        for inter in intervals[1:]:
            if inter.start <= prev.end: # Can merge
                prev.end = max(prev.end, inter.end)
            else:
                ret.append(prev)
                prev = inter
        ret.append(prev)
        return ret
```
-----

##[65. Merge Sorted Array](https://oj.leetcode.com/problems/merge-sorted-array/)

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

```python

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m - 1
        j = n - 1
        x = m + n - 1
        while i>=0 and j>=0:
            if A[i] > B[j]:
                A[x] = A[i]
                i -= 1
            else:
                A[x] = B[j]
                j -= 1
            x -= 1
        while j>=0:
            A[x] = B[j]
            x -= 1
            j -= 1
    # Focus on detail!!!
```
-----

##[66. Merge Two Sorted Lists](https://oj.leetcode.com/problems/merge-two-sorted-lists/)

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Use dummy
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1 is not None:
            cur.next = l1

        if l2 is not None:
            cur.next = l2

        return dummy.next
```
-----

##[67. Merge k Sorted Lists](https://oj.leetcode.com/problems/merge-k-sorted-lists/)

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        pq = []
        for node in lists:
            if node is not None:
                heapq.heappush(pq, (node.val, node))
        dummy = ListNode(0)
        cur = dummy
        while len(pq) > 0:
            val, node = heapq.heappop(pq)
            cur.next = node
            cur = cur.next
            if node.next is not None:
                heapq.heappush(pq, (node.next.val, node.next))
        return dummy.next

    # Remember this to use Priority Queue
```
-----

##[68. Minimum Depth of Binary Tree](https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/)

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        return self.minDepth_rec(root)

    def minDepth_rec(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth_rec(root.right) + 1
        if root.right is None:
            return self.minDepth_rec(root.left) + 1
        return min(self.minDepth_rec(root.left), self.minDepth_rec(root.right)) + 1

    # Must do it in this way.
    # It's different from the maxDepth because in max, we search for max
    # In this min, the min depth is root to leaf node
    # A leaf node is node does not have any child.
    # Those has one child cannot be called leaf node

    def minDepth_iter(self, root):
        if root is None:
            return 0
        queue = []
        queue.append( (root, 1) )
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                queue.append( (node.left, depth+1) )
            if node.right is not None:
                queue.append( (node.right, depth+1) )
```
-----

##[69. Minimum Path Sum](https://oj.leetcode.com/problems/minimum-path-sum/)

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

```python

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        M = len(grid)
        N = len(grid[0])
        dp = [ [0 for j in range(N)] for i in range(M)]
        for i in range(M):
            for j in range(N):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[M-1][N-1]

    # Note:
    # 1. dp[i][j] means from (0, 0) to (i, j) the min path sum
    # 2. init: dp[i][0] = dp[i-1][0]+grid[i][j], dp[0][j] += dp[0][j-1]+grid[i][j]
    # 3. func: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    # 4. ret: dp[m-1][n-1]

All Previous work. No need to worry
    def minPathSum_1(self, grid):
        M = len(grid)
        N = len(grid[0])
        dp = [[ 0 for j in range(N)] for i in range(M)]
        dp[0][0] = grid[0][0]
        for i in range(1, M):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, N):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[M-1][N-1]

    # Another time:
    # dp[m][n] dp[i][j]
    # M is the rows
    # N is the cols
    # [[for j in range(N)] for i in range(M)]
    # M = len(grid)
    # N = len(grid[0])


    Given the dynamic programming formula f[i][j]=min(f[i-1][j],f[i][j-1])+grid[i][j]:

    Assume that you are populating the table row by row, the current value (f[i][j]) will be used immediately in the calculation of f[i][j+1], so there is no need to store all the previous column values.

    Therefore, you can do it in linear space complexity.

    def minPathSum_2(self, grid):
        M = len(grid)
        N = len(grid[0])
        dp = [ 0 for j in range(N)]
        dp[0] = grid[0][0]
        for j in range(1, N):
            dp[j] = dp[j-1] + grid[0][j]
        for i in range(1, M):
            dp[0] += grid[i][0]
            for j in range(1, N):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        return dp[N-1]

    # This is a bit tricky. Read the above how to simplify this
    # The key is we are doing this for j ... so we can just j-1

```
-----

##[70. Minimum Window Substring](https://oj.leetcode.com/problems/minimum-window-substring/)

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

```python

class Solution:
    # @return a string
    def minWindow(self, S, T):
        N = len(S)
        M = len(T)
        if N < M:
            return ''
        need = dict.fromkeys(T, 0)
        find = dict.fromkeys(T, 0)
        for i, char in enumerate(T):
            need[char] += 1
        start = 0
        end = 0
        res_start = -1
        res_end = N
        count = 0
        while end < N:
            if S[end] not in need:
                end += 1
                continue
            if find[S[end]] < need[S[end]]:
                count += 1
            find[S[end]] += 1
            if count != M:
                end += 1
                continue
            while start < end:
                if S[start] not in need:
                    start += 1
                    continue
                if find[S[start]] == need[S[start]]:
                    break
                find[S[start]] -= 1
                start += 1
            if end - start < res_end - res_start:
                res_end = end
                res_start = start
            end += 1
        if res_start == -1:
            return ''
        else:
            return S[res_start: res_end+1]

    # Whole bunch of things can be improved from here
```
-----

##[71. Multiply Strings](https://oj.leetcode.com/problems/multiply-strings/)

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.

```python

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        res = 0
        for i, bit_i in enumerate(num1[::-1]):
            num_i = int(bit_i) * (10**i)
            for j, bit_j in enumerate(num2[::-1]):
                num_j = int(bit_j) * (10**j)
                res += num_i * num_j
        return str(res)
```
-----

##[72. N-Queens](https://oj.leetcode.com/problems/n-queens/)

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

```python

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        ret = []
        res = ['.' * n for i in range(n)]
        self.solveNQueens_helper(n, res, ret, 0)
        return ret

    def solveNQueens_helper(self, n, res, ret, queens):
        if queens == n:
            ret.append(res[:])
            return
        for i in range(n):
            new_row = '.'*n
            res[queens] = new_row[:i] + 'Q' + new_row[i+1:]
            if self.is_valid(res, queens, i):
                self.solveNQueens_helper(n, res, ret, queens+1)
            res[queens] = new_row

    def is_valid(self, board, row, col):
        for i in range(row):
            for j in range(len(board[0])):
                if board[i][j] == 'Q' and (j == col or abs(row-i) == abs(col-j)):
                    return False
        return True

    # Note:
    # 1. Remember this it's row-i == col-j
    # 2. The other way to do is use res.append() then pop()
    # 3. In this case, is_valid, we can do str.find('Q') or [char for char in line].index('Q') to get index
```
-----

##[73. N-Queens II](https://oj.leetcode.com/problems/n-queens-ii/)

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

```python

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.ret = 0
        self.totalNQueens_helper(n, [])
        return self.ret

    def totalNQueens_helper(self, n, res):
        if len(res) == n:
            self.ret += 1                    # ret.append(res[:])
            return
        for i in range(n):
            res.append(i)
            if self.is_valid(res):
                self.totalNQueens_helper(n, res)
            res.pop()

    def is_valid(self, board):
        l = len(board) - 1
        for i in range(len(board)-1):
            if board[i] == board[l] or abs(board[i]-board[l]) == abs(i-l):
                    return False
        return True

    # First remember this is diff to a normal cheesboard,
    # placing a n*n chess board
    # input 1, expect 1 but not 8
    # Keep in mind the way to use self.ret as global
```
-----

##[74. Next Permutation](https://oj.leetcode.com/problems/next-permutation/)

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

```python

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) <= 1:
            return num
        i = len(num) - 1
        while i > 0 and num[i-1]>= num[i]: # It's >=
            i -= 1
        num = num[:i] + sorted(num[i:])
        if i == 0:
            return num
        j = i
        while j < len(num) and num[i-1] >= num[j]: # again >=
            j += 1
        self.swap(i-1, j, num)
        return num

    def swap(self, i, j, num):
        tmp = num[i]
        num[i] = num[j]
        num[j] = tmp

    # A little bit hard to think
```
-----

##[75. Palindrome Number](https://oj.leetcode.com/problems/palindrome-number/)

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1) No!

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

```python

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 10
        while x > div:
            div *= 10
        div /= 10
        while x > 0:
            if x / div != x % 10:
                return False
            x = (x % div) / 10
            div /= 100
        return True
```
-----

##[76. Palindrome Partitioning](https://oj.leetcode.com/problems/palindrome-partitioning/)

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

```python

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        res = []
        ret = []
        self.partition_helper(s, res, ret)
        return ret

    def partition_helper(self, s, res, ret):
        N = len(s)
        if N == 0 :
            ret.append(res[:])
            return
        for i in range(1, N+1):         # This N+1 is important
            if self.is_palindrome(s[:i]):
                res.append(s[:i])
                self.partition_helper(s[i:], res, ret)
                res.pop()

    def is_palindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    # This function can use return s == s[::-1] to replace.```
-----

##[77. Palindrome Partitioning II](https://oj.leetcode.com/problems/palindrome-partitioning-ii/)

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

```python

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        N = len(s)
        dp = [ N for i in range(N)]
        dp[0] = 0
        for i in range(1, N):
            dp[i] = sys.maxint
            for j in range(i)[::-1]:
                if self.isPalindrome(s[j:i]):
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[N-1]

    def isPalindrome(self, s):
        return s == s[::-1]

    # 1. dp means from 0 ... i the mean cut of palin
    # 2. dp[0] = 0
    # 3. dp[i] = min(dp[i], dp[j]+1) for j = i-1 ... 0 if isPalin(s[j:i])
    # 4. dp[N-1]
    # This idea is correct, but next thing is to reduce the cost of isPalindrome
```
-----

##[78. Partition List](https://oj.leetcode.com/problems/partition-list/)

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        before_cur = before_dummy
        after_cur = after_dummy
        while head is not None:
            if head.val < x:
                before_cur.next = head
                before_cur = before_cur.next
                head = head.next
                before_cur.next = None
            else:
                after_cur.next = head
                after_cur = after_cur.next
                head = head.next
                after_cur.next = None
        if before_dummy.next is not None:
            before_cur.next = after_dummy.next
            return before_dummy.next
        else:
            return after_dummy.next
        # Set None can be done for only last
```
-----

##[79. Pascals Triangle](https://oj.leetcode.com/problems/pascals-triangle/)

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

```python

class Solution:
    # @return a list of lists of integers
    def generate(numRows):
        return self.generate_1(numRows)

    def generate_1(self, numRows):
        res = []
        for j in range(numRows):
            current = [1]
            for i in range(1, j):
                current.append(res[-1][i]+res[-1][i-1])
            if j>=1:
                current.append(1)
            res.append(current[:])
        return res

    def generate_2(self, numRows):
        if numRows ==0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1], [1,1]]
        prev = [1,1]
        for j in range(numRows-1):
            current = [1]
            for i in range(1,len(prev)):
                current.append(prev[i]+prev[i-1])
            current.append(1)
            res.append(current[:])
            prev = current
        return res
```
-----

##[80. Pascals Triangle II](https://oj.leetcode.com/problems/pascals-triangle-ii/)

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

```python

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        return self.getRow_2(rowIndex)

    def getRow_1(self, rowIndex):
        ret = [1]
        if rowIndex == 0:
            return ret
        while rowIndex > 0:
            if len(ret) > 1:
                for i in range(1, len(ret)):
                    ret[i-1] = ret[i] + ret[i-1]
            ret.insert(0, 1)
            rowIndex -= 1
        return ret

    def getRow_2(self, rowIndex):
        ret = [1 for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(i-1, 0, -1):
                ret[j] += ret[j-1]
        return ret
```
-----

##[81. Path Sum](https://oj.leetcode.com/problems/path-sum/)

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
```
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None: # Found a leaf
            if sum == root.val:
                return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

    # Need to note, a leaf is a node has no left chind and no right child
```
-----

##[82. Path Sum II](https://oj.leetcode.com/problems/path-sum-ii/)

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
```
return
[
   [5,4,11,2],
   [5,8,4,5]
]

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        ret = []
        self.pathSum_helper(root, sum, [], ret)
        return ret

    def pathSum_helper(self, root, sum, res, ret):
        if root is None:
            return
        if root.left is None and root.right is None:
            if sum == root.val:
                res.append(root.val)
                ret.append(res[:])
                res.pop()
            return
        res.append(root.val)
        self.pathSum_helper(root.left, sum - root.val, res, ret)
        self.pathSum_helper(root.right, sum - root.val, res, ret)
        res.pop()


This way will have long run time
    def pathSum(self, root, sum):
        if root is None:
            return []
        ret = []
        self.pathSum_helper(root, sum, [root.val], ret)
        return ret

    def pathSum_helper(self, root, sum, res, ret):
        if root.left is None and root.right is None: # Found a leaf
            if sum == root.val:
                ret.append(res[:])
                return
        if root.left is not None:
            res.append(root.left)
            self.pathSum_helper(root.left, sum, res, ret)
            res.pop()
        if root.right is not None:
            res.append(root.right)
            self.pathSum_helper(root.right, sum, res, ret)
            res.pop()

```
-----

##[83. Permutation Sequence](https://oj.leetcode.com/problems/permutation-sequence/)

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

```python

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        num_list = []
        total = 1
        res = ''
        for i in range(1, n+1):         # Detail!!! this is n+1
            total *= i
            num_list.append(str(i))
        k -= 1                          # This is very important
        while n > 0:
            total /= n
            i = k / total
            k %= total
            res += num_list[i]
            num_list.pop(i)
            n -= 1
        return res

    # total is very important here
```
-----

##[84. Permutations](https://oj.leetcode.com/problems/permutations/)

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

```python

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        return self.permute_2(num)

    # Normal way to think about this
    def permute_1(self, num):
        ret = []
        self.permute_helper([], num, ret)
        return ret

    def permute_helper(self, res, num, ret):
        if len(num) == 0:
            ret.append(res[:])
            return
        for i, n in enumerate(num):
            res.append(n)
            self.permute_helper(res, num[:i]+num[i+1:], ret)
            res.pop()

    # Do this "inplace"
    def permute_2(self, num):
        if len(num) == 0:
            return [[]]                 # This is the tricky part
        ret = []
        for i, n in enumerate(num):
            rest_perms = self.permute_2( num[:i]+num[i+1:] )
            for perm in rest_perms:
                ret.append( [n] + perm)
        return ret
```
-----

##[85. Permutations II](https://oj.leetcode.com/problems/permutations-ii/)

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

```python

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        return self.permuteUnique_2(num)

    def permuteUnique_1(self, num):
        ret = []
        self.permuteUnique_helper(num, [], ret)
        return ret

    def permuteUnique_helper(self, num, res, ret):
        if len(num) == 0:
            ret.append(res[:])
            return
        unique_perm = {}
        for i, n in enumerate(num):
            if n not in unique_perm:
                unique_perm[n] = True
                res.append(n)
                self.permuteUnique_helper(num[:i]+num[i+1:], res, ret)
                res.pop()
        # This is miracle to do this correctly in one time

    def permuteUnique_2(self, num):
        if len(num) == 0:
            return [[]]
        unique_perm = {}
        ret = []
        for i, n in enumerate(num):
            if n not in unique_perm:
                unique_perm[n] = True
                rest_perms = self.permuteUnique_2(num[:i]+num[i+1:])
                for perm in rest_perms:
                    ret.append([n,]+perm)
        return ret
```
-----

##[86. Plus One](https://oj.leetcode.com/problems/plus-one/)

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

```python

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        i = len(digits) - 1
        carry = 1
        while i >= 0 and carry == 1:    # So many detail! No need to continue calculation if carry == 0
            s = digits[i] + carry       # Calculate s first
            digits[i] = s % 10
            carry = s / 10
            i -= 1
        if carry == 1:                  # Last check
            digits.insert(0, 1)
        return digits
```
-----

##[87. Populating Next Right Pointers in Each Node](https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/)

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
```
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
```

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None or root.left is None:
            return
        root.left.next = root.right
        if root.right is not None and root.next is not None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    # Or maybe use a level order traversal
    # Removed one line
```
-----

##[88. Populating Next Right Pointers in Each Node II](https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
```
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
```

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        if root.left is not None:
            if root.right is not None:
                root.left.next = root.right
            else:
                root.left.next = self.find_next(root.next)

        if root.right is not None:
            root.right.next = self.find_next(root.next)

        self.connect(root.right)        # Do right first then left
        self.connect(root.left)

    def find_next(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return self.find_next(root.next)
        if root.left is not None:
            return root.left
        return root.right

    # This is miracle that I can do this with one time!!!!
    # Very simple to think
    # One thing need to notice is that need to do connect right first and then left
    # Because otherwise, when linking towards the right but the right isnt ready there will be error
```
-----

##[89. Powx-n](https://oj.leetcode.com/problems/powx-n/)

Implement pow(x, n).

```python

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if x == 0 or x == 1:
            return x
        elif x < 0 and n % 2 == 0:
            return self.pow(-x, n)
        elif x < 0 and n % 2 ==1:
            return self.pow(-x, n) * (-1)
        elif n < 0:
            return 1.0 / self.pow(x, -n)
        elif n == 0:
            return 1.0
        # Notice here:
        # 1. Must checks: n < 0 and n == 0
        # 2. No need to check x, but if x == 0 or 1 will reduce calculation
        half = self.pow(x, n/2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
    # Note to use the half var to make the code clean
```
-----

##[90. Recover Binary Search Tree](https://oj.leetcode.com/problems/recover-binary-search-tree/)

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        return self.recoverTree_2(root)

    # This is the first attempt, several things need to note
    # first and second need to be a list, so that it can work like pointer
    # Since we are only comparing the last and cur, we dont't need to store the whole list,
    # just use prev like solution 2
    # Be careful when doing the if/else check, we can use only if here like solution 2
    # Notice the way to determine the wrongs, always update the wrongs[1] but wrongs[0] will only updated once

    def recoverTree_1(self, root):
        nodes = []
        wrongs = [None, None]
        self.recoverTree_helper_1(root, nodes, wrongs)
        tmp = wrongs[0].val
        wrongs[0].val = wrongs[1].val
        wrongs[1].val = tmp
        return root

    def recoverTree_helper_1(self, root, nodes, wrongs):
        if root is None:
            return
        self.recoverTree_helper_1(root.left, nodes, wrongs)
        if len(nodes) == 0 or nodes[-1].val < root.val:
            pass
        else:
            if not wrongs[0]:
                wrongs[0] = nodes[-1]
            wrongs[1] = root
        nodes.append(root)
        self.recoverTree_helper_1(root.right, nodes, wrongs)

    # prev need to be a list inorder to use a pointer
    def recoverTree_2(self, root):
        wrongs = [None, None]
        self.recoverTree_helper_2(root, [None], wrongs)
        tmp = wrongs[0].val
        wrongs[0].val = wrongs[1].val
        wrongs[1].val = tmp
        return root

    def recoverTree_helper_2(self, root, prev, wrongs):
        if root is None:
            return
        self.recoverTree_helper_2(root.left, prev, wrongs)
        if prev[0] is not None and prev[0].val > root.val:
            if wrongs[0] is None:
                wrongs[0] = prev[0]
            wrongs[1] = root
        prev[0] = root
        self.recoverTree_helper_2(root.right, prev, wrongs)

    
    The third way is mad
    def recoverTree_3(self, root):
    
```
-----

##[91. Regular Expression Matching](https://oj.leetcode.com/problems/regular-expression-matching/)

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

```python

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        return self.isMatch_helper(s, p, 0, 0)

    def isMatch_helper(self, s, p, i, j):
        if j >= len(p):
            return s[i] >= len(p)

        if s[i] == p[j] or ( p[j] == '.' and i < len(s)):
            if j+1 < len(p) and p[j+1] != '*':
                return self.isMatch_helper(s, p, i+1, j+1)
            else:
                return self.isMatch_helper(s, p, i+1, j) or self.isMatch_helper(s, p, i, j+2)

        return j+1 < len(p) and p[j+1] == '*' and self.isMatch(s, p, i, j+2)

    # Recursion
    def isMatch(self, s, p):
        if len(p)==0: return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i=-1; length=len(s)
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]): return True
                i+=1
            return False

    #dp
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]
```
-----

##[92. Remove Duplicates from Sorted Array](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/)

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

```python

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        return self.removeDuplicates_2(A)

    def removeDuplicates_1(self, A):
        i = 0
        for j in range(len(A)):
            if i == 0 or A[j] != A[j-1]:
                A[i] = A[j]
                i += 1
        return i

    def removeDuplicates_2(self, A):
        if len(A) <= 1:
            return len(A)
        i = 0
        for j in range(1, len(A)):
            if A[i] != A[j]:
                A[i+1] = A[j]
                i += 1
        return i+1
    # Second way is my way
```
-----

##[93. Remove Duplicates from Sorted Array II](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].

```python

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
        start = 1
        cur = 2
        while cur < len(A):
            if A[cur] != A[start] or A[cur] != A[start-1]:
                A[start+1] = A[cur]
                start += 1
            cur+= 1
        return start+1
```
-----

##[94. Remove Duplicates from Sorted List](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/)

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        current = head
        while current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
```
-----

##[95. Remove Duplicates from Sorted List II](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return None
        dummy = ListNode(0)
        cur = dummy
        while head.next is not None:
            if head.val == head.next.val:
                #jump here, need to find next start
                dup = head
                while head is not None and head.val == dup.val:
                    head = head.next
                # Stop if head it None or found a new head val
                if head is None:
                    break
            else:
                cur.next = head
                cur = cur.next
                head = head.next
                cur.next = None         # Clean up the last pointer

        if head is not None:            # Process the last one
            cur.next = head
        return dummy.next
```
-----

##[96. Remove Element](https://oj.leetcode.com/problems/remove-element/)

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

```python

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i = 0
        for j, num in enumerate(A):
            if num != elem:
                A[i] = A[j]
                i += 1
        return i

    # Two pointer problem
```
-----

##[97. Remove Nth Node From End of List](https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/)

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        fast = head
        dummy = ListNode(0)
        dummy.next = head
        while n > 0:
            fast = fast.next
            n -= 1
        slow = dummy
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
```
-----

##[98. Reorder List](https://oj.leetcode.com/problems/reorder-list/)

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None:
            return
        slow = head
        fast = head.next.next                     # Let fast go one more round first then we don't need mid
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        mid = slow
        cur = mid.next
        while cur.next is not None:
            move = cur.next
            cur.next = move.next
            move.next = mid.next
            mid.next = move
        left = head                     # Start to merge two lists
        while left != mid:              # Ends when left = mid
            right = mid.next
            mid.next = right.next
            right.next = left.next
            left.next = right
            left = right.next

    # Way to think:
    # If we loop the list all the time, it will exceed the time limit
    # So just find the second half, reverse the second half, and merge it with the first half, that's done
    This way should work, but will exceed the time limit
    def reorderList(self, head):
        while head is not None:
            tail = head
            prev = tail
            while tail.next is not None:
                prev = tail
                tail = tail.next
            if prev == tail:
                return
            prev.next = None
            tail.next = head.next
            head.next = tail
            head = tail.next
    
    # Should separate to 3 steps
    # 1. Find middle
    # 2. Reverse second half
    # 3. Merge first half and reversed second half
    # Will be simpler if separate these 3 step
```
-----

##[99. Restore IP Addresses](https://oj.leetcode.com/problems/restore-ip-addresses/)

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

```python

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        ret = []
        self.restoreIpAddresses_helper(s, [], ret)
        return ret

    def restoreIpAddresses_helper(self, s, res, ret):
        if len(res) >= 4 and len(s) != 0:
            return
        if len(res) == 4 and len(s) == 0:
            ret.append('.'.join(res))
            return
        for i in range(1, min(3,len(s))+1):
            # This check is a shit!
            if (int(s[:i]) >= 0 and int(s[:i]) < 256 and s[:i][0]!= '0') or (int(s[:i])==0 and len(s[:i])==1):
                res.append(s[:i])
                self.restoreIpAddresses_helper(s[i:], res, ret)
                res.pop()

        # Note the check:
        # 1. 0<= ip < 255
        # 2. ip shouldn't like 001, 000
```
-----

##[100. Reverse Integer](https://oj.leetcode.com/problems/reverse-integer/)

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

Throw an exception? Good, but what if throwing an exception is not an option? You would then have to re-design the function (ie, add an extra parameter).

```python

class Solution:
    # @return an integer
    def reverse(self, x):
        if x < 0:
            return (-1) * self.reverse( (-1) * x)
        res = 0
        while x > 0:
            res = res*10 + x%10
            x /= 10
        return res
```
-----

##[101. Reverse Linked List II](https://oj.leetcode.com/problems/reverse-linked-list-ii/)

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        i = 1
        while i < m:
            start = start.next
            i += 1
        cur = start.next
        while i < n:
            move = cur.next
            cur.next = move.next
            move.next = start.next
            start.next = move
            i += 1
        return dummy.next
    # Can use or without dummy
```
-----

##[102. Reverse Nodes in k-Group](https://oj.leetcode.com/problems/reverse-nodes-in-k-group/)

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k <= 1:
            return head
        dummy = ListNode(0)
        dummy.next = head

        total_nodes = 0
        cur = head
        while cur is not None:
            cur = cur.next
            total_nodes += 1
        n = total_nodes / k

        prev = dummy
        while n > 0:
            i = 1
            cur = prev.next
            while i < k:
                move = cur.next
                cur.next = move.next
                move.next = prev.next
                prev.next = move
                i += 1
            prev = cur
            n -= 1
        return dummy.next
```
-----

##[103. Reverse Words in a String](https://oj.leetcode.com/problems/reverse-words-in-a-string/)

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


```python
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return self.reverseWords_2(s)

    def reverseWords_1(self, str):
        return ' '.join(str.split()[::-1])

    def reverseWords_2(self, str):
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
```
-----

##[104. Roman to Integer](https://oj.leetcode.com/problems/roman-to-integer/)

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

```python

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_map = { 'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000,
                  }
        ret = 0
        prev = s[0]
        for char in s:
            if roman_map[char] <= roman_map[prev]:
                ret += roman_map[char]
            else:
                ret += roman_map[char] - 2 * roman_map[prev]
            prev = char
        return ret
```
-----

##[105. Rotate Image](https://oj.leetcode.com/problems/rotate-image/)

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

```python

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return self.rotate_2(matrix)

    def rotate_1(self, matrix):
        n = len(matrix)

        for i in range(n/2):
            start = i
            end   = n-1-i
            for j in range(start, end):
                offset = j - start
                top = matrix[start][j]
                matrix[start][j]          = matrix[end-offset][start]  # bottom to top
                matrix[end-offset][start] = matrix[end][end-offset]    # right to left
                matrix[end][end-offset]   = matrix[j][end]             # top to bottom
                matrix[j][end]            = top
        return matrix

    def rotate_2(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                self.swap(matrix, i, j , j, i)
        for i in range(n):
            for j in range(n/2):
                self.swap(matrix, i, j, i, n-1-j)
        return matrix

    def swap(self, matrix, i1, j1, i2, j2):
        tmp = matrix[i1][j1]
        matrix[i1][j1] = matrix[i2][j2]
        matrix[i2][j2] = tmp
```
-----

##[106. Rotate List](https://oj.leetcode.com/problems/rotate-list/)

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head:
            return None
        length = 1
        tail = head                     # Naming
        while tail.next:                # No need to use extra prev
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head                 # Detail
        tail.next = head
        cur = head
        i = 0
        while i < length - k - 1:       # Note this detail
            cur = cur.next
            i += 1
        new_head = cur.next
        cur.next = None
        return new_head
```
-----

##[107. Same Tree](https://oj.leetcode.com/problems/same-tree/)

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```
-----

##[108. Scramble String](https://oj.leetcode.com/problems/scramble-string/)

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

```
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
```
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

```python

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if not self.hasSameLetter(s1, s2):
            return False
        if len(s1) <= 2:
            return True
        for i in range(1, len(s1)):
            if ( self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) ) or ( self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]) ): # This is soooo important, -i!!!
                return True
        return False

    def hasSameLetter(self, s1, s2):
        if sorted(s1) != sorted(s2):
            return False
        return True
    # Another way to do this in dp, need to learn
```
-----

##[109. Search Insert Position](https://oj.leetcode.com/problems/search-insert-position/)

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

```python

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:       # need to search second half
                start = mid + 1
            else:
                end = mid - 1
        return start

    # Too easy way, not the way wanted
    def searchInsert_2(self, A, target):
        for i, num in enumerate(A):
            if target <= num:
                return i
        return len(A)
```
-----

##[110. Search a 2D Matrix](https://oj.leetcode.com/problems/search-a-2d-matrix/)

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

```python

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        start = 0
        end = len(matrix) -1            # -1 !!!
        while start <= end:
            mid = (start + end) / 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                col = mid
                start = 0
                end = len(matrix[0]) -1         # -1!!!
                while start <= end:
                    mid = (start + end) / 2
                    if target == matrix[row][mid]:
                        return True
                    elif target < matrix[row][mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                return False
            elif target < matrix[mid][0]:
                end = mid-1
            else:
                start = mid + 1
        return False

    # This is better, nested matrix

Generate m*n matrix
a = 0
m = []
for i in range(10):
    row = []
    for j in range(8):
        row.append(a)
        a += 1
    m.append(row[:])

```
-----

##[111. Search for a Range](https://oj.leetcode.com/problems/search-for-a-range/)

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

```python

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start = 0
        end = len(A) - 1
        bound = [-1, -1]

        # Check for left bound
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            bound[0] = start
        elif A[end] == target:
            bound[0] = end
        else:
            return bound

        # Check right bound
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[end] == target:
            bound[1] = end
        elif A[start] == target:
            bound[1] = start

        return bound
```
-----

##[112. Search in Rotated Sorted Array](https://oj.leetcode.com/problems/search-in-rotated-sorted-array/)

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

```python

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        return self.search_1(A, target)

    def search_1(self, A, target):
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if target == A[mid]:
                return mid
            if A[start] < A[mid]:                           # First half sorted
                if A[start] <= target < A[mid]:             # In first half
                    end = mid
                else:                                       # In second half
                    start = mid
            else:                                           # Second half sorted
                if A[mid] < target <= A[end]:               # In second half
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

    # Switching to NC way, use start+1 < end instead

    def search_rec(self, A, target):
        return self.search_helper(A, target, 0, len(A) - 1)

    def search_helper(self, A, target, start, end):
        if start > end:
            return -1
        mid = (start  + end) / 2
        if A[mid] == target:
            return mid
        elif A[mid] > A[end]:         # First half sorted
            if A[start] <= target and target < A[mid]:
                return self.search_helper(A, target, start, mid - 1)
            else:
                return self.search_helper(A, target, mid + 1, end)
        else:                           # Second half sorted
            if A[mid] < target and target <= A[end]:
                return self.search_helper(A, target, mid + 1, end)
            else:
                return self.search_helper(A, target, start, mid - 1)
```
-----

##[113. Search in Rotated Sorted Array II](https://oj.leetcode.com/problems/search-in-rotated-sorted-array-ii/)

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

```python

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return True
            elif A[start] < A[mid]:     # First half sorted
                if A[start] <= target and target < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif A[start]> A[mid]:      # Second half sorted
                if A[mid] < target and target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start += 1
        return False
```
-----

##[114. Set Matrix Zeroes](https://oj.leetcode.com/problems/set-matrix-zeroes/)

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

```python

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        n = len(matrix[0])
        m = len(matrix)
        zero_row = False
        zero_col = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_row = True
                    if j == 0:
                        zero_col = True
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zero_col:
            for i in range(m):
                matrix[i][0] = 0

        if zero_row:
            for j in range(n):
                matrix[0][j] = 0

        return matrix
```
-----

##[115. Simplify Path](https://oj.leetcode.com/problems/simplify-path/)

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

```python

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
                    continue
                else:
                    ret.insert(0, p)
        return '/'+'/'.join(ret)
    # Note:
    # 1. Remove dup '/', if using split(), // will become '', remove it
    # 2. Keep in mind those two [::-1]
    # 3. Don't forget to attach the first '/'
```
-----

##[116. Single Number](https://oj.leetcode.com/problems/single-number/)

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

```python

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        for num in A[1:]:
            A[0] ^= num
        return A[0]
```
-----

##[117. Single Number II](https://oj.leetcode.com/problems/single-number-ii/)

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

```python

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bits = [0 for i in range(32)]
        for num in A:
            i = 0
            while num > 0:
                bits[i] += num & 1
                i += 1
                num >>= 1
        for bit in bits:
            bit %= 3
            ret += bit
            ret >>= 1
        ret <<= 1
        return ret
```
-----

##[118. Sort Colors](https://oj.leetcode.com/problems/sort-colors/)

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

```python

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        start = 0
        end = len(A)-1
        i = 0
        while i <= end:
            if A[i]==0:
                self.swap(start, i, A)
                start += 1
                i += 1
            elif A[i]==2:
                self.swap(end, i, A)
                end -= 1
            else:
                i += 1
        return

    def swap(self, a, b, A):
        tmp = A[a]
        A[a] = A[b]
        A[b] = tmp

    # Keep in mind that's i<= end
```
-----

##[119. Sort List](https://oj.leetcode.com/problems/sort-list/)

Sort a linked list in O(n log n) time using constant space complexity.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        prev = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        head = self.sortList(head)
        slow = self.sortList(slow)
        return self.sortedMerge(head, slow)

    def sortedMerge(self, head1, head2):
        dummy = ListNode(0)
        head = dummy
        while head1 is not None or head2 is not None:
            if head1 is None:
                head.next = head2
                head2 = head2.next
            elif head2 is None:
                head.next = head1
                head1 = head1.next
            elif head1.val < head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        return dummy.next

    # Way to think about this:
    # 1. Split the list into first half and second half
    # 2. Recursion sort the two half
    # 3. Merge those two
```
-----

##[120. Spiral Matrix](https://oj.leetcode.com/problems/spiral-matrix/)

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].>

```python

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        M = len(matrix)
        if len(matrix) == 0:
            return []
        N = len(matrix[0])
        start_x = 0
        start_y = 0
        end_x   = N - 1
        end_y   = M - 1
        ret = []
        while True:
            for i in range(start_x, end_x + 1):
                ret.append(matrix[start_y][i])
            start_y += 1
            if start_y > end_y:
                break
            for i in range(start_y, end_y + 1):
                ret.append(matrix[i][end_x])
            end_x -= 1
            if start_x > end_x:
                break
            for i in range(start_x, end_x + 1)[::-1]:
                ret.append(matrix[end_y][i])
            end_y -= 1
            if start_y > end_y:
                break
            for i in range(start_y, end_y + 1)[::-1]:
                ret.append(matrix[i][start_x])
            start_x += 1
            if start_x > end_x:
                break
        return ret
```
-----

##[121. Spiral Matrix II](https://oj.leetcode.com/problems/spiral-matrix-ii/)

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

```python

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        ret = [ [ 0 for i in range(n)] for j in range(n)]
        num = 1
        start_row = start_col = 0
        end_row = end_col = n - 1
        while start_row < end_row and start_col < end_col:
            for i in range(start_col, end_col + 1):
                ret[start_row][i] = num
                num += 1
            start_row += 1
            for i in range(start_row, end_row + 1):
                ret[i][end_col] = num
                num += 1
            end_col -= 1
            for i in range(end_col, start_col - 1, -1):
                ret[end_row][i] = num
                num += 1
            end_row -= 1
            for i in range(end_row, start_row -1, -1):
                ret[i][start_col] = num
                num += 1
            start_col += 1
        if n%2 == 1:
            ret[start_col][start_row] = num
        return ret
```
-----

##[122. Sqrtx](https://oj.leetcode.com/problems/sqrtx/)

Implement int sqrt(int x).

Compute and return the square root of x.

```python

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        return self.sqrt_1(x)

    # NC way to do this
    def sqrt_1(self, x):
        if x <= 1:
            return x
        left = 0
        right = x
        while left + 1 < right:
            mid = (left + right) / 2
            sqr = mid * mid
            if sqr == x:
                return mid
            elif sqr < x:
                left = mid
            else:
                right = mid
        return left
    # We are looking for the smaller one

    def sqrt_2(self, x):
        left = 0                         # Here must 0, otherwise 1 won't pass
        right = x                        # Use x/2 + 1
        while left <= right:             # <=
            mid = (left + right) / 2
            sqr = mid * mid
            if sqr == x:
                return mid
            elif sqr < x:
                left = mid + 1
            else:
                right = mid - 1
        return (left + right) / 2           # This is so important
    # On the end, we can return right, or recalculate the mid, very important
```
-----

##[123. String to Integer atoi](https://oj.leetcode.com/problems/string-to-integer-atoi/)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

```python

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        N = len(str)
        if N == 0:
            return 0
        sign = 1
        res = 0
        imin, imax = -1<<31, (1<<31)-1
        for i, bit in enumerate(str):
            if i == 0 and bit in ['-', '+']:
                if bit == '-':
                    sign = -1
            elif bit.isdigit():
                res = res*10 + int(bit)
                if res * sign <= imin:
                    return imin
                elif res * sign >= imax:
                    return imax
            else:
                break
        return sign * res

    # Don't forget to check sign at the beginning
```
-----

##[124. Subsets](https://oj.leetcode.com/problems/subsets/)

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

```python

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        return self.subsets_1(S)

    # Iteration method
    def subsets_1(self, S):
        ret = [[]]
        for i in sorted(S):
            res = []
            for el in ret:
                res.append(el[:])
                el.append(i)
                res.append(el[:])
            ret = res[:]
        return ret

    # Recursion method
    def subsets_2(self, S):
        ret = []
        self.subsets_helper(0, sorted(S), [], ret)
        return ret

    def subsets_helper(self, i, S, res, ret):
        if i == len(S):
            ret.append(res[:])
            return
        self.subsets_helper(i+1, S, res, ret) # No element i
        res.append(S[i])
        self.subsets_helper(i+1, S, res, ret) # With element i
        res.pop()

    # Keep in mind the sorted
```
-----

##[125. Subsets II](https://oj.leetcode.com/problems/subsets-ii/)

Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

```python

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        return self.subsetsWithDup_2(S)

    # Iteration way
    def subsetsWithDup_1(self, S):
        ret = [[]]
        for i in sorted(S):
            res = []
            for el in ret:
                if len(el) == 0 or el[-1] != i: # Check len(el) == 0
                    res.append(el[:])           # if == 0 no el[-1]
                el.append(i)                    # if el[-1] != 1, then append(el[:])
                res.append(el[:])
            ret = res
        return ret

    # Recursion way
    def subsetsWithDup_2(self, S):
        ret = []
        self.subsetsWithDup_rec(0, sorted(S), [], ret)
        return ret

    def subsetsWithDup_rec(self, i, S, res, ret):
        if i == len(S):
            ret.append(res[:])
            return
        if len(res)==0 or S[i] != res[-1]: # This is tricky, but I should be careful, it's checking against
            self.subsetsWithDup_rec(i+1, S, res, ret) # last res char, but not S[i-1]
        res.append(S[i])
        self.subsetsWithDup_rec(i+1, S, res, ret)
        res.pop()
```
-----

##[126. Substring with Concatenation of All Words](https://oj.leetcode.com/problems/substring-with-concatenation-of-all-words/)

You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

```python

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        LS, LL, LL0 = len(S), len(L), len(L[0])
        did, ids, dl = {}, 0, {}
        for s in L:
            id = did.get(s, -1)
            if id == -1:
                 ids = ids + 1
                 id = ids
                 did[s] = id
            dl[id] = dl.get(id, 0) + 1

        pos, ans = [0] * LS, []
        for k, v in did.items():
            f = S.find(k)
            while f != -1:
                pos[f] = v
                f = S.find(k, f + 1)

        for sp in range(LL0):
            np, pp, tot, dt = sp, sp, 0, {}
            while np < LS:
                t = pos[np]
                if t == 0:
                    tot, dt = 0, {}
                    pp, np = np + LL0, np + LL0
                elif dt.get(t, 0) < dl[t]:
                    dt[t] = dt.get(t, 0) + 1
                    tot = tot + 1
                    if tot == LL:
                        ans.append(pp)
                    np = np + LL0
                else:
                    while pos[pp] != t:
                        tot = tot - 1
                        dt[pos[pp]] -= 1
                        pp = pp + LL0
                    pp = pp + LL0
                    dt[t] -= 1
                    tot = tot - 1
        return ans


        if len(S) == 0 or len(L) == 0:
            return []
        length = len(L[0])
        N = len(S)
        dp = [0 for i in range(N-length)]
        ret = 0
        for i in range(N-length):
            if S[i:length] in L:
                dp[i] = 1
                if i >= length and dp[i-length] > 0:
                    dp[i] += dp[i-length]
                ret = max(ret, dp[i])
        return ret

```
-----

##[127. Sudoku Solver](https://oj.leetcode.com/problems/sudoku-solver/)

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

```python

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.solve(board, 0, 0)

    def solve(self, board, i, j):
        i, j = self.getEmpty(board, i, j)
        if i == 9:                      # Set end point
            return True                 # These return valuse are very important
        fill = self.getPossibleInput(board, i, j)
        for f in fill:
            board[i] = board[i][:j] + [f] + board[i][j+1:] # Python string is imutable, but this is weird
            if self.solve(board, i, j):                    # in leetcode, don't know what is their input
                return True
        board[i] = board[i][:j] + ['.'] + board[i][j+1:]
        return False

    def getEmpty(self, board, i, j):
        while i < 9 and j < 9 and board[i][j] != '.':
            i += (j+1) / 9                  # This is so qiao miao
            j = (j+1) % 9
        return (i, j)

    def getPossibleInput(self, board, x, y):
        fill = [str(i+1) for i in range(9)] # Note the type here
        for i in range(9):
            if board[x][i] in fill:
                fill.remove(board[x][i])
            if board[i][y] in fill:
                fill.remove(board[i][y])
        start_x = x / 3 * 3
        start_y = y / 3 * 3
        for i in range(3):
            for j in range(3):
                if board[start_x+i][start_y+j] in fill:
                    fill.remove(board[start_x+i][start_y+j])
        return fill
```
-----

##[128. Sum Root to Leaf Numbers](https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/)

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

```
    1
   / \
  2   3
```
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sumNumbers_2(root)

    def sumNumbers_1(self, root):
        if root is None:
            return 0
        ret = [0]
        self.sumNumbers_helper(root, 0, ret)
        return ret[0]

    def sumNumbers_helper(self, root, res, ret):
        res = res * 10 + root.val
        if root.left is None and root.right is None: # Found a leaf node
            ret[0] += res
            return
        if root.left is not None:
            self.sumNumbers_helper(root.left, res, ret)
        if root.right is not None:
            self.sumNumbers_helper(root.right, res, ret)

    # Miracle to do this in one submit
    # Now think about a way to do this without using list[0]

    # Second way but this will reduce the check of root.left is None or root.right is None
    def sumNumbers_2(self, root):
        ret = [0]
        self.sumNumbers_2_helper(root, 0, ret)
        return ret[0]

    def sumNumbers_2_helper(self, root, res, ret):
        if root is None:
            return
        res = root.val + res * 10
        if root.left is None and root.right is None:
            ret[0] += res
            return
        self.sumNumbers_2_helper(root.left, res, ret)
        self.sumNumbers_2_helper(root.right, res, ret)
```
-----

##[129. Surrounded Regions](https://oj.leetcode.com/problems/surrounded-regions/)

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

```python

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0: # This is sooooo keng
            return board
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if i == 0 or i == M-1 or j == 0 or j == N-1:
                    self.bfs(board, i, j)
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def bfs(self, board, row, col):
        if (board[row][col] != 'O'):
            return
        q = []
        q.append((row, col))
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                continue
            if board[i][j] != 'O':
                continue
            board[i][j] = 'V'
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))

    # DFS will cause stack overflow
    def dfs(self, board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return
        if board[row][col] != 'O':
            return
        board[row][col] = 'V'
        self.dfs(board, row+1, col)
        self.dfs(board, row-1, col)
        self.dfs(board, row, col+1)
        self.dfs(board, row, col-1)

    # Note:
    # 1. For matrix/board problems, need to check if matrix/board == [], otherwise len(matrix[0]) will fail
    # 2. DFS may cause stack overflow
```
-----

##[130. Swap Nodes in Pairs](https://oj.leetcode.com/problems/swap-nodes-in-pairs/)

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        return self.swapPairs_3

    def swapPairs_1(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while head is not None and head.next is not None:
          current.next = head.next
          head.next = head.next.next
          current.next.next = head
          current = head
          head = head.next
        return dummy.next

    def swapPairs_2(self, head):
        if head.next is None or head.next.next is None:
            return
        move = head.next.next
        head.next.next = move.next
        move.next = head.next.next
        head.next = move
        self.swapPairs_2(move.next)

    def swapPairs_3(self, head):
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        first.next = second.next
        second.next = first
        first.next = self.swapPairs_3(first.next)
        return second
```
-----

##[131. Symmetric Tree](https://oj.leetcode.com/problems/symmetric-tree/)

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
```
Note:
Bonus points if you could solve it both recursively and iteratively.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        return self.isSymmetric_2(root)

    def isSymmetric_1(self, root):
        if root is None:
            return True
        return self.symmetric_helper(root.left, root.right)

    def symmetric_helper(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None or n1.val != n2.val:
            return False
        return self.symmetric_helper(n1.left, n2.right) and self.symmetric_helper(n1.right, n2.left)

    # No need to use two queues here, just one but pop twice would be fine
    # Keep in mind which node should be pop first
    def isSymmetric_2(self, root):
        if root is None:
            return True
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while len(queue)>0:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None or t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
```
-----

##[132. Text Justification](https://oj.leetcode.com/problems/text-justification/)

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

```python

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
```
-----

##[133. Trapping Rain Water](https://oj.leetcode.com/problems/trapping-rain-water/)

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

```python

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        N = len(A)
        if N == 0:
            return 0
        left_to_right = [0 for i in range(N)]
        right_to_left = [0 for i in range(N)]
        max_left = A[0]
        max_right = A[N-1]
        for i in range(N):
            max_left = max(max_left, A[i])
            left_to_right[i] = max_left
            max_right = max(max_right, A[N-1-i])
            right_to_left[N-1-i] = max_right
        water = 0
        for i in range(N):
            water += min(left_to_right[i], right_to_left[i]) - A[i] # Note here
        return water
```
-----

##[134. Triangle](https://oj.leetcode.com/problems/triangle/)

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

```python

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        M = len(triangle)
        N = len(triangle[-1])
        dp = [ [ 0 for j in range(N)] for i in range(M)]
        for i in range(M)[::-1]:
            for j in range(len(triangle[i])):
                if i == M-1:
                    dp[i][j] = triangle[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]
    # Notes:
    # This is not the best solution. But easier to understand
    # 1. status: ```dp[x][y]```表示从bottom走到top每个坐标的最短路径
    # 2. function: dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
    # 3. initialize: dp[-1][j] = triangle[-1][j]
    # 4. answer: dp[0][0]

    #This is older way, but still pretty good
    def minimumTotal_2(self, triangle):
        n = len(triangle) - 1
        dp = triangle[n]
        n -= 1
        while n >= 0:
            for i in range(n+1):
                dp[i] = triangle[n][i] + min(dp[i], dp[i+1])
            n -= 1
        return dp[0]

    # This look too simple
    # Understand of this:
    # 1. From bottom to top
    # 2. transfer func: dp[i] = triangle[n][i] + min(dp[i], dp[i+1])
    #    top level dp[i] = current triangle value + min(bottom level reachable dps)
```
-----

##[135. Two Sum](https://oj.leetcode.com/problems/two-sum/)

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

```python

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        return self.twoSum_3(num, target)

    # O(n^2)
    def twoSum_1(self, num, target):
        N = len(num)
        for i in range(N-1):
            for j in range(i+1, N):
                if target == num[i] + num[j]:
                    return (num[i], num[j])

    # O(n)
    def twoSum_2(self, num, target):
        num_map = {}
        for i, n in enumerate(num):
            if target - n not in num_map:
                num_map[n] = i
            else:
                return (num_map[target-n] + 1, i + 1) # Don't know why leetcode call the index [0] as 1

    # O(nlgn) This is the best way, used in X Sum
    def twoSum_3(self, num, target):
        d = {}                          # This is used because we need to sort the array
        for i, n in enumerate(num):
            d.setdefault(n, []).append(i+1)
        num = sorted(num)
        l = 0
        r = len(num) - 1
        while l < r:
            if num[l] + num[r]  == target:
                if num[l] == num[r]:
                    return (d[num[l]][0], d[num[r]][1])
                else:
                    return sorted((d[num[l]][0], d[num[r]][0]))
            elif num[l] + num[r] < target:
                l += 1
            else:
                r -= 1

    # Note:
    # 1. Keep in mind we need to use a dict to store the original position.
```
-----

##[136. Unique Binary Search Trees](https://oj.leetcode.com/problems/unique-binary-search-trees/)

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

```python

class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
```
-----

##[137. Unique Binary Search Trees II](https://oj.leetcode.com/problems/unique-binary-search-trees-ii/)

Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        nums = [ i for i in range(1, n+1)]
        return self.generateTrees_helper(nums)

    def generateTrees_helper(self, nums):
        if not nums:
            return [None]
        res = []
        for i, num in enumerate(nums):
            left = self.generateTrees_helper(nums[:i])
            right = self.generateTrees_helper(nums[i+1:])
            for l in left:
                for r in right:
                    root = TreeNode(num)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

    # Annie's DP way couldn't understand
```
-----

##[138. Unique Paths](https://oj.leetcode.com/problems/unique-paths/)

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

```python

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [ [0 for j in range(n)] for i in range(m) ]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    # Note:
    # 1. dp[i][j] means from (0,0) to (i, j) how many ways to finish
    # 2. init dp[i][0] = 1, dp[0][j] = 1
    # 3. dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 4. result dp[m-1][n-1]
```
-----

##[139. Unique Paths II](https://oj.leetcode.com/problems/unique-paths-ii/)

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

```python

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        dp = [ [0 for j in range(N)] for i in range(M) ]
        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[M-1][N-1]

    # Note:
    # Same to unique path I but more steps to initialize
```
-----

##[140. Valid Number](https://oj.leetcode.com/problems/valid-number/)

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

```python

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        if len(s.split('e')) > 2 or len(s.split('E')) > 2:
            return False

        if 'e' in s:
            return self.isNumberwoE_2(s.split('e')[0]) and self.isNumberwoE_2(s.split('e')[1], False)
        elif 'E' in s:
            return self.isNumberwoE_2(s.split('E')[0]) and self.isNumberwoE_2(s.split('E')[1], False)
        else:
            return self.isNumberwoE_2(s)

    def isNumberwoE_1(self, s, allow_digit = True):
        digit = '0123456789'
        N = len(s)
        if N == 0:
            return False
        has_digit = False
        has_num = False
        for i, char in enumerate(s):
            if char == '+' or char == '-':
                if i != 0:
                    return False
            elif char == ' ':
                return False
            elif char == '.':
                if not allow_digit or has_digit:
                    return False
                if (i == 0 or s[i-1] not in digit) and (i == N-1 or s[i+1] not in digit):
                    return False
                has_digit = True
            elif char not in digit:
                return False
            else:
                has_num = True
        return has_num

    def isNumberwoE_2(self, s, allow_digit = True):
        digit = '0123456789'
        has_num = False
        for i, char in enumerate(s):
            if i == 0 and char in ['+', '-']:
                continue
            if char == '.' and allow_digit:
                allow_digit = False
                if (i == 0 or s[i-1] in digit) or (i == len(s)-1 or s[i+1] in digit):
                    continue
            if char in digit:
                has_num = True
                continue
            return False
        return has_num

    # Note:
    # 1. Before/after e/E must be a valid num
    # 2. check each sign and dot and num and space
    # 3. Keep an eye on line 44 and line 61 using and / or. Reason is +.8 is valid.
    # 4. isNumberwoE_2 is easier to think, don't think reversely
```
-----

##[141. Valid Palindrome](https://oj.leetcode.com/problems/valid-palindrome/)

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

```python

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
    # 1. isalnum()
    # 2. lower()
    # 3. no need to check len at the begining
```
-----

##[142. Valid Parentheses](https://oj.leetcode.com/problems/valid-parentheses/)

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

```python

class Solution:
    # @return a boolean
    def isValid(self, s):
        bracket_dict = { '[' : ']',
                         '{' : '}',
                         '(' : ')',
                         }
        stack = []
        for bracket in s:
            if bracket in bracket_dict.keys():
                stack.append(bracket)
            elif len(stack) == 0 or bracket !=bracket_dict[stack.pop()]:
                return False
        return len(stack) == 0

    # Note return len(stack) == 0 not True!
```
-----

##[143. Valid Sudoku](https://oj.leetcode.com/problems/valid-sudoku/)

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

```python

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in row:
                    row.append(board[i][j])
                elif board[i][j] in row:
                    return False
                if board[j][i] != '.' and board[j][i] not in col:
                    col.append(board[j][i])
                elif board[j][i] in col:
                    return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                square = []
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] != '.' and board[i+x][j+y] not in square:
                            square.append(board[i+x][j+y])
                        elif board[i+x][j+y] in square:
                            return False
        return True
```
-----

##[144. Validate Binary Search Tree](https://oj.leetcode.com/problems/validate-binary-search-tree/)

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBST_1(root)

    def isValidBST_1(self, root):         # sys.maxint and -sys.maxint-1
        return self.isValidBST_helper_1(root, -9223372036854775808,  9223372036854775807)

    def isValidBST_helper_1(self, root, min, max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValidBST_helper_1(root.left, min, root.val) and self.isValidBST_helper_1(root.right, root.val, max)


This won't pass
    def isValidBST_2(self, root):
        return self.isValidBST_helper_2(root, -9223372036854775808)

    def isValidBST_helper_2(self, root, val):
        if root is None:
            return True
        if root.left is not None and not self.isValidBST_helper_2(root.left, val):
            return False
        if root.val <= val:
            return False
        val = root.val
        if root.right is not None and not self.isValidBST_helper_2(root.right, val):
            return False
        return True

```
-----

##[145. Wildcard Matching](https://oj.leetcode.com/problems/wildcard-matching/)

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false

```python

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        i = 0
        j = 0
        backupS = -1
        backupP = -1
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                while j < len(p) and p[j] == '*':
                    j += 1
                if j == len(p):
                    return True
                backupS = i
                backupP = j
            else:
                if backupS == -1:
                    return False
                i = backupS + 1
                backupS += 1
                j = backupP
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p) and i == len(s)


    def isMatch_helper(self, s, i1, p, i2):
        S = len(s)
        P = len(p)
        if i1 >= S and i2 >= P:
            return True
        elif i2 >= P:
            return False
        elif i1 >= S and p[i2] == '*':
            return self.isMatch_helper(s, i1, p, i2+1)
        elif p[i2] == '?':
            return self.isMatch_helper(s, i1+1, p, i2+1)
        elif p[i2] == '*':
            return self.isMatch_helper(s, i1+1)
```
-----

##[146. Word Break](https://oj.leetcode.com/problems/word-break/)

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

```python

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        return self.wordBreak_1(s, dict)

    def wordBreak_1(self, s, dict):
        N = len(s)
        dp = [False for i in range(N+1)]
        dp[0] = True
        for i in range(1, N+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break
        return dp[N]
    # Note:
    # 1. dp[i] means from first i-1 chars can be break
    # 2. dp[0] = True
    # 3. dp[i] = for j in (i-1, ... 0) if dp[j] and s[j:i] in dict
    # 4. dp[N] !!! Very important here it's N not N-1


    # Naive solution, won't pass
    def wordBreak_2(self, s, dict):
        N = len(s)
        if N == 0:
            return True

        for i in range(1, N+1):
            if s[:i] in dict and self.wordBreak(s[i:], dict):
                return True
        return False
```
-----

##[147. Word Break II](https://oj.leetcode.com/problems/word-break-ii/)

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

```python

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        ret = []
        dp = [True for i in range(len(s))]
        self.wordBreak_helper(0, s, dict, [], ret, dp)
        return ret

    def wordBreak_helper(self, start, s, dict, res, ret, dp):
        if start == len(s):
            ret.append(' '.join(res))
            return
        for i in range(start+1, len(s)+1):
            if s[start:i] in dict and dp[i-1]:
                res.append(s[start:i])
                beforeChange = len(ret)
                self.wordBreak_helper(i, s, dict, res, ret, dp)
                if beforeChange == len(ret):
                    dp[i-1] = False
                res.pop()

    # Use dp to reduce the duplicate
    # Another way is follow NC use divide and conquer
```
-----

##[148. Word Ladder](https://oj.leetcode.com/problems/word-ladder/)

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

```python
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
                for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in dict:
                            queue.append((new_word, depth+1))
                            dict.remove(new_word)
        return 0
```
-----

##[149. Word Ladder II](https://oj.leetcode.com/problems/word-ladder-ii/)

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

```python

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
```
-----

##[150. Word Search](https://oj.leetcode.com/problems/word-search/)

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

```python

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0] and self.isWord(board, i, j, 0, word):
                    return True
        return False

    def isWord(self, board, i, j, index, word):
        if index == len(word):
            return True

        M = len(board)
        N = len(board[0])

        if i < 0 or i >= M or j < 0 or j >= N or board[i][j] != word[index]:
            return False

        board[i][j] = '#'
        if self.isWord(board, i+1, j, index+1, word) or \
                self.isWord(board, i-1, j, index+1, word) or \
                self.isWord(board, i, j+1, index+1, word) or \
                self.isWord(board, i, j-1, index+1, word):
           return True

        board[i][j] = word[index]

        return False

    # Note:
    # 1. Keep in mind the declare of matrix, M, N, board, board[0]
    # 2. Line 28 check board[i][j] == word[0]
    # 3. Use in place make board[i][j] = '#' and recover later
    # 4. Line 43 line break use \
    # 5. Very important, must remark the 'visisted' part
```
-----

##[151. ZigZag Conversion](https://oj.leetcode.com/problems/zigzag-conversion/)

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

```python

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:    # Be careful about nRows ==1
            return s
        size = 2 * nRows - 2
        n = len(s) / size + 1
        res = []
        for i in range(size):
            if i == 0 or i == size / 2:
                for j in range(n):
                    if j * size + i < len(s):
                        res.append(s[j*size+i])
                if i == size/2:
                    return ''.join(res)
            else:
                for j in range(n):
                    if j * size + i < len(s):
                        res.append(s[j*size+i])
                    if (j+1) * size - i < len(s):
                        res.append(s[(j+1) * size - i])
```
-----

##152. Alternating Positive N Negative

or Rearrange Array Alternating Positive Negative Items
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance.

Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

Example:

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

Found online, also NC has marked this to high frequency

[Solution](http://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/)

```python

def rearrange_array(A):
    start  = 0
    while start < len(A) - 1:
        if start % 2 == 0 and A[start] > 0:
            i = start + 1
            while i < len(A) and A[i] >= 0:
                i += 1
            if i == len(A):
                break
            value = A[i]
            del A[i]
            A.insert(start, value)
        elif start % 2 == 1 and A[start] < 0:
            i = start + 1
            while i < len(A) and A[i] <= 0:
                i += 1
            if i == len(A):
                break
            value = A[i]
            del A[i]
            A.insert(start, value)
        start += 1
    return A

A = [1, 2, 3, -4, -1, 4]
print rearrange_array(A)
B = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print rearrange_array(B)
```
-----

##153. Consecutive Subarray

#####Interview With Cyan
1. Shortest Path
2. Consecutive Subarray

# Prob 2:
[1, 4, 20, 10, 3, 5, 9] # (20, 10, 3) Sum=33 Also the subarray must be consecutive
Note: All elements are positive integers exception: array can include 0
Note: You cannot sort the array
1
4
20

```python

# This is O(n^2)
def find_consecutive(num, sum):
    N = len(num)
    for i in range(N-1):
        cur_sum = 0
        for j in range(i, N):
            cur_sum += num[j]
            if cur_sum == sum:
                return (i, j)
            elif cur_sum > sum:
                break
    return -1

# This is O(n), very similar to KMP
def find_consecutive(num, sum):
    N = len(num)
    cur_sum = 0
    i = 0
    j = 0
    while j < N:
        if cur_sum + num[j] == sum:
            return num[i:j+1]
        elif cur_sum + num[j] < sum:
            cur_sum += num[j]
            j += 1
        else:
            cur_sum -= num[i]
            i += 1
    return -1

num = [9, 1, 4, 20, 10, 3, 5]
sum = 33
print find_consecutive(num, sum)
```
-----

##155. Delete a Node in BST

[Solution](http://answer.ninechapter.com/solutions/delete-a-node-in-binary-search-tree/)
实际上有好几种做法
1. replace current node with left maximum node
2. replace current node with right minimum node
3. 整体移动，前提是这个node只能有一边的subtree

这里就直接选第一种作为解法
但是这种也有特殊情况
1. no left subtree (只有一边有子树，简单，直接挪大块)
2. left maximum has a left child (不管有没有，都得把left child分配给max_node_parent，但是left maximum一定没有right child)
3. node is root of the tree (use dummy node)


```python
def delete_node(root, val):
    dummy_node = treeNode(0)
    dummy_node.left = root
    find_delete(dummy_node, root)
    return dummy_node.left

def find_delete(parent, node, val):
    if node is None:
        return
    if node.val == val:
        delete_node_in_BST(parent, node)
    elif node.val < val:
        find_delete(node, node.right, val)
    else:
        find_delete(node, node.left, val)

def delete_node_in_BST(parent, node):
    if not node.left:
        if parent.left == node:
            parent.left = node.right
        else:
            parent.right = node.right
    else:
        max_node_parent = node
        max_node = node.left

        while max_node.right:
            max_node_parent = max_node
            max_node = max_node.right

        # Found max_node and max_node_parent, need to replace max_node_parent a new child
        # max_node won't have a right child
        if max_node_parent.left == max_node:
            max_node_parent.left = max_node.left
        else:
            max_node_parent.right = max_node.right

        # Move max_node to node
        max_node.left = node.left
        max_node.right = node.right
        if parent.left == node:
            parent.left = max_node
        else:
            parent.right = max_node
```
-----

##158. Longest Common Subsequence

Need to distinguish from Longest Common Substring

Examples:
LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.

[Solution](http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/)

DP way is O(m*n)
Normal way O(m^2 *n)

1. dp[i][j] is LCS for first i chars of a and first j chars of b
2. dp[i][j] = 0
3. dp[i][j] = dp[i-1][j-1] + 1             # if a[i] == b[j]
            = max(dp[i-1][j], dp[i][j-1])  # if a[i] != b[j]
4. dp[M][N]

Keep reading for [print LCS](http://www.geeksforgeeks.org/printing-longest-common-subsequence/)

```python

def Longest_Common_Subsequence(a, b):
    M = len(a)
    N = len(b)
    dp = [ [0 for j in range(N+1)] for i in range(M+1)]

    for i in range(1, M+1):
        for j in range(1, N+1):
            if a[i-1] != b[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = dp[i-1][j-1] + 1

    return dp[M][N]

# Note
# 1. Very important, line 25 and 26 is range(1, X+1)

print Longest_Common_Subsequence('ABCDGH', 'AEDFHR')
print Longest_Common_Subsequence('AGGTAB', 'GXTXAYB')
print Longest_Common_Subsequence('B', 'B')
print '-'*10
# This is also correct, be we are storing all the results. So should do in dp way
def LCS_recur(a, b):
    if not a or not b:
        return 0
    if a[-1] == b[-1]:
        return 1 + LCS_recur(a[:-1], b[:-1])
    else:
        return max(LCS_recur(a[:-1], b), LCS_recur(a, b[:-1]))

print LCS_recur('ABCDGH', 'AEDFHR')
print LCS_recur('AGGTAB', 'GXTXAYB')
print LCS_recur('B', 'B')
print '-'*10

def LCS(a, b):
    M = len(a)
    N = len(b)
    dp = [ [0 for j in range(N+1)] for i in range(M+1)]

    for i in range(1, M+1):
        for j in range(1, N+1):
            if a[i-1] != b[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = dp[i-1][j-1] + 1

    res = []
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            res.insert(0, a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(res)

print LCS('ABCDGH', 'AEDFHR')
print LCS('AGGTAB', 'GXTXAYB')


                0       1       2       3       4       5       6       7
                Ø       M       Z       J       A       W       X       U
0       Ø       0       0       0       0       0       0       0       0
1       X       0       0       0       0       0       0       1       1
2       M       0       1       1       1       1       1       1       1
3       J       0       1       1       2       2       2       2       2
4       Y       0       1       1       2       2       2       2       2
5       A       0       1       1       2       3       3       3       3
6       U       0       1       1       2       3       3       3       4
7       Z       0       1       2       2       3       3       3       4

```
-----

##159. Longest Common Substring

##### 9/4/2014 Interview with Tubular
1. Subset(second le)
2. LCS

Given two strings 'X' and 'Y', find the length of the longest common substring.
For example, if the given strings are "GeeksforGeeks" and "GeeksQuiz",
the output should be 5 as longest common substring is "Geeks"

[Solution](http://www.geeksforgeeks.org/longest-common-substring/)

DP is O(n^2)
[Naive](http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/) way would be O(n * m^2), similar to KMP way
Which is for each word, we start search
str1 == substring of str2
Substring of str2 O(m^2)
search str1 O(n)
So O(n * m^2)



1. dp[i][j] is LCS of first i-1 chars in a ends with char i-1 and first j-1 chars in b ends with char j-1
2. init dp[i][j] = 0
3. dp[i][j] = dp[i-1][j-1] + 1 # if a[i] == b[j]
              0                # if a[i] != b[j]
4. max(dp[0...M][0...N])

```python

def Longest_Common_Substring(a,b):
    M = len(a)
    N = len(b)
    dp = [ [ 0 for j in range(N+1)] for i in range(M+1) ]
    res = (0, None)

    for i in range(1, M+1):
        for j in range(1, N+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > res[0]:
                    res = (dp[i][j], i)
            else:
                dp[i][j] = 0
    word = []
    i = res[1]
    for j in range(i-res[0], i):
        word.append(a[j])
    print word
    return res[0]

# "abcdefg"
print Longest_Common_Substring("abc", "abz")
print Longest_Common_Substring("abcdefgabyzzkabcde", "zzzzzzgabyzzabcabcdefg")
print Longest_Common_Substring("GeeksforGeeks", "GeeksQuiz")
```
-----

##160. Longest Increasing Subsequence

#####NC Class 5, slides 17

The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

[Solution](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)

1. dp[i] is length of LIS ends with char i
2. dp[0...N] = 1
3. dp[i] = for j in range(i): if A[j] <= A[i], max(dp[i], dp[j]+1)
4. dp[N-1]
5. O(n^2)

```python

def LIS(A):
    N = len(A)
    dp = [1 for i in range(N)]
    max_len = 1
    for i in range(1, N):
        for j in range(i)[::-1]:
            if A[j] <= A[i]:
                dp[i] = max(dp[i], dp[j]+1)
                max_len = max(max_len, dp[i])
    sequence = []
    for i in range(N)[::-1]:
        if dp[i] != max_len:
            continue
        else:
            sequence.insert(0, A[i])
            max_len -= 1
    print sequence
    return max_len

A = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print LIS(A)

# Using this can print one answer
# if need to print all, would rather do a dfs

def LIS(A):
    ret = {}
    LIS_helper(A, [], ret)
    return ret

def LIS_helper(A, res, ret):
    if not A:
        ret.setdefault(len(res[:]), []).append(res[:])
        return
    for i, num in enumerate(A):
        if not res or num > res[-1]:
            res.append(num)
            LIS_helper(A[i+1:], res, ret)
            res.pop()
A = [10, 22, 9, 33, 21, 50, 41, 60, 80]
d_A = LIS(A)

print d_A[max(d_A.keys())]
```
-----

##161. Lowest Common Ancestor

#####[LCA, Lowest Common Ancestor](http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/) Pocket Gem possible question 9/8/2014

Use O(n)

```python

# With Parent
def LCA(node1, node2):
    if node1 is None or node2 is None:
        return None
    path1 = get_path(node1)
    path2 = get_path(node2)

    index_1 = 0
    index_2 = 0
    while index_1 < len(path1) and index_2 < len(path2) and path1[index_1] == path2[index_2]:
        index1 += 1
        index2 += 1
    if index_1 < len(path1) and index_2 < len(path2):
        return path_1[index_1].parent
    else:
        return path_1[index_1 - 1]

    # Note:
    # 1. line 18 check if index is out of path:
    # if out of index: means node1/node2 is node2/node1's LCA, need to get index - 1
    # else:            we need to get parent

def get_path(node):
    path = []
    while node is not None:
        path.append(node)
        node = node.parent
    return path[::-1]

def get_path(root, node, current, path):
    if not root:
        return

    if root == node:
        path.append(current[:])
        return

    current.append(root)
    get_path(root.left, node, current, path)
    get_path(root.right, node, current, path)
    current.pop()

# Divdie and Conquer
def LCA(root, node1, node2):
    if not node1 or not node2:
        return None

    return get_LCA(root, node1, node2)

def get_LCA(root, node1, node2):
    if not root or node1 == root or node2 == root:
        return root

    left = get_LCA(root.left, node1, node2)
    right = get_LCA(root.right, node1, node2)

    if left and right:
        return root
    if left:
        return left
    if right:
        return right
    return None
```
-----

##163. Operations Calculation

##### 9/5/2014 Elasticbox
加减运算
```
string = '7 + 8 - 19 - 5 + 10'
8 - 19 - 5
```

```python

def get_result(str):
  N = len(str)
  ret = 0
  num = [0,1,2,3,4,5,6,7,8,9,]
  for i in range(N):
    if str[i] == ' ':
      continue
    if str[i] in num

-/+
str.split('+')

# 1. digit, check previous char, 1. digit, add it to new one   2. stop, this is a num
# 2. space, continue, don't care
# 3. operator, -, -num, +, +num
     sum(all number)

def get_result(str):
  plus = str.split('+')
  sum = 0
  minus = []
  for el in plus:
    try:
      num = int(el)
    except Error:
      minus.append(el)
    else:
      sum += num

  for el in minus:
    piece = el.split('-')
    result = piece[0]
    for i, num in enumerate(piece, 1):
      result
      if i == 0:
        sum += int(num)
      else:
        sum -= int(num)

  return sum

+8
find_next_num()
```
-----

##164. Print Numbers With Five

##### 9/7/2014 From [mitbbs](http://www.mitbbs.com/article_t/JobHunting/32651839.html) for Groupon
写一个function，对于参数n，输出从0到n之间所有含5的数字。
func(30) 应该输出5，15，25

```python

def find_five(n):
    ret = []
    helper(ret, [], n)
    return ret

def helper(ret, res, n):
    if len(res) > 0 and ( int(''.join(res)) > n or len(res) > len(str(n)) ):
        return
    if '5' in res and int(''.join(res)) not in ret:
        ret.append(int(''.join(res)))

    for i in range(10):
        res.append(str(i))
        helper(ret, res, n)
        res.pop()

print find_five(60)
```
-----

##170. Shortest Path

#####With Twitter & Cyan

2D array of characters
```
1 1 1 1 1
S 1 X 1 1
1 1 1 1 1
X 1 1 E 1
1 1 1 1 X
```

S is the starting point
E is the ending point
X means you cannot traverse to that point

1. Find if there is a path from S to E
2. Find the length of shortest path from S to E given the above matrix
3. Find the shortest path from S to E given the above matrix


Restriction: Move to 8 positions

```python

def find_path(map):
    M = len(map)
    N = len(map[0])
    S = None
    for i in range(M):
        if S:
            break
        for j in range(N):
            if map[i][j] == 'S':
                S = (i, j)
                break

    queue = [ ( S, [] ) ]

    while len(queue) > 0:
        current, path = queue.pop()
        x, y = current
        if x < 0 or y < 0 or x >= M or y >= N or map[x][y] == 'X':
            continue

        path.append(current)
        if map[x][y] == 'E':
            return path        # Or len(path) for question 2

        map[x][y] = 'X'        # Mark as visited

        queue.insert(0, ((x-1, y-1), path[:]))
        queue.insert(0, ((x-1, y  ), path[:]))
        queue.insert(0, ((x-1, y+1), path[:]))
        queue.insert(0, ((x  , y-1), path[:]))
        queue.insert(0, ((x  , y+1), path[:]))
        queue.insert(0, ((x+1, y-1), path[:]))
        queue.insert(0, ((x+1, y  ), path[:]))
        queue.insert(0, ((x+1, y+1), path[:]))

    return None

map = [ ['1', '1', '1', '1', '1',],
        ['S', '1', 'X', '1', '1',],
        ['1', '1', '1', '1', '1',],
        ['X', '1', '1', 'E', '1',],
        ['1', '1', '1', '1', 'X',],
        ]

print find_path(map)

# 讨论
# 1. 无论用何种方法，最好的复杂度应该都是O(m*n)因为最坏情况都是要遍历完整个图
# 2. 但是单就最好情况来说，想讨论下有没有更好的方法，主要考虑如下：
#    因为实际已知 S 和 E 的坐标，这里用到的BFS实际是和不知道终点位置是一样的，都是BFS最先的情况就是答案
#    但我觉得方法应该是可以向着终点方向走，遇到障碍让开走，如果能够实现这种方法，肯定是最优的解法，
#    希望大家能给我点思路

# 用DFS是没有意义的，因为最后的结果是你怎么都得遍历整个图
```
-----

##171. Shuffle

###Shuffle a given array
Saw it from FiveStar's interview.

Solution is from Geeksforgeesk
Fisher-Yates shuffle Algorithm works in O(n) time complexity.

```python

def shuffle_array(A):
    from random import random
    N = len(A)
    for i in range(N):
        random_num = int(random() * (N-i))
        A[N-i-1], A[random_num] = A[random_num], A[N-i-1]
    return A


A = [ i + 1 for i in range(52)]

print shuffle_array(A)

# Note
# 1. from random import random
# 2. from random import randint. randint(start, end), include start and end
```
-----

##172. isOneEditDistance

From [mitbbs](http://www.mitbbs.com/article_t/JobHunting/32760941.html) for facebook

```python

def is_one_edit_distance(s1, s2):
    M = len(s1)
    N = len(s2)
    if abs(M-N) >= 2:
        return False
    if M != N:
        if M > N:
            longer = s1
            shorter = s2
        else:
            longer = s2
            shorter = s1
        i = 0
        j = 0
        counter = 0
        while i < len(shorter) and j < len(shorter):
            if longer[i] != shorter[j]:
                j += 1
                counter += 1
            else:
                i += 1
                j += 1
            if counter > 1:
                return False
        return True

    else:
        counter = 0
        for i in range(M):
            if s1[i] != s2[i]:
                counter += 1
                if counter > 1:
                    return False
        return True
```
-----


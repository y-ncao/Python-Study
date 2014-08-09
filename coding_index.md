## Coding Summary by Keywords and Type

####Permutation & Combination Type
* [x] Permutations
* [x] Permutations II
* [x] Next Permutation
* [x] Permutation Sequence

----

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
* [ ] Longest Valid Parentheses

-----

* [x] Palindrome Number
* [x] Valid Palindrome
* [ ] Palindrome Partitioning
* [ ] Palindrome Partitioning II

####Tree Traversal
* [x] Binary Tree Inorder Traversal
* [x] Binary Tree Preorder Traversal
* [x] Binary Tree Postorder Traversal
* [x] Binary Tree Level Order Traversal
* [x] Binary Tree Level Order Traversal II
* [x] Binary Tree Zigzag Level Order Traversal

____

* [x] Construct Binary Tree from Preorder and Inorder Traversal (Redo)
* [x] Construct Binary Tree from Inorder and Postorder Traversal (Redo)

----

* [x] Same Tree
* [x] Balanced Binary Tree
* [x] Symmetric Tree
* [x] Maximum Depth of Binary Tree
* [x] Minimum Depth of Binary Tree

####Binary Search Tree
* [x] Convert Sorted Array to Binary Search Tree
* [x] Unique Binary Search Trees
* [x] Unique Binary Search Trees II
* [x] Validate Binary Search Tree (Redo)
* [x] Recover Binary Search Tree (Redo)

####类Tree(以tree作为Data Structure的题目)
* [x] Path Sum
* [x] Path Sum II
* [x] Populating Next Right Pointers in Each Node
* [x] Populating Next Right Pointers in Each Node II
* [x] Sum Root to Leaf Numbers
* [x] Flatten Binary Tree to Linked List
* [x] Binary Tree Maximum Path Sum

####Array(意义不大)
* [x] Maximum Subarray
* [x] Convert Sorted Array to Binary Search Tree
* [x] Merge Sorted Array
* [x] Remove Duplicates from Sorted Array
* [x] Remove Duplicates from Sorted Array II
* [x] Search in Rotated Sorted Array
* [x] Search in Rotated Sorted Array II
* [ ] Median of Two Sorted Arrays

* [x] Remove Element

####List(意义不大)
* [x] Linked List Cycle
* [x] Linked List Cycle II
* [x] Remove Duplicates from Sorted List
* [x] Remove Duplicates from Sorted List II
* [x] Merge Two Sorted Lists
* [x] Remove Nth Node From End of List
* [x] Partition List
* [x] Reverse Linked List II (Why only II??)
* [ ] Insertion Sort List (Insertion Sort)
* [ ] Copy List with Random Pointer
* [x] Merge k Sorted Lists
* [x] Rotate List
* [ ] Sort List (Merge Sort)
* [ ] Reorder List

######Dup with tree
* [x] Flatten Binary Tree to Linked List
* [x] Convert Sorted List to Binary Search Tree

####Matrix
* [x] Search a 2D Matrix
* [ ] Spiral Matrix
* [x] Spiral Matrix II
* [x] Set Matrix Zeroes
* [x] Valid Sudoku
* [ ] Sudoku Solver

####Play With Math
* [x] Reverse Integer
* [x] Roman to Integer
* [x] Intger to Roman
* [x] Pascal's Triangle
* [x] Pascal's Triangle II

####Dynamic Programming
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
* [ ] Edit Distance
* [ ] Distinct Subsequences
* [ ] Maximal Rectangle
* [ ] Longest Palindromic Substring
* [ ] Scramble String
* [ ] Palindrome Partitioning II
* [ ] Interleaving String
* [ ] Word Break
* [ ] Decode Ways

####Cannot Classify(记住思路)
* [x] Search Insert Position
* [x] Container With Most Water (In Two pointers)
* [x] Count and Say
* [x] Implement strStr() (KMP)

####Not Sure Yet
* [x] 3Sum Closest
* [ ] 4Sum
* [ ] Two Sum
* [ ] 3Sum

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


##### Below Two Looks Similar, seems all use DFS
* Palindrome Partitioning
* Binary Tree Maximum Path Sum

Not good, seems I need to redo every questions AC rate below 25%

##Still Cannot Understand
* Edit Distance
* Distinct Subsequences(I'm too bad at DP, need to find out a way to understand these)

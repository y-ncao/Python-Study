## Coding Summary by Keywords and Type

####Permutation & Combination Type
* Permutations
* Permutations II
* Next Permutation
* Permutation Sequence

----

* Combinations
* Combination Sum
* Combination Sum II
* Letter Combination of a Phone Number

-----

######Note:
做Permutation的感觉和做Combination的感觉非常像，注意

1. 结束条件都是用完所有可用的char, 也就是i == len(n). 然后在ret.append(res[:]), 这里千万别忘了要return cancel函数
2. 做for循环的时recursion函数的输入会有差别(记得这里用enumerate会方便好多)
  1. Permutation传入剩余num_list 是 num[:i] + num[i+1], 因为只是除去当前数字, permute剩余
  2. Combination传入剩余num_list 是 num[i+1:],  因为除去比当前数字之前的数, combine剩余
  3. 两者相同的地方都是
    1. res.append(n)
    2. do combine_rec/permute_rec
    3. res.pop()


-----

* Gray Code

-----

* Subset
* Subset II

-----

* Generate Parentheses
* Valid Parentheses
* Longest Valid Parentheses

-----

* Palindrome Number
* Valid Palindrome
* Palindrome Partitioning
* Palindrome Partitioning II

####Tree Traversal
* Binary Tree Inorder Traversal
* Binary Tree Preorder Traversal
* Binary Tree Postorder Traversal
* Binary Tree Level Order Traversal
* Binary Tree Level Order Traversal II
* Binary Tree Zigzag Level Order Traversal

____

* Construct Binary Tree from Preorder and Inorder Traversal
* Construct Binary Tree from Inorder and Postorder Traversal

----

* Same Tree
* Balanced Binary Tree
* Symmetric Tree
* Maximum Depth of Binary Tree
* Minimum Depth of Binary Tree

####Binary Search Tree
* Convert Sorted Array to Binary Search Tree
* Unique Binary Search Trees
* Unique Binary Search Trees II
* Validate Binary Search Tree
* Recover Binary Search Tree

####类Tree(以tree作为Data Structure的题目)
* Path Sum
* Path Sum II
* Populating Next Right Pointers in Each Node
* Populating Next Right Pointers in Each Node II
* Sum Root to Leaf Numbers
* Flatten Binary Tree to Linked List
* Binary Tree Maximum Path Sum

####Array(意义不大)
* Maximum Subarray
* Convert Sorted Array to Binary Search Tree
* Merge Sorted Array
* Remove Duplicates from Sorted Array
* Remove Duplicates from Sorted Array II
* Search in Rotated Sorted Array
* Search in Rotated Sorted Array II
* Median of Two Sorted Arrays

####List(意义不大)
* Linked List Cycle
* Linked List Cycle II
* Remove Duplicates from Sorted List
* Remove Duplicates from Sorted List II
* Merge Two Sorted Lists
* Remove Nth Node From End of List
* Partition List
* Reverse Linked List II(Why only II??)
* Insertion Sort List
* Copy List with Random Pointer
* Merge k Sorted Lists
* Rotate List
* Sort List
* Reorder List

######Dup with tree
* Flatten Binary Tree to Linked List
* Convert Sorted List to Binary Search Tree

####Matrix
* Search a 2D Matrix
* Spiral Matrix
* Spiral Matrix II
* Set Matrix Zeroes

####Dynamic Programming
* Climbing Stairs
* Minimum Path Sum

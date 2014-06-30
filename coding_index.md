##Two pointers
###[]Start -> End
* Implement strStr()
* Longest Substring Without Repeating Characters
* Minimum Window Substring
* Remove Duplicates from Sorted Array I & II
* Remove Duplicates from Sorted List I & II
* Remove Element
* Remove Nth Node From End of List
* Reverse Linked Llist II
* Rotate List
* Substring with Concatenation of All Words
* Swap Nodes in Pairs

###[]Sides -> Mid
* 3Sum
* 3Sum Closest
* 4Sum
* Container With Most Water
* Sort Colors
* Trapping Rain Water
* Two Sum
* Binary search (will discuss it in a separate section)

### []Separated
* Add Binary
* Add Two Numbers
* Merge Sorted Array
* Merge Two Sorted Lists
* Multiply Strings
* Partition List

##[]Permutation and Combination
Permutation
* 输入没有重复：Permutations, CC150 9.5, PIE Chapter7 Permutations of a String
* 输入有重复，输出不能有重复：Permutations II
* Next Permutation: 经典算法，背吧
* Permutation Sequence: 非常有意思的题目
* Combination
纯粹的subset
* 输入没有重复：Subsets, CC150 9.4, PIE Chapter7 Combinations of a String
* 输入有重复，输出不能有重复：Subsets II
需要满足一定要求的组合
* 一个元素只能取一次(输入没有重复): Combinations
* 一个元素可以取多次(输入没有重复): Combination Sum, CC150, 9.8
* 一个元素只能取一次(输入有重复，输出不能有重复）:
* Combination Sum II
* Gray Code: 具有subset的序列特点 （考虑CC150 9.4 Solution#2: Combinatorics)

##[]Binary search and divide and conquer

Binary search非常tricky，虽说道理简单，但是面试的时候却很容易出bug，因此总结一下是必须的。假设i=0,j=A.length-1, 我做了一下LeetCode上的所有binary search的题目，发现了以下几点值得注意。

* 终止条件不同 i<=j, i<j
* mid的上下取向不同 i+(j-i)/2, j-(j-i)/2
* 如何合理分半
* 分半的时候取=mid, mid-1, or mid+1

* Search a 2D Matrix： 这是一道普通的binary search。终止条件i<=j, mid取向i+(j-i)/2, 分半的时候=mid-1 or mid+1。
* Search for a Range：这道题需要终止条件i<j, mid取向两种都需要用到，分半的时候需要用到=mid。我发现一般＝mid的时候，终止条件往往是i<j,不然会有死循环。

如何合理分半：下边这几道题都很tricky，分半的时候都有各自的特点，很不容易一次写对。需要多多练习和体会。
* Search in Rotated Sorted Array
* Search in Rotated Sorted Array II
* Median of Two Sorted Arrays

还有一个有趣的现象就是很多数学相关的题目也是通过binary search来解决的：
* Divide Two Integers：这题没做过面试也容易跪
* Pow(x, n)
* Sqrt(x)：其实算是一道典型的binary search题目，不过里边包括了几个tricky的地方，很难一次写对

##[]Linked List
首先LeetCode上几乎所有的Linked list的题目都可以用two pointers来解决，或者会用到two pointers这个基本编程技巧。因此two pointers跟linked list是紧密相关的。因为two pointers以前已经总结过了，就不多讲了。
其次，因为LinkedList和Array/ArrayList一样都具备有List的特性，因此很多题目都出现在了两种数据结构上，或者说很多题目都是可以把这两种数据结构互换的。比如：
* Add Two Numbers
* Convert Sorted List to Binary Search Tree
* Insert Interval
* Merge Intervals
* Merge k Sorted Lists
* Merge Two Sorted Lists
* Remove Duplicates from Sorted List
* Remove Duplicates from Sorted List II
第三，LinkedList的题目大多自然而然使用iteration来解决的，但是我发现有些时候iteration比较容易出bug，换成recursion实现更容易。面试的时候万一iteration卡住可以换换recursion的思路。
第四，dummy head非常有用，可以使代码简洁很多，并且容易写bug free的code。这个技巧可以大量使用。
第五，今天做了一遍LinkedList的题目，发现两个地方容易出bug。一是two pointers
loop完之后常常会有一个收尾的工作，比如Add Two Numbers需要处理carrier>0的情况。二是在swap了nodes之后，新的tail需要把next置
空，不然就出现死循环了。

##[]Tree
1. Recursive DFS
2. Iterative DFS
3. BFS

有些tree的题目比较tricky一些，但是最终解法还是逃不出这三个套路，所以我觉得面试的时候代码的质量就变得更加的重要了。因为没有什么太多总结的，下边就随便聊一下了。

Leetcode上graph的题目涉及的很少，不过从算法和coding来说DFS，BFS完全适用于tree和graph。因此，把tree的题目练好了，graph的多数题目应该也不会有什么问题才对。当然graph涉及的算法比tree还是要多的，比如shortest path,toposort等等，但是DFS,BFS还是基本中的基本。因此做Leetcode上的tree的题目也相当于练习了graph的题目了。

由于Tree的题目比较多，我感觉一些可以skip掉，如果时间不充裕的话。或者做一遍即可，不需要反复练习。这些题目或者太简单，或者面试不太可能碰到。

* Balanced Binary Tree
* Binary Tree Level Order Traversal II
* Maximum Depth of Binary Tree
* Minimum Depth of Binary Tree
* Same Tree
* Symmetric Tree
* Unique Binary Search Trees
* Unique Binary Search Trees II
* Pre-order, In-order, Post-order traversal
需要会recursive和iterative的两种实现方式。可惜Leetcode上只包含了In-order，有
* 些遗憾。
* Tree的serialization/deserialization也是常常被考到的题目，这个Leetcode目前还没有包含，当然套路还是DFS/BFS。
* LinkedList和Binary Tree相互转换的题目。
* Convert Sorted List to Binary Search Tree
* Flatten Binary Tree to Linked List
(这题原题在CC150是一道双向链表题，不知道Leetcode上怎么改单向了。双向链表应该更复杂一些，大家要注意一下）


##[]数据结构
* Array, ArrayList
* String, StringBuffer
* LinkedList
* HashMap, HashSet
* Stack and Queue
* Tree:
* BT: binary tree
* BST: binary search tree,
* Balanced BST (red-black tree): TreeMap, TreeSet
* Trie: prefix tree
* Heap: PriorityQueue
* Grpah


Thanks to http://www.mitbbs.com/article_t/JobHunting/32564237.html

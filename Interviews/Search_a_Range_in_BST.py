"""
or Print BST Keys in the Give Range

Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Print all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST. Print all the keys in increasing order.

[Solution](http://www.geeksforgeeks.org/print-bst-keys-in-the-given-range/)


"""

def search_a_range(root, k1, k2):
    if root is None:
        return

    if root.val > k1:
        search_a_range(root.left, k1, k2)

    if k1 <= root.val <= k2:
        print root.val

    if root.val < k2:
        search_a_range(root.right, k1, k2)

    # Note:
    # 1. in line 15 and line 21, using > < instead of >= <= because
    #    if k1 == root.val, no needs to check it's child since this is the left bound in it's tree

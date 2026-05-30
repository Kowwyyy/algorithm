# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        curr = root
        while curr:
            small, big = min(p.val, q.val), max(p.val, q.val)
            if small > curr.val:
                curr = curr.right
            elif big < curr.val:
                curr = curr.left
            else:
                return curr
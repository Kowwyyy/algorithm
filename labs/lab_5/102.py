# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        levels = []

        def traverse(curr, depth):
            if curr is None:
                return
            if len(levels) == depth:
                levels.append([])
            levels[depth].append(curr.val)
            traverse(curr.left, depth + 1)
            traverse(curr.right, depth + 1)

        traverse(root, 0)
        return levels
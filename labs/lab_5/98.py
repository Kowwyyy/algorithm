# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def check(curr, mn=None, mx=None):
            if curr is None:
                return True
            if mn is not None and curr.val <= mn:
                return False
            if mx is not None and curr.val >= mx:
                return False
            left_ok = check(curr.left, mn, curr.val)
            right_ok = check(curr.right, curr.val, mx)
            return left_ok and right_ok

        return check(root)
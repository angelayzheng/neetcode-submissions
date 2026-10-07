# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root) != -1

    def isBalancedHelper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        l = self.isBalancedHelper(root.left)
        r = self.isBalancedHelper(root.right)

        if l == -1 or r == -1 or abs(l - r) >= 2:
            return -1

        else:
            return max(l, r) + 1
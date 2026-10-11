# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diameter: int

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.height(root)
        return self.max_diameter

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = self.height(root.left)
        r = self.height(root.right)

        self.max_diameter = max(self.max_diameter, l + r)

        return 1 + max(l, r)
     
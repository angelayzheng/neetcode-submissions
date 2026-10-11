# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None and subRoot is not None:
            return False

        return self.equals(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def equals(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        elif root is None and subRoot is not None:
            return False

        elif subRoot is None:
            return False

        if root.val != subRoot.val:
            return False

        return self.equals(root.left, subRoot.left) and self.equals(root.right, subRoot.right)

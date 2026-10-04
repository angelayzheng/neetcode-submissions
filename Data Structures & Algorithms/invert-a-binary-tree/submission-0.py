# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invertTreeMutate(root)
            return root

        return None

    def invertTreeMutate(self, root: TreeNode) -> None:
        root.left, root.right = root.right, root.left

        if root.left:
            self.invertTreeMutate(root.left)
        
        if root.right:
            self.invertTreeMutate(root.right)

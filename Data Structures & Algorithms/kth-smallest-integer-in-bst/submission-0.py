# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.kthSmallestHelper(root, k, 0)[0]
        
    def kthSmallestHelper(self, root: Optional[TreeNode], k: int, count: int) -> tuple[int, bool]:

        if root is None:
            return count, False

        count, found = self.kthSmallestHelper(root.left, k, count)

        if found:
            return count, True

        if k == count + 1:
            return root.val, True

        return self.kthSmallestHelper(root.right, k, count + 1)
        
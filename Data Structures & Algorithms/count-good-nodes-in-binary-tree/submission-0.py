# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.good(root, root.val)

    def good(self, curr: TreeNode, max_so_far: int) -> int:
        if curr is None:
            return 0

        if curr.left is None and curr.right is None and curr.val >= max_so_far:
            return 1

        count = 0

        if curr.val >= max_so_far:
            max_so_far = curr.val
            count = 1

        count += self.good(curr.left, max_so_far)
        count += self.good(curr.right, max_so_far)
        return count

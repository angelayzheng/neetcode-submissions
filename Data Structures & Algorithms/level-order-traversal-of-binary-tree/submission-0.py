# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.order(root, result, 0)

        return result

    def order(self, root: Optional[TreeNode], result: List[List[int]], depth: int) -> None:

        if root is None:
            return

        if depth >= len(result):
            result.append([root.val])

        else:
            result[depth].append(root.val)

        self.order(root.left, result, depth + 1)
        self.order(root.right, result, depth + 1)

#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.val} -> {self.left} -> {self.right}"


# @lc code=start
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.last_val = 0
        self.normalize_tree(root)

        return root

    def __init__(self) -> None:
        self.last_val = 0

    def normalize_tree(self, root: Optional[TreeNode]):
        if not root:
            return 0

        if root.right is not None:
            self.normalize_tree(root.right)

        root.val += self.last_val
        self.last_val = root.val

        if root.left is not None:
            self.normalize_tree(root.left)


# @lc code=end

if __name__ == "__main__":
    root = TreeNode(0, right=TreeNode(1))

    s = Solution()
    s.convertBST(root)

    print(root)

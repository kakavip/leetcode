#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start

from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(
        self, root: Optional[TreeNode], values: List[int] = []
    ) -> List[str]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return ["->".join(map(str, values + [root.val]))]

        return self.binaryTreePaths(
            root.left, values + [root.val]
        ) + self.binaryTreePaths(root.right, values + [root.val])


# @lc code=end

if __name__ == "__main__":
    root = TreeNode(1)
    root = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3))

    s = Solution()

    print(s.binaryTreePaths(root))

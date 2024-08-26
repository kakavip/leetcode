#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        if not root:
            return result

        if root.left:
            result.extend(self.postorderTraversal(root.left))
        if root.right:
            result.extend(self.postorderTraversal(root.right))
        result.append(root.val)

        return result


# @lc code=end

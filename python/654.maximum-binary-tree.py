#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

from typing import List, Optional


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


def gen_tree_node(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    _max = max(nums)
    _max_idx: int = nums.index(_max)

    root = TreeNode(_max)
    if nums[:_max_idx]:
        root.left = gen_tree_node(nums[:_max_idx])
    if nums[_max_idx + 1 :]:
        root.right = gen_tree_node(nums[_max_idx + 1 :])

    return root


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return gen_tree_node(nums)


# @lc code=end

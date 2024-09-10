#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
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
from typing import List, Optional


class Solution:
    def _gen_one(self, a: int) -> List[TreeNode]:
        return [TreeNode(a)]

    def _gen_two(self, a: int, b: int) -> List[TreeNode]:
        return [TreeNode(a, right=TreeNode(b)), TreeNode(b, left=TreeNode(a))]

    def gen_tree(self, arr: List[int]):
        if len(arr) == 0:
            return []

        if len(arr) == 1:
            return self._gen_one(arr[0])

        if len(arr) == 2:
            return self._gen_two(*arr)

        result: List[TreeNode] = []
        for i in range(len(arr)):
            _pre = self.gen_tree(arr[:i])
            _next = self.gen_tree(arr[i + 1 :])

            if _pre:
                for j in _pre:
                    if _next:
                        for k in _next:
                            result.append(TreeNode(arr[i], j, k))
                    else:
                        result.append(TreeNode(arr[i], left=j))
            elif _next:
                for k in _next:
                    result.append(TreeNode(arr[i], right=k))
            else:
                result.append(TreeNode(arr[i]))

        return result

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.gen_tree([i + 1 for i in range(n)])


# @lc code=end

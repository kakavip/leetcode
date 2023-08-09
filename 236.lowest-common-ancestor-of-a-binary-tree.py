#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import Tuple


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        return self.checkNodesRecurring(root, p, q)[0]

    def checkNodesRecurring(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Tuple[TreeNode, bool, bool]:
        if not root:
            return None, False, False

        b_node: TreeNode
        b_node, b_has_1, b_has_2 = None, False, False
        if root.val in [p.val, q.val]:
            b_node, b_has_1, b_has_2 = root, False, False

        # l_has, r_has = False, False
        (l_node, l_has_1, l_has_2) = self.checkNodesRecurring(root.left, p, q)
        if l_node and not (l_has_1 or l_has_2):
            l_has_1, l_has_2 = True, False
        if l_has_1 and l_has_2:
            return l_node, l_has_1, l_has_2

        (r_node, r_has_1, r_has_2) = self.checkNodesRecurring(root.right, p, q)
        if r_node and not (r_has_1 or r_has_2):
            r_has_1, r_has_2 = False, True
        if r_has_1 and r_has_2:
            return r_node, r_has_1, r_has_2

        if r_node and l_node:
            return root, True, True

        if b_node:
            if l_node or r_node:
                return b_node, True, True
            else:
                return b_node, False, False
        else:
            if l_node or r_node:
                return l_node or r_node, False, False

        return None, False, False

        # if root.right:
        #     r_has = self.checkNodesRecurring(root.right, p, q)

        # # check left node
        # if l_has and r_has:
        #     return root
        # if not (l_has or r_has):
        #     return None
        # if l_has:
        #     return self.checkNodesRecurring(root.left, p, q)
        # if r_has:
        #     return self.checkNodesRecurring(root.right, p, q)

        # return None


# @lc code=end

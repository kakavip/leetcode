#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
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
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # left_nodes: List[TreeNode] = [root]
        base_nodes: List[TreeNode] = [root]
        while True:
            n_nodes: List[TreeNode] = []
            # l_nodes: List[TreeNode] = []

            for b_node in base_nodes:
                if b_node is None:
                    continue

                b_node.left and n_nodes.append(b_node.left)
                b_node.right and n_nodes.append(b_node.right)

                # b_node.left and l_nodes.append(b_node.left)

            if not n_nodes:
                break

            base_nodes.clear()
            base_nodes.extend(n_nodes)

            # if l_nodes:
            #     left_nodes.clear()
            #     left_nodes.extend(l_nodes)

        return base_nodes[0].val


# @lc code=end

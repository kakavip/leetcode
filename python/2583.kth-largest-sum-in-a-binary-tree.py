#
# @lc app=leetcode id=2583 lang=python3
#
# [2583] Kth Largest Sum in a Binary Tree
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
import heapq
from typing import List, Optional


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        sum_layers: List[int] = []

        c_nodes: List[TreeNode] = [root]
        while c_nodes:
            _sum: int = 0
            n_nodes: List[TreeNode] = []
            for node in c_nodes:
                if node.left:
                    n_nodes.append(node.left)
                if node.right:
                    n_nodes.append(node.right)

                _sum += node.val

            heapq.heappush(sum_layers, -_sum)
            c_nodes.clear()
            c_nodes = n_nodes

        if len(sum_layers) < k:
            return -1

        while k > 1:
            heapq.heappop(sum_layers)
            k -= 1

        # print(sum_layers)
        return -heapq.heappop(sum_layers)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.kthLargestLevelSum(TreeNode(1, TreeNode(2, TreeNode(3))), 1) == 3)

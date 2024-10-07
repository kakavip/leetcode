#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
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

from typing import List, Optional, Tuple


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def consider_rob(root: Optional[TreeNode]) -> Tuple[int, int]:
            if not root:
                return (0, 0)

            left_rob, right_rob = consider_rob(root.left), consider_rob(root.right)

            _root_rob: int = root.val + left_rob[1] + right_rob[1]
            _not_root_rob: int = max(left_rob) + max(right_rob)
            return (_root_rob, _not_root_rob)

        return max(consider_rob(root))


# @lc code=end

if __name__ == "__main__":
    s = Solution()

    a = TreeNode(
        3,
        left=TreeNode(2, right=TreeNode(3)),
        right=TreeNode(3, right=TreeNode(1)),
    )

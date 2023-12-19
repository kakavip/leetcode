#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

from typing import Optional, List


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
    def __init__(self) -> None:
        self.fre_sum_map = {}
        self.max_fre = 0
        self.fre_count_map = {}

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None

        self.calc_sum_root(root)
        return self.fre_count_map[self.max_fre]

    def _up_fre_sum(self, _sum: int):
        if _sum not in self.fre_sum_map:
            self.fre_sum_map[_sum] = 0
        self.fre_sum_map[_sum] += 1

        count = self.fre_sum_map[_sum]
        if count not in self.fre_count_map:
            self.fre_count_map[count] = []
        self.fre_count_map[count].append(_sum)
        if count > self.max_fre:
            self.max_fre = count

    def calc_sum_root(self, root: Optional[TreeNode]):
        if not root:
            return 0
        _sum: int = root.val
        _sum += self.calc_sum_root(root.left)
        _sum += self.calc_sum_root(root.right)

        setattr(root, "_sum", _sum)

        self._up_fre_sum(_sum)
        return _sum


# @lc code=end

if __name__ == "__main__":
    root = TreeNode(5, left=TreeNode(14, left=TreeNode(1)))

    s = Solution()
    print(s.findFrequentTreeSum(root))

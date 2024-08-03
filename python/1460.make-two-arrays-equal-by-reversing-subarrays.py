#
# @lc app=leetcode id=1460 lang=python3
#
# [1460] Make Two Arrays Equal by Reversing Subarrays
#

# @lc code=start
from typing import Dict, List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)


# @lc code=end

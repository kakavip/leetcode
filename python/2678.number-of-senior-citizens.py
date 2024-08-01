#
# @lc app=leetcode id=2678 lang=python3
#
# [2678] Number of Senior Citizens
#
from typing import List


# @lc code=start
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len(list(filter(lambda x: int(x[-4:-2]) > 60, details)))


# @lc code=end

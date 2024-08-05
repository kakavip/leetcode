#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#

# @lc code=start
from typing import Dict, List


class Solution:
    distinct_cache: Dict[str, int] = {}

    def kthDistinct(self, arr: List[str], k: int) -> str:
        self.distinct_cache.clear()

        for v in arr:
            if v not in self.distinct_cache:
                self.distinct_cache[v] = 0

            self.distinct_cache[v] += 1

        result = ""
        for v in arr:
            if self.distinct_cache[v] == 1:
                k -= 1

                if k <= 0:
                    result = v
                    break
        return result


# @lc code=end

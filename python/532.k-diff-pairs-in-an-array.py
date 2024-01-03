#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#


# @lc code=start
from typing import Dict, List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_c: Dict[int, int] = {}
        for num in nums:
            if num not in num_c:
                num_c[num] = 0

            num_c[num] += 1

        counter: int = 0
        for num in sorted(list(num_c.keys())):
            if (num + k) in num_c:
                if k != 0 or num_c[num] > 1:
                    counter += 1

        return counter


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.findPairs([1, 3, 1, 5, 4], 0)

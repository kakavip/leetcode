#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
import heapq
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)

        score: int = 0
        for _ in range(k):
            v = -heapq.heappop(nums)

            score += v

            n = int(math.ceil(v / 3))
            heapq.heappush(nums, -n)

        return score


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxKelements(nums=[10, 10, 10, 10, 10], k=5) == 50)
    print(s.maxKelements(nums=[1, 10, 3, 3, 3], k=3) == 17)

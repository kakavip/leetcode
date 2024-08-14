#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            if self.count_pairs(nums, k, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def count_pairs(self, nums: List[int], k: int, mid: int) -> bool:
        count = 0
        left = 0

        for right in range(1, len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left

        return count >= k


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.smallestDistancePair([1, 3, 1], 1) == 0)
    print(s.smallestDistancePair([1, 1, 1], 1) == 0)
    print(s.smallestDistancePair([1, 6, 1], 3) == 5)
    print(s.smallestDistancePair([62, 100, 4], 2) == 58)
    print(s.smallestDistancePair([2, 2, 0, 1, 1, 0, 0, 1, 2, 0], 2) == 0)

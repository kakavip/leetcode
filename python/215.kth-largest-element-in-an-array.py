#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums: List[int] = nums.copy()

        new_nums.sort(reverse=True)

        return new_nums[min(k-1, len(nums) - 1)]
        # @lc code=end


if __name__ == "__main__":
    print("Done")

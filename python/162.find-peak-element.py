#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        for idx, val in enumerate(nums):
            if (
                idx < len(nums) - 1
                and val > nums[idx - 1]
                and val > nums[idx + 1]
                or idx == len(nums) - 1
                and nums[idx] > nums[idx] - 1
            ):
                return idx

        return 0


# @lc code=end

if __name__ == "__main__":
    pass

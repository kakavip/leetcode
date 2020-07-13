from typing import List

#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        while k > len(nums):
            k -= len(nums)

        threshold = len(nums) - k

        sub_nums = nums[threshold:]
        for idx in range(threshold):
            re_idx = len(nums) - 1 - idx
            nums[re_idx] = nums[re_idx - k]

        for idx in range(k):
            nums[idx] = sub_nums[idx]

        return None


# @lc code=end

if __name__ == "__main__":

    s = Solution()

    print(s.rotate([1, 2], 3))
    pass

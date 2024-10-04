#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#

# @lc code=start
from typing import Dict, List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = 0

        # Step 1: Calculate total sum and target remainder
        for num in nums:
            total_sum = (total_sum + num) % p

        target = total_sum % p
        if target == 0:
            return 0  # The array is already divisible by p

        # Step 2: Use a dict to track prefix sum mod p
        mod_map = {
            0: -1
        }  # To handle the case where the whole prefix is the answer
        current_sum = 0
        min_len = n

        # Step 3: Iterate over the array
        for i in range(n):
            current_sum = (current_sum + nums[i]) % p

            # Calculate what we need to remove
            needed = (current_sum - target + p) % p

            # If we have seen the needed remainder, we can consider this subarray
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])

            # Store the current remainder and index
            mod_map[current_sum] = i

        # Step 4: Return result
        return -1 if min_len == n else min_len


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minSubarray([3, 1, 4, 2], 6) == 1)
    print(s.minSubarray(nums=[6, 3, 5, 2], p=9) == 2)
    print(s.minSubarray(nums=[1, 2, 3], p=3) == 0)
    print(s.minSubarray([1, 2, 3], 7) == -1)
    print(s.minSubarray([4, 4, 2], 7) == -1)
    print(
        s.minSubarray(
            [8, 32, 31, 18, 34, 20, 21, 13, 1, 27, 23, 22, 11, 15, 30, 4, 2], 148
        )
        == 7
    )

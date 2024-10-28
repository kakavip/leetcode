#
# @lc app=leetcode id=2501 lang=python3
#
# [2501] Longest Square Streak in an Array
#

# @lc code=start
from collections import deque
from typing import Deque, List, Set


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        set_nums: Set[int] = set(nums)
        uniq_nums: Deque[int] = deque(sorted(set_nums))
        _max: int = max(uniq_nums)

        _expo_max: int = 1
        while uniq_nums:
            c_expo: int = 1
            cur_num: int = uniq_nums.popleft()

            # print(cur_num, uniq_nums)

            if cur_num ** (2**_expo_max) > _max:
                break

            while cur_num**2 in uniq_nums:
                c_expo += 1

                uniq_nums.remove(cur_num**2)
                cur_num = cur_num**2

            _expo_max = max(_expo_max, c_expo)

        if _expo_max < 2:
            return -1
        return _expo_max


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestSquareStreak([4, 3, 6, 16, 8, 2]) == 3)
    print(s.longestSquareStreak([2, 3, 5, 6, 7]) == -1)
    print(s.longestSquareStreak([2, 4, 8, 16]) == 3)

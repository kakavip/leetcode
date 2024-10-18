#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#

# @lc code=start
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        _max_or: int = nums[0]

        n: int = len(nums)
        for i in range(1, n):
            _max_or |= nums[i]

        def count(pre_or: int, idx: int) -> int:
            counter: int = 0
            if pre_or == _max_or:
                counter += 1
            for i in range(idx, n):
                c = count(pre_or | nums[i], i + 1)
                counter += c
            return counter

        n_counter: int = 0
        for k in range(n):
            n_counter += count(nums[k], k + 1)

        return n_counter


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.countMaxOrSubsets([3, 1]))
    print(s.countMaxOrSubsets([2, 2, 2]))
    print(s.countMaxOrSubsets([3, 2, 1, 5]))

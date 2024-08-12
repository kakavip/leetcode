#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
from typing import Dict, List


class Solution:
    _cache: Dict[int, int] = {}
    _max: int
    _max_counter: int

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        max_counters: List[int] = [1] * n
        max_nums: List[int] = [1] * n

        for i in range(n - 1):
            # max_nums[i] = max(max_nums[i], 1)
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    if max_nums[j] < max_nums[i] + 1:
                        max_nums[j] = max_nums[i] + 1
                        max_counters[j] = max_counters[i]
                    elif max_nums[j] == max_nums[i] + 1:
                        max_counters[j] += max_counters[i]

                    # max_nums[j] = max(max_nums[i] + 1, max_nums[j])

        _counter: int = 0
        _max: int = max(max_nums)
        for idx in range(len(max_nums)):
            val: int = max_nums[idx]
            if val == _max:
                _counter += max_counters[idx]

        # print("MAX: ", max(max_nums))
        # print("MAX_COUNTER: ", _counter)

        return _counter

    # def findNumberOfLIS2(self, nums: List[int]) -> int:
    #     self._cache.clear()
    #     self._max = 0
    #     self._max_counter = 0

    #     for i in range(len((nums))):
    #         self.find_next(nums, i, 0)

    #     # print(self._cache.values())

    #     return self._max_counter

    # def find_next(self, nums: List[int], pos: int, counter: int):
    #     if pos in self._cache and self._cache[pos] > counter + 1:
    #         return

    #     if counter + 1 > self._max:
    #         self._max = counter + 1
    #         self._max_counter = 1
    #     elif counter + 1 == self._max:
    #         self._max_counter += 1

    #     self._cache[pos] = counter + 1

    #     for i in range(pos + 1, len(nums)):
    #         if nums[i] > nums[pos]:
    #             self.find_next(nums, i, counter + 1)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findNumberOfLIS([1, 3, 5, 4, 7]) == 2)
    print(s.findNumberOfLIS([2, 2, 2, 2, 2]) == 5)
    print(s.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]) == 3)
    print(s.findNumberOfLIS([1, 1, 1, 2, 2, 2, 3, 3, 3]) == 27)

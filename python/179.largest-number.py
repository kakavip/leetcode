#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from typing import List


class Solution:
    _n: int

    def _cov(self, num: int) -> int:
        return int((str(num) * (self._n // len(str(num)) + 1))[: self._n])

    def largestNumber(self, nums: List[int]) -> str:
        # _max: int = max(nums)
        # self._n = len(str(_max))
        self._n = 12

        nums.sort(key=self._cov, reverse=True)

        return str(int("".join([str(num) for num in nums])))


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([3, 30, 34, 5, 9]) == "9534330")
    print(s.largestNumber([10, 2]) == "210")
    print(s.largestNumber([432, 43243]) == "43243432")
    print(s.largestNumber([111311, 1113]) == "1113111311")
    print(s.largestNumber([0, 0]) == "0")
    print(s.largestNumber([12341, 123411234]) == "12341123412341")
    print(s.largestNumber([111231111, 11123111]) == "11123111111231111")

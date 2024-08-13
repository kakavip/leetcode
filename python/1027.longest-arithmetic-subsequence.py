#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Subsequence
#

# @lc code=start
from typing import Dict, List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        counter: List[Dict[int, int]] = [{} for _ in range(n)]

        for i in range(n - 1):
            for j in range(i + 1, n):
                sub = nums[j] - nums[i]
                if sub not in counter[i]:
                    counter[i][sub] = 1
                counter[j][sub] = counter[i][sub] + 1

        _max: int = 0
        for i in range(n):
            for j in counter[i]:
                if counter[i][j] > _max:
                    _max = counter[i][j]

        # print(counter)
        return _max


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.longestArithSeqLength([3, 6, 9, 12]) == 4)
    print(s.longestArithSeqLength([9, 4, 7, 2, 10]) == 3)
    print(s.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]) == 4)
    print(s.longestArithSeqLength([83, 20, 17, 43, 52, 78, 68, 45]) == 2)

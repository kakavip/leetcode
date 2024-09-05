#
# @lc app=leetcode id=2028 lang=python3
#
# [2028] Find Missing Observations
#

# @lc code=start
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m: int = len(rolls)
        result: List[int] = [1] * n

        target_sum: int = mean * (m + n)
        _sum: int = sum(rolls)
        if not (_sum + n <= target_sum <= _sum + 6 * n):
            return []

        target_sum -= _sum
        for i in range(n):
            _sum_next: int = n - 1 - i
            if target_sum - _sum_next <= 6:
                result[i] = target_sum - _sum_next
                break
            else:
                result[i] = 6
                target_sum -= 6

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2))
    print(s.missingRolls(rolls=[1, 5, 6], mean=3, n=4))
    print(s.missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4))

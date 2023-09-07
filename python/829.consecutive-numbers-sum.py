#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#


# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        counter: int = 0
        if n in [1, 2]:
            return 1

        for k in range(1, int(n / 2 + 0.5) + 1):
            # first = ((n * 2 / k) + 1 - k) / 2
            if (n * 2 / k) + 1 - k <= 0:
                break
            if ((n * 2 / k) + 1 - k) % 2 == 0:
                counter += 1
                # print(first)

        return counter


# @lc code=end

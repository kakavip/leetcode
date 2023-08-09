#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start


class Solution:
    def addDigits(self, num: int) -> int:
        r = num
        while r >= 10:
            r = self.calc_digits(r)

        return r

    @staticmethod
    def calc_digits(num: int) -> int:
        return sum(map(int, list(str(num))))


# @lc code=end

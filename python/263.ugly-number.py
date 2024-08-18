#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#


# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return 0

        for v in [5, 3, 2]:
            while n % v == 0:
                n //= v

        return n == 1


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(6) == True)

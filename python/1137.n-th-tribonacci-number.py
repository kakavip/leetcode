#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#


# @lc code=start
class Solution:
    __cache = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n in self.__cache:
            return self.__cache[n]

        r = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.__cache[n] = r

        return self.__cache[n]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.tribonacci(4)

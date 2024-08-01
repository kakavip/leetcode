#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# @lc code=start
class Solution:
    __cache = {}

    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n

        if n in self.__cache:
            return self.__cache[n]

        result = self.fib(n - 1) + self.fib(n - 2)
        self.__cache[n] = result
        return self.__cache[n]


# @lc code=end

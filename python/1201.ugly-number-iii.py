#
# @lc app=leetcode id=1201 lang=python3
#
# [1201] Ugly Number III
#


# @lc code=start
import heapq
from typing import List
import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        _max: int = max(a, b, c)
        _min: int = min(a, b, c)
        _mid: int = a + b + c - _min - _max

        n_min: int = n * _min

        num_min: int = n
        num_mid: int = n_min // _mid
        num_max: int = n_min // _max

        new_n: int = n
        new_n += num_max + num_mid
        new_n -= n_min // ((_max * _mid) // math.gcd(_max, _mid))
        new_n -= n_min // ((_min * _mid) // math.gcd(_min, _mid))
        new_n -= n_min // ((_min * _max) // math.gcd(_min, _max))

        bcnn_max_mid: int = (_mid * _max) // math.gcd(_mid, _max)
        new_n += n_min // ((_min * bcnn_max_mid) // math.gcd(_min, bcnn_max_mid))

        while new_n > n:
            n_min = num_min * _min
            n_mid = num_mid * _mid
            n_max = num_max * _max

            drop_int: int = max(n_min, n_mid, n_max)

            if drop_int == n_min:
                num_min -= 1
            if drop_int == n_mid:
                num_mid -= 1
            if drop_int == n_max:
                num_max -= 1

            new_n -= 1

        return max(num_min * _min, num_max * _max, num_mid * _mid)


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(3, 2, 3, 5) == 4)
    print(s.nthUglyNumber(4, 2, 3, 4) == 6)
    print(s.nthUglyNumber(5, 2, 11, 12) == 10)
    print(s.nthUglyNumber(5, 2, 3, 3) == 8)
    print(s.nthUglyNumber(10, 7, 6, 8) == 28)
    # print(s.nthUglyNumber(1_000_000_000, 2, 217_983_653, 336_916_467))


# # 5: 2 4 6 8 10
# # 3: 3 6 9
# # 7: 2 3 4 6 8 9 10
# + 3: _max
# # - 1: max same min

# + 3: _mid
# - 1: mid same min
# - 3: mid same max
# # + 1: max same min same mid
# # 3: 3 6 9

# # - 1 same min
# # - 3 same _max
# # + 1 same (max _ min)

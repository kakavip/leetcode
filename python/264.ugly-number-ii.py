#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#


# @lc code=start
import heapq
from typing import Dict, List


class Solution:
    _max_n: int = 0
    _array: List[int] = []

    def nthUglyNumber(self, n: int) -> int:
        if n <= self._max_n:
            return self._array[n - 1]

        if not self._array:
            num_heap: List[int] = []

            for exp_5 in range(20):
                for exp_3 in range(30):
                    for exp_2 in range(50):
                        num_heap.append(2**exp_2 * 3**exp_3 * 5**exp_5)

            heapq.heapify(num_heap)

            while self._max_n <= 1690:
                self._array.append(heapq.heappop(num_heap))

                self._max_n += 1

        return self._array[n - 1]

        # while self._max_n <= n:
        #     next_2: int = (2 ** (exp_2 + 1)) * (3**exp_3) * (5**exp_5)
        #     next_3: int = (2**exp_2) * (3 ** (exp_3 + 1)) * (5**exp_5)
        #     next_5: int = (2**exp_2) * (3**exp_3) * (5 ** (exp_5 + 1))

        #     print("NEXT 2: {}, NEXT 3: {}, NEXT 5: {}".format(next_2, next_3, next_5))

        #     _min: int = min(next_2, next_3, next_5)
        #     if _min == next_2:
        #         exp_2 += 1
        #     elif _min == next_3:
        #         exp_3 += 1
        #     else:
        #         exp_5 += 1

        #     print("ADD NUMBER: ", _min)

        #     self._array.append(_min)
        #     self._max_n += 1

        # return self._array[n - 1]

    # def is_valid(self, x: int) -> bool:
    #     if x in self._cache:
    #         return self._cache[x]

    #     for v in [5, 3, 2]:
    #         while x % v == 0:
    #             x //= v

    #             if x in self._cache:
    #                 return self._cache[x]

    #     return x == 1


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.nthUglyNumber(10) == 12)
    # print(s.nthUglyNumber(1) == 1)
    print(s.nthUglyNumber(1352))
    print(s.nthUglyNumber(46))
    print(s.nthUglyNumber(10))

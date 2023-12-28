#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List


class Solution:
    cache = {1: [[1]], 2: [[1], [1, 1]]}

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows in self.cache:
            return self.cache[numRows]

        _max = max(list(self.cache.keys()))
        r = self.cache[_max].copy()
        for i in range(len(r[-1]) + 1, numRows + 1):
            c = [1]

            for j in range(len(r[-1]) - 1):
                c.append(r[-1][j] + r[-1][j + 1])

            c.append(1)
            r.append(c)

            self.cache.update({i: r.copy()})
        return r


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.generate(30))
    print(s.generate(20))

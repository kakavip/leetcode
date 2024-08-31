#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
from typing import Dict


class Solution:
    _cache: Dict[int, int] = {
        0: 1,
        1: 1,
        2: 2,
    }

    def numTrees(self, n: int) -> int:
        if len(list(self._cache.keys())) == 3:
            for i in range(3, 20):
                result: int = 0
                for j in range(1, i + 1):
                    result += self._cache[j - 1] * self._cache[i - j]

                self._cache[i] = result

        # print(self._cache)

        return self._cache[n]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3) == 5)

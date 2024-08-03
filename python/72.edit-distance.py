#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#


# @lc code=start
from typing import List


class Solution:
    def solve(self, word1: str, word2: str, n: int, m: int) -> int:
        if m < 0:
            return n + 1
        if n < 0:
            return m + 1

        if word1[n] == word2[m]:
            return 0 + self.solve(word1, word2, n - 1, m - 1)
        else:
            remove = 1 + self.solve(word1, word2, n - 1, m)
            add = 1 + self.solve(word1, word2, n, m - 1)
            replace = 1 + self.solve(word1, word2, n - 1, m - 1)

            return min(remove, add, replace)

    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        return self.solve(word1, word2, n - 1, m - 1)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.minDistance("horse", "ros") == 3, "Test 1"
    assert s.minDistance("intention", "execution") == 5, "Test 2"
    assert s.minDistance("", "") == 0, "Test 3"
    # print(s.minDistance("zoologicoarchaeologist",    "zoogeologist"))
    assert s.minDistance("zoologicoarchaeologist", "zoogeologist") == 10, "Test 5"
    assert s.minDistance("zoologicoarchaeologist", "zoopsychologist") == 10, "Test 6"
    assert s.minDistance("sea", "eat") == 2, "Test 7"
    assert s.minDistance("teacher", "acheer") == 3, "Test 8"
    assert s.minDistance("distance", "disbalance") == 3, "Test 9"

[
    [0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
]
[
    [0, 1, 2, 3, 4, 5, 6, 7],
    [1, 0, 2, 3, 4, 5, 6, 7],
    [2, 1, 0, 3, 4, 5, 6, 7],
    [3, 2, 1, 1, 2, 3, 4, 5],
    [4, 3, 2, 2, 1, 3, 4, 5],
    [5, 4, 3, 3, 2, 2, 3, 4],
    [6, 5, 4, 4, 2, 3, 3, 4],
    [7, 6, 5, 5, 3, 2, 4, 4],
    [8, 7, 6, 6, 4, 3, 2, 5],
    [9, 8, 7, 7, 5, 4, 3, 2],
]

[[1, 0, 1], [1, 1, 0], [1, 1, 1]]
[[1, 1, 2], [2, 2, 1], [3, 3, 3]]

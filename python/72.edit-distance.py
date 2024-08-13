#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#


# @lc code=start
from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2)
        n = len(word1)
        if m == 0:
            return n
        if n == 0:
            return m

        matrix: List[List[int]] = [[1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if word2[i] == word1[j]:
                    matrix[i][j] = 0

        min_matrix: List[List[int]] = [[float("inf")] * n for _ in range(m)]
        min_matrix[0][0] = matrix[0][0]
        zero: bool = False
        for i in range(1, n):
            if not zero:
                min_matrix[0][i] = min_matrix[0][i - 1] + matrix[0][i]
                if matrix[0][i] == 0:
                    zero = True
            else:
                min_matrix[0][i] = min_matrix[0][i - 1] + 1
        zero = False
        for i in range(1, m):
            if not zero:
                min_matrix[i][0] = min_matrix[i - 1][0] + matrix[i][0]
                if matrix[i][0] == 0:
                    zero = True
            else:
                min_matrix[i][0] = min_matrix[i - 1][0] + 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and j < n - 1 and i >= 1:
                    pre_right = min_matrix[i][j] + matrix[i][j + 1]
                    # if matrix[i][j + 1] + matrix[i][j] == 0:
                    #     pre_right += 1

                    min_matrix[i][j + 1] = min(min_matrix[i][j + 1], pre_right)
                if i < m - 1 and matrix[i][j] != 0 and j >= 1:
                    pre_bottom = min_matrix[i][j] + matrix[i + 1][j]
                    # if matrix[i + 1][j] + matrix[i][j] == 0:
                    #     pre_bottom += 1
                    min_matrix[i + 1][j] = min(min_matrix[i + 1][j], pre_bottom)

                if j < n - 1 and i < m - 1:
                    min_matrix[i + 1][j + 1] = min(
                        min_matrix[i + 1][j + 1],
                        min_matrix[i][j] + matrix[i + 1][j + 1],
                    )

        for i in range(1, n):
            min_matrix[m - 1][i] = min(
                min_matrix[m - 1][i - 1] + 1, min_matrix[m - 1][i]
            )

        for i in range(1, m):
            min_matrix[i][n - 1] = min(
                min_matrix[i - 1][n - 1] + 1, min_matrix[i][n - 1]
            )

        # print(matrix)
        # print(min_matrix)

        return min_matrix[m - 1][n - 1]


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

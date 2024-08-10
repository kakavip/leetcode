#
# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#

# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        matrix = [[0] * n * 3 for _ in range(n * 3)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    matrix[i * 3][j * 3 + 2] = 1
                    matrix[i * 3 + 1][j * 3 + 1] = 1
                    matrix[i * 3 + 2][j * 3] = 1

                elif grid[i][j] == "\\":
                    matrix[i * 3][j * 3] = 1
                    matrix[i * 3 + 1][j * 3 + 1] = 1
                    matrix[i * 3 + 2][j * 3 + 2] = 1

        region_counter: int = 0
        for i in range(n * 3):
            for j in range(n * 3):
                if matrix[i][j] == 0:
                    self.fill_matrix(matrix, (i, j))
                    region_counter += 1

        # print(matrix)
        # print(region_counter)

        return region_counter

    def fill_matrix(self, matrix: List[List[int]], pos: Tuple[int, int]):
        down_rows: List[Tuple[int, int]] = []
        up_rows: List[Tuple[int, int]] = []

        # matrix[pos[0]][pos[1]] = 1

        l_slice: List[int] = [pos[0], pos[1]]
        while l_slice[1] >= 0 and matrix[l_slice[0]][l_slice[1]] == 0:
            if l_slice[0] < len(matrix) - 1 and matrix[l_slice[0] + 1][l_slice[1]] == 0:
                down_rows.append((l_slice[0] + 1, l_slice[1]))

            if l_slice[0] > 0 and matrix[l_slice[0] - 1][l_slice[1]] == 0:
                up_rows.append((l_slice[0] - 1, l_slice[1]))

            matrix[l_slice[0]][l_slice[1]] = 1
            l_slice[1] -= 1

        r_slice: List[int] = list(pos)
        while r_slice[1] + 1 < len(matrix) and matrix[r_slice[0]][r_slice[1] + 1] == 0:
            if (
                r_slice[0] < len(matrix) - 1
                and matrix[r_slice[0] + 1][r_slice[1] + 1] == 0
            ):
                down_rows.append((r_slice[0] + 1, r_slice[1] + 1))

            if r_slice[0] > 0 and matrix[r_slice[0] - 1][r_slice[1] + 1] == 0:
                up_rows.append((r_slice[0] - 1, r_slice[1] + 1))

            matrix[r_slice[0]][r_slice[1] + 1] = 1
            r_slice[1] += 1

        for pos in down_rows + up_rows:
            self.fill_matrix(matrix, pos)


# @lc code=end

# [
#     [0, 0, 1, 1, 0, 0],
#     [0, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 1],
#     [0, 1, 0, 0, 1, 0],
#     [0, 0, 1, 1, 0, 0],
# ]

if __name__ == "__main__":
    s = Solution()
    # assert s.regionsBySlashes([" /", "/ "]) == 2, "Test 1"
    # assert s.regionsBySlashes(["/\\", "\\/"]) == 5, "Test 2"
    assert s.regionsBySlashes([" /", "  "]) == 1, "Test 3"

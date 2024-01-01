#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
from typing import Any, Dict, List, Tuple

debug = False


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        _max: int = 0
        old_squares: Dict[Tuple[int, int, int], int] = {}

        if not matrix:
            return 0

        matrix.append(["0"] * len(matrix[0]))

        for y, row in enumerate(matrix):
            o_squares = list(old_squares.keys())
            for square in o_squares:
                o_y, x1, x2 = square
                h = old_squares[square]

                if x2 - x1 <= h:
                    _max = max(_max, min(x2 - x1, h))
                    old_squares.pop(square)
                    continue

                _start = -1
                _n_ranges = []
                for x, val in enumerate(row[x1:x2] + ["0"]):
                    if val == "1" and _start == -1:
                        _start = x
                        continue

                    if val == "0" and _start != -1:
                        _n_ranges.append([_start + x1, x + x1])
                        _start = -1

                debug and print(_n_ranges)
                old_squares.pop(square)
                if not _n_ranges:
                    _max = max(_max, min(h, x2 - x1))
                else:
                    for _range in _n_ranges:
                        if _range[1] - _range[0] >= h:
                            old_squares.update({(o_y, _range[0], _range[1]): h + 1})
                        else:
                            _max = max(min(_range[1] - _range[0], h + 1), _max)
                            _max = max(min(x2 - x1, h), _max)

            _start = -1
            for x, col in enumerate(row + ["0"]):
                if col == "1" and _start == -1:
                    _start = x
                    continue

                if col == "0" and _start != -1:
                    if x - _start > _max:
                        old_squares.update({(y, _start, x): 1})

                    _start = -1
            debug and print("OLD SQUARES: ", old_squares, "MAX: ", _max)

        return _max**2


# @lc code=end

debug = True

if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    matrix = [["0", "1"], ["1", "0"]]
    matrix = [["1", "1"]]
    matrix = [["1", "1"], ["1", "1"]]
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    matrix = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1"],
    ]

    s = Solution()
    print(s.maximalSquare(matrix))

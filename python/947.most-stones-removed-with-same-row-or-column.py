#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        col_map: Dict[int, List[List[int]]] = {}
        row_map: Dict[int, List[List[int]]] = {}
        _cache: Dict[Tuple[int, int], bool] = {}

        for stone in stones:
            _cache[(stone[0], stone[1])] = False
            if stone[0] not in col_map:
                col_map[stone[0]] = []
            col_map[stone[0]].append(stone)

            if stone[1] not in row_map:
                row_map[stone[1]] = []
            row_map[stone[1]].append(stone)

        def fill(stone: List[int]) -> int:
            result: int = 1

            _cache[(stone[0], stone[1])] = True
            for n_stone in col_map[stone[0]]:
                if not _cache[(n_stone[0], n_stone[1])]:
                    result += fill(n_stone)

            for n_stone in row_map[stone[1]]:
                if not _cache[(n_stone[0], n_stone[1])]:
                    result += fill(n_stone)

            return result

        _counter: int = 0
        for stone in stones:
            if not _cache[(stone[0], stone[1])]:
                _counter += fill(stone) - 1

        return _counter


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3)
    print(s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5)
    print(s.removeStones([[0, 0]]) == 0)
    print(s.removeStones([[3, 2], [3, 1], [4, 4], [1, 1], [0, 2], [4, 0]]) == 4)

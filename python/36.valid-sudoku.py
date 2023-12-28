#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import Dict, List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        v_map = {}
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] != ".":
                    if board[y][x] not in v_map:
                        v_map[board[y][x]] = {"x": [], "y": []}
                    if x in v_map[board[y][x]]["x"] or y in v_map[board[y][x]]["y"]:
                        return False

                    v_map[board[y][x]]["x"].append(x)
                    v_map[board[y][x]]["y"].append(y)

        for _k in v_map:
            if not self.check_value(v_map[_k]):
                return False

        return True

    def check_value(self, data: Dict[str, List[int]]) -> bool:
        g_map: Dict[int, bool] = {}
        for i in range(len(data["x"])):
            g = self.get_group(data["x"][i], data["y"][i])
            if g in g_map:
                return False
            g_map[g] = True

        return True

    @staticmethod
    def get_group(x: int, y: int) -> int:
        if 0 <= x < 3:
            if 0 <= y < 3:
                return 1
            if 3 <= y < 6:
                return 4
            if 6 <= y < 9:
                return 7
        if 3 <= x < 6:
            if 0 <= y < 3:
                return 2
            if 3 <= y < 6:
                return 5
            if 6 <= y < 9:
                return 8
        if 6 <= x < 9:
            if 0 <= y < 3:
                return 3
            if 3 <= y < 6:
                return 6
            if 6 <= y < 9:
                return 9
        return 0


# @lc code=end
if __name__ == "__main__":
    # board = [
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    # ]
    # board = [
    #     [".", ".", ".", ".", "5", ".", ".", "1", "."],
    #     [".", "4", ".", "3", ".", ".", ".", ".", "."],
    #     [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    #     ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    #     [".", ".", "2", ".", "7", ".", ".", ".", "."],
    #     [".", "1", "5", ".", ".", ".", ".", ".", "."],
    #     [".", ".", ".", ".", ".", "2", ".", ".", "."],
    #     [".", "2", ".", "9", ".", ".", ".", ".", "."],
    #     [".", ".", "4", ".", ".", ".", ".", ".", "."],
    # ]
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    s = Solution()
    print(s.isValidSudoku(board))

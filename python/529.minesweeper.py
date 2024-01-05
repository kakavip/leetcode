#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
from typing import List


class Solution:
    def __init__(self) -> None:
        self.maxX = 0
        self.maxY = 0
        self.board = []
        self.mask_board = []

    def reset(self, board: List[List[str]]):
        self.maxX = len(board[0])
        self.maxY = len(board)

        self.board = board

        for y in range(self.maxY):
            self.mask_board.append([0] * self.maxX)

        # check all mine
        for y in range(self.maxY):
            for x in range(self.maxX):
                if board[y][x] == "M":
                    if x > 0 and y < self.maxY - 1:
                        self.mask_board[y + 1][x - 1] += 1
                    if y < self.maxY - 1 and x < self.maxX:
                        self.mask_board[y + 1][x] += 1
                    if x < self.maxX - 1 and y < self.maxY - 1:
                        self.mask_board[y + 1][x + 1] += 1

                    if x > 0:
                        self.mask_board[y][x - 1] += 1
                    if x < self.maxX - 1:
                        self.mask_board[y][x + 1] += 1

                    if x > 0 and y > 0:
                        self.mask_board[y - 1][x - 1] += 1
                    if y > 0:
                        self.mask_board[y - 1][x] += 1
                    if y > 0 and x < self.maxX - 1:
                        self.mask_board[y - 1][x + 1] += 1

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        if board[click[0]][click[1]] != "E":
            return board

        self.reset(board)

        self.update_board_recursively(click)

        return board

    def get_num_adjcent_mines(self, point: List[int]) -> int:
        return self.mask_board[point[0]][point[1]]

    def update_board_recursively(self, click: List[int]):
        # set and check can next
        if self.board[click[0]][click[1]] != "E":
            return

        _num = self.get_num_adjcent_mines(click)
        if _num > 0:
            self.board[click[0]][click[1]] = str(_num)
            return
        else:
            self.board[click[0]][click[1]] = "B"

        y, x = click
        if x > 0 and y < self.maxY - 1:
            self.update_board_recursively([y + 1, x - 1])
        if y < self.maxY - 1 and x < self.maxX:
            self.update_board_recursively([y + 1, x])
        if x < self.maxX - 1 and y < self.maxY - 1:
            self.update_board_recursively([y + 1, x + 1])

        if x > 0:
            self.update_board_recursively([y, x - 1])
        if x < self.maxX - 1:
            self.update_board_recursively([y, x + 1])

        if x > 0 and y > 0:
            self.update_board_recursively([y - 1, x - 1])
        if y > 0:
            self.update_board_recursively([y - 1, x])
        if y > 0 and x < self.maxX - 1:
            self.update_board_recursively([y - 1, x + 1])


# @lc code=end

if __name__ == "__main__":
    board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]
    click = [3, 0]

    board = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    click = [1, 2]

    s = Solution()
    print(s.updateBoard(board, click))

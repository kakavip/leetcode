#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#
from typing import List


# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        counter: int = 0

        for y in range(len(board)):
            for x in range(len(board[y])):
                if y == 0:
                    if board[y][x] == "X" and (x == 0 or board[y][x - 1] != "X"):
                        counter += 1
                else:
                    if (
                        board[y][x] == "X"
                        and board[y - 1][x] != "X"
                        and (x == 0 or board[y][x - 1] != "X")
                    ):
                        counter += 1

        return counter


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.countBattleships([["."]]))

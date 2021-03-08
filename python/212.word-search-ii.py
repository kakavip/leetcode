#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

from typing import List
# @lc code=start

LEFT, TOP, BOTTOM, RIGHT = 0, 1, 2, 3


class Solution:
    @classmethod
    def check_word(cls,
                   x: int,
                   y: int,
                   board: List[List[str]],
                   word: str,
                   hist_points: List[List[int]] = None):
        if len(word) == 0:
            return True

        hist_points = hist_points or [[y, x]]

        left_point: List[int] = [] if x <= 0 or [y, x -
                                                 1] in hist_points else [
                                                     y, x - 1
        ]
        up_point: List[int] = [] if y <= 0 or [y - 1, x] in hist_points else [
            y - 1, x
        ]
        right_point: List[int] = [] if (
            x >= len(board[0]) - 1) or [y, x +
                                        1] in hist_points else [y, x + 1]
        down_point: List[int] = [] if (
            y >= len(board) - 1) or [y + 1, x] in hist_points else [y + 1, x]

        check_left, check_right, check_up, check_down = False, False, False, False
        if left_point and board[left_point[0]][left_point[1]] == word[0]:
            # print("-> LEFT " + word + "  --> ", hist_points)

            check_left = cls.check_word(left_point[1], left_point[0], board,
                                        word[1:], hist_points + [left_point])

        if up_point and board[up_point[0]][up_point[1]] == word[0]:
            # print("-> UP " + word + "  --> ", hist_points)
            check_up = cls.check_word(up_point[1], up_point[0], board,
                                      word[1:], hist_points + [up_point])

        if right_point and board[right_point[0]][right_point[1]] == word[0]:
            # print("-> RIGHT " + word + "  --> ", hist_points)
            check_right = cls.check_word(right_point[1], right_point[0], board,
                                         word[1:], hist_points + [right_point])

        if down_point and board[down_point[0]][down_point[1]] == word[0]:
            # print("-> DOWN " + word + "  --> ", hist_points)
            check_down = cls.check_word(down_point[1], down_point[0], board,
                                        word[1:], hist_points + [down_point])

        return check_left or check_right or check_up or check_down

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result: List[str] = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                processed_words: List[str] = words.copy()
                removed_words: List[str] = []

                for word in processed_words:
                    if board[i][j] == word[0] and self.check_word(
                            j, i, board, word[1:]):
                        result.append(word)
                        removed_words.append(word)

                for _w in removed_words:
                    words.remove(_w)

        return result

        # @lc code=end


if __name__ == "__main__":
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain", "hklf", "hf"]
    # result = Solution.check_word(3, 0, board, words[0][1:])
    # result = Solution.check_word(3, 0, board, words[0][1:])
    instance: Solution = Solution()
    result = instance.findWords(board, words)

    print("Nguyen Minh Tuan: ", result)

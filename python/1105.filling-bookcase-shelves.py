#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#
from typing import List


# @lc code=start
is_debug = False


class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        n = len(books)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0  # Base case: no books require 0 height

        for i in range(1, n + 1):
            is_debug and print("DP: ", dp)
            is_debug and print("CHECK [i]: ", i, " dp[i]: ", dp[i])

            total_width = 0
            max_height = 0
            for j in range(i, 0, -1):
                total_width += books[j - 1][0]
                if total_width > shelfWidth:
                    break

                max_height = max(max_height, books[j - 1][1])
                is_debug and print("CHECK MAX HEIGHT: ", max_height)

                is_debug and print(
                    "BOOKS [j-1](index): ",
                    j - 1,
                    " WIDTH: ",
                    books[j - 1][0],
                    " HEIGHT: ",
                    books[j - 1][1],
                )
                is_debug and print(
                    "CHECK PREVIOUS: [j-1]: ", j - 1, " dp[j-1]: ", dp[j - 1]
                )
                is_debug and print(
                    "dp[j-1] + max_height: ",
                    dp[j - 1] + max_height,
                    " vs dp[i]: ",
                    dp[i],
                )
                dp[i] = min(dp[i], dp[j - 1] + max_height)

            is_debug and print("UPDATE [i]: ", i, " dp[i]: ", dp[i])
            is_debug and print("---------------------------------------")

        return dp[n]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    is_debug = True
    s.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4)

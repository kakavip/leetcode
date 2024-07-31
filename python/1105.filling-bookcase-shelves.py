#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#
from typing import List


# @lc code=start
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        f = [0] * (n + 1)

        for i, (w, h) in enumerate(books, 1):
            new_h = f[i - 1] + h
            f[i] = new_h

            for j in range(i - 1, 0, -1):
                w += books[j - 1][0]
                if w > shelfWidth:
                    break

                h = max(h, books[j - 1][1])
                f[i] = min(f[i], f[j - 1] + h)

        return f[n]


# @lc code=end

#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)

        pairs = sorted(pairs, key=lambda x: x[0])

        counter: List[int] = [1] * n
        for i in range(n - 1):
            for j in range(i, n):
                if pairs[i][-1] < pairs[j][0]:
                    counter[j] = max(counter[j], counter[i] + 1)

        return max(counter)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2)
    print(s.findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3)

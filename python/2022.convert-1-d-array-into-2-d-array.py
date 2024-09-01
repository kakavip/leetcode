#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        result: List[List[int]] = []
        for i in range(m):
            result.append(original[i * n : (i + 1) * n])

        return result


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.construct2DArray([1, 2, 3], 1, 3) == [[1, 2, 3]])
    print(s.construct2DArray(original=[1, 2, 3, 4], m=2, n=2) == [[1, 2], [3, 4]])
    print(s.construct2DArray(original=[1, 2], m=1, n=1) == [])

#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#

# @lc code=start


from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
        result = [[rStart, cStart]]
        steps = d = 0

        while len(result) < rows * cols:
            if d % 2 == 0:
                steps += 1

            for _ in range(steps):
                rStart += directions[d][0]
                cStart += directions[d][1]

                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])

                if len(result) == rows * cols:
                    return result

            d = (d + 1) % 4

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.spiralMatrixIII(1, 4, 0, 0))
    print(
        s.spiralMatrixIII(5, 6, 1, 4)
        == [
            [1, 4],
            [1, 5],
            [2, 5],
            [2, 4],
            [2, 3],
            [1, 3],
            [0, 3],
            [0, 4],
            [0, 5],
            [3, 5],
            [3, 4],
            [3, 3],
            [3, 2],
            [2, 2],
            [1, 2],
            [0, 2],
            [4, 5],
            [4, 4],
            [4, 3],
            [4, 2],
            [4, 1],
            [3, 1],
            [2, 1],
            [1, 1],
            [0, 1],
            [4, 0],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0],
        ]
    )

#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
from typing import List, Tuple


# @lc code=start
debug = False


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        b_points: List[List[int]] = points.copy()

        b_points.sort(key=lambda x: x[0])
        debug and print(f"Ball Points: {b_points}")

        num_arr: int = 0
        _min, _max = -1, -1
        _current_blocks: List[List[int]] = []
        for b_point in b_points:
            if not _current_blocks:
                _current_blocks.append(b_point)
                _min, _max = b_point[:2]
            else:
                # check in
                if b_point[0] > _max:
                    num_arr += 1

                    _current_blocks.clear()
                    _current_blocks.append(b_point)
                    _min, _max = b_point[:2]
                else:
                    _min = max(b_point[0], _min)
                    _max = min(b_point[1], _max)
                    _current_blocks.append(b_point)

        return num_arr + 1


# @lc code=end

debug = True
if __name__ == "__main__":
    s = Solution()
    print(s.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))  # 4
    print(s.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))  # 2
    print(s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2
    print(
        s.findMinArrowShots(
            [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
        )
    )  # 2

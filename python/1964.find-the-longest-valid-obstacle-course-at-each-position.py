#
# @lc app=leetcode id=1964 lang=python3
#
# [1964] Find the Longest Valid Obstacle Course at Each Position
#

# @lc code=start
from typing import List
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n: int = len(obstacles)
        # _max: int = -1

        result: List[int] = []
        dp: List[int] = [0] + [float("inf")] * n
        for i in range(n):
            idx: int = bisect.bisect_right(dp, obstacles[i])

            dp[idx] = obstacles[i]
            # _max = max(_max, idx)

            print(dp)
            result.append(idx)

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestObstacleCourseAtEachPosition([1, 2, 3, 2]) == [1, 2, 3, 3])
    print(s.longestObstacleCourseAtEachPosition([2, 2, 1]) == [1, 2, 1])
    print(
        s.longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]) == [1, 1, 2, 3, 2, 2]
    )

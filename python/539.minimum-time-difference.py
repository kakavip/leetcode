#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
from typing import List


def time_to_min(s: str) -> int:
    h, m = s.split(":")
    return int(h) * 60 + int(m)


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)

        mins: List[int] = sorted(map(time_to_min, timePoints))
        diff_mins: List[int] = [0] * n

        diff_mins[0] = 24 * 60 + mins[0] - mins[-1]
        for i in range(1, n):
            diff_mins[i] = mins[i] - mins[i - 1]

        return min(diff_mins)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findMinDifference(["23:59", "00:00"]))
    print(s.findMinDifference(["00:00", "23:59", "00:00"]))

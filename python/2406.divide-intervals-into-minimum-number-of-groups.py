#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        _min_group: int = 0
        out_time_intervals: List[int] = []
        heapq.heapify(out_time_intervals)
        for interval in intervals:
            start, end = interval[:2]

            while out_time_intervals and out_time_intervals[0] < start:
                heapq.heappop(out_time_intervals)

            heapq.heappush(out_time_intervals, end)
            _min_group = max(len(out_time_intervals), _min_group)

        return _min_group


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3)
    print(s.minGroups([[1, 3], [5, 6], [8, 10], [11, 13]]) == 1)

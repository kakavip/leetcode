#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#

# @lc code=start
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        start_mins: List[List] = sorted(arrays, key=lambda x: x[0])
        end_maxs: List[List] = sorted(arrays, key=lambda x: -x[-1])

        max_dis: int = end_maxs[0][-1] - start_mins[0][0]
        if end_maxs[0] == start_mins[0]:
            max_dis = max(
                end_maxs[1][-1] - start_mins[0][0], end_maxs[0][-1] - start_mins[1][0]
            )

        return max_dis


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]) == 4)
    print(s.maxDistance([[1], [1]]) == 0)

#
# @lc app=leetcode id=517 lang=python3
#
# [517] Super Washing Machines
#
from collections import deque
import heapq
from itertools import accumulate
from typing import Any, Dict, List


# @lc code=start
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if not machines:
            return -1
        if sum(machines) % len(machines) != 0:
            return -1

        avg: int = sum(machines) // len(machines)

        zero_machines = [m - avg for m in machines]
        _min_moves = max(zero_machines)

        acc_machines = []
        _sum: int = 0
        for m in zero_machines:
            _sum += m

            acc_machines.append(abs(_sum))

        _max_moves_in_hole: int = max(acc_machines)
        return max(_min_moves, _max_moves_in_hole)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.findMinMoves([1, 0, 5]))
    # print(s.findMinMoves([0, 3, 0]))
    # print(s.findMinMoves([4, 0, 0, 4]))
    print(s.findMinMoves([0, 0, 11, 5]))
    # print(s.findMinMoves([0, 0, 10, 0, 0, 0, 10, 0, 0, 0]))
    # print(
    #     s.findMinMoves(
    #         [100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0]
    #     )
    # )

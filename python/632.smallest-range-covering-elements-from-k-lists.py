#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
from collections import deque
import heapq
from typing import Deque, Dict, List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k: int = len(nums)
        pipeline: List[int] = []
        _map_queue: Dict[int, List[int]] = {}

        for i in range(k):
            nums[i] = list(set(nums[i]))
            for j in range(len(nums[i])):
                if nums[i][j] not in _map_queue:
                    _map_queue[nums[i][j]] = []

                _map_queue[nums[i][j]].append(i)

                pipeline.append(nums[i][j])

        pipeline = list(set(pipeline))
        heapq.heapify(pipeline)

        slide_windows: Deque[int] = deque()
        queue_checker: List[int] = [0] * k
        queue_counter: List[int] = [0] * k

        while sum(queue_checker) != k:
            v: int = heapq.heappop(pipeline)
            slide_windows.append(v)
            for q in _map_queue[v]:
                queue_checker[q] = 1
                queue_counter[q] += 1

        while slide_windows:
            _can_pop: bool = True
            for q in _map_queue[slide_windows[0]]:
                if queue_counter[q] <= 1:
                    _can_pop = False
                    break

            if _can_pop:
                for q in _map_queue[slide_windows[0]]:
                    queue_counter[q] -= 1

                slide_windows.popleft()
            else:
                break

        _min_range: List[int] = [slide_windows[0], slide_windows[-1]]
        _duration: int = slide_windows[-1] - slide_windows[0]

        while _duration > 0 and pipeline:
            v = heapq.heappop(pipeline)
            slide_windows.append(v)
            for q in _map_queue[v]:
                queue_counter[q] += 1
                queue_checker[q] = 1

            while slide_windows and v - slide_windows[0] >= _duration:
                for q in _map_queue[slide_windows[0]]:
                    queue_counter[q] -= 1
                    if queue_counter[q] <= 0:
                        queue_checker[q] = 0

                slide_windows.popleft()

            if sum(queue_checker) == k:
                while slide_windows:
                    _can_pop: bool = True
                    for q in _map_queue[slide_windows[0]]:
                        if queue_counter[q] <= 1:
                            _can_pop = False
                            break

                    if _can_pop:
                        for q in _map_queue[slide_windows[0]]:
                            queue_counter[q] -= 1

                        slide_windows.popleft()
                    else:
                        break

                if slide_windows[-1] - slide_windows[0] < _duration:
                    _duration = slide_windows[-1] - slide_windows[0]
                    _min_range = [slide_windows[0], slide_windows[-1]]

        return _min_range


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(
        s.smallestRange(nums=[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
        == [20, 24]
    )
    print(s.smallestRange(nums=[[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [1, 1])
    print(s.smallestRange([[-5, -4, -3, -2, -1], [1, 2, 3, 4, 5]]) == [-1, 1])
    print(s.smallestRange([[10, 10], [11, 11]]) == [10, 11])

#
# @lc app=leetcode id=2402 lang=python3
#
# [2402] Meeting Rooms III
#

# @lc code=start
import heapq
from typing import Dict, List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if n == 1:
            return 0

        meetings.sort(key=lambda x: x[0])

        avai_rooms: List[int] = [i for i in range(1, n + 1)]
        timeout_rooms: List[int] = []
        timeout_map: Dict[int, List[int]] = {}
        room_meeting_counters: List[int] = [0] * n

        heapq.heapify(avai_rooms)
        heapq.heapify(timeout_rooms)

        for meeting in meetings:
            start, end = meeting

            while timeout_rooms and timeout_rooms[0] <= start:
                to: int = heapq.heappop(timeout_rooms)

                if to in timeout_map:
                    for room in timeout_map[to]:
                        heapq.heappush(avai_rooms, room)

                    del timeout_map[to]

            n_start: int = start
            if not avai_rooms:
                min_to: int = heapq.heappop(timeout_rooms)
                pending_room: int = heapq.heappop(timeout_map[min_to])

                n_start = min_to
                heapq.heappush(avai_rooms, pending_room)

            n_end: int = n_start + (end - start)
            used_room: int = heapq.heappop(avai_rooms)

            if n_end not in timeout_map:
                timeout_map[n_end] = []
                heapq.heapify(timeout_map[n_end])

            room_meeting_counters[used_room - 1] += 1
            heapq.heappush(timeout_map[n_end], used_room)
            heapq.heappush(timeout_rooms, n_end)

        _max = max(room_meeting_counters)
        # print(room_meeting_counters)

        return room_meeting_counters.index(_max)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1)
    print(s.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]) == 0)
    print(s.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]) == 0)
    print(
        s.mostBooked(n=4, meetings=[[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]) == 0
    )

#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
import heapq
from typing import List, Tuple


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        queue_s: List[Tuple[int, str]] = []
        heapq.heapify(queue_s)

        a and heapq.heappush(queue_s, (-a, "a"))
        b and heapq.heappush(queue_s, (-b, "b"))
        c and heapq.heappush(queue_s, (-c, "c"))

        s: str = ""
        while queue_s:
            count, char = heapq.heappop(queue_s)
            count = -count

            if not s or char != s[-1]:
                s += char * min(2, count)
                count -= min(2, count)

                if count > 0:
                    heapq.heappush(queue_s, (-count, char))
            # elif char == s[-1]:
            else:
                if not queue_s:
                    break

                new_count, new_char = heapq.heappop(queue_s)
                new_count = -new_count

                s += new_char * min(1, new_count)
                new_count -= min(1, new_count)

                if new_count > 0:
                    heapq.heappush(queue_s, (-new_count, new_char))

                heapq.heappush(queue_s, (-count, char))

        return s


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestDiverseString(1, 1, 7) == "ccaccbcc")
    print(s.longestDiverseString(7, 1, 0) == "aabaa")
    print(s.longestDiverseString(0, 8, 11))

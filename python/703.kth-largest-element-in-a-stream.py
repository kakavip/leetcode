#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq
from typing import List


class KthLargest:
    k: int
    k_min_queue: List[int]
    k_max_queue: List[int]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_min_queue = []
        self.k_max_queue = [i for i in nums]
        heapq.heapify(self.k_min_queue)
        heapq.heapify(self.k_max_queue)

        self._transfer()

        # print(self.k_min_queue)
        # print(self.k_max_queue)

    def _transfer(self):
        k = self.k

        n_max: int = len(self.k_max_queue)
        while n_max > k:
            v = heapq.heappop(self.k_max_queue) * -1
            heapq.heappush(self.k_min_queue, v)

            n_max -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.k_max_queue, val)
        self._transfer()

        # print(self.k_min_queue)
        # print(self.k_max_queue)

        return self.k_max_queue[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

if __name__ == "__main__":
    # s = KthLargest(3, [4, 5, 8, 2])

    # print(s.add(3))
    # print(s.add(5))
    # print(s.add(10))
    # print(s.add(9))
    # print(s.add(4))

    s = KthLargest(1, [])
    print(s.add(-3))
    print(s.add(-2))
    print(s.add(-4))
    print(s.add(0))
    print(s.add(4))

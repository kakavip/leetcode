#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
import heapq
from typing import List

# @lc code=start


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index_map = {}
        h_nums = nums[:k].copy()
        for idx in range(len(h_nums)):
            index_map[h_nums[idx]] = idx
            h_nums[idx] *= -1

        heapq.heapify(h_nums)
        max_windows = [-h_nums[0]]
        for idx in range(k, len(nums)):
            index_map[nums[idx]] = idx
            heapq.heappush(h_nums, -nums[idx])

            while index_map[-h_nums[0]] + k - 1 < idx:
                heapq.heappop(h_nums)

            max_windows.append(-h_nums[0])

        return max_windows


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(s.maxSlidingWindow([1, -1], 1))

#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#
from typing import Any, Dict, List, Optional, Tuple


# @lc code=start
is_debug = False


class Solution:
    @staticmethod
    def check_valid(thres: int, arr: List[str], m: int, k: int) -> bool:
        num_bouquets: int = 0

        pre_count: int = 0
        for v in arr + [float("inf")]:
            if v <= thres:
                pre_count += 1
            else:
                num_bouquets += pre_count // k
                pre_count = 0

        return num_bouquets >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        num_flowers = m * k
        len_bloom_day = len(bloomDay)
        if num_flowers > len_bloom_day:
            return -1
        elif num_flowers == len_bloom_day:
            return max(bloomDay)

        b_day_mask = sorted(set(bloomDay))
        start, end = 0, len(b_day_mask) - 1

        result: int = -1
        while start <= end:
            mid = (end + start) // 2

            if self.check_valid(b_day_mask[mid], bloomDay, m, k):
                result = b_day_mask[mid]

                end = mid - 1
            else:
                start = mid + 1

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.minDays([1, 10, 3, 10, 2], m=3, k=1))
    # print(s.minDays([1, 10, 3, 10, 2], m=3, k=2))
    # print(s.minDays([7, 7, 7, 7, 12, 7, 7], m=2, k=3))
    # is_debug = True
    assert s.minDays([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2) == 9, "Test 1"
    # print("--------------------------------------------------------------")
    assert (
        s.minDays(
            [5, 37, 55, 92, 22, 52, 31, 62, 99, 64, 92, 53, 34, 84, 93, 50, 28], 8, 2
        )
        == 93
    ), "Test 2"

    assert s.minDays([30, 49, 11, 66, 54, 22, 2, 57, 35], 3, 3) == 66, "Test 3"
    assert (
        s.minDays(
            [62, 75, 98, 63, 47, 65, 51, 87, 22, 27, 73, 92, 76, 44, 13, 90, 100, 85],
            2,
            7,
        )
        == 98
    ), "Test 4"

    assert s.minDays([1, 10, 3, 10, 2], 3, 1) == 3, "Test 5"

#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
from random import randint
from time import time
from typing import List


# @lc code=start

is_debug = False


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.quick_sort(nums, 0, len(nums) - 1)
        # return self.radix_sort(nums)
        return self._index(nums)

    def quick_sort(self, nums: List[int], start: int, end: int) -> List[int]:
        if end <= start:
            return nums

        mark_idx = (start + end) // 2

        mark_val: int = nums[mark_idx]
        is_debug and print(
            "ORIGINAL MARK: ", mark_idx, " VALUE MARK: ", mark_val, " NUMS: ", nums
        )

        slice_start: int = start
        slice_end: int = end

        while slice_start < slice_end:
            while slice_start <= end and nums[slice_start] < mark_val:
                slice_start += 1

            # print("TEST: ", slice_end, nums)
            while slice_end >= start and nums[slice_end] > mark_val:
                slice_end -= 1

            if slice_start >= slice_end:
                break

            nums[slice_start], nums[slice_end] = nums[slice_end], nums[slice_start]

            if mark_idx in [slice_end, slice_start]:
                mark_idx = (slice_start + slice_end) - mark_idx
                if mark_idx == slice_start:
                    slice_end -= 1
                if mark_idx == slice_end:
                    slice_start += 1

            else:
                slice_start += 1
                slice_end -= 1

        is_debug and print("MARK: ", mark_idx, " NUMS: ", nums)
        self.quick_sort(nums, start, mark_idx - 1)
        self.quick_sort(nums, mark_idx + 1, end)

        return nums

    @staticmethod
    def radix_el_sort(nums: List[int], exp: int):
        n = len(nums)

        bucket: List[int] = [0] * n

        partition: List[int] = [0] * 10
        for num in nums:
            partition[int((num // (10 ** (exp - 1))) % 10)] += 1

        for i in range(1, 10):
            partition[i] += partition[i - 1]

        # print(partition)

        i = n - 1
        while i >= 0:
            num = nums[i]
            idx: int = int((num // (10 ** (exp - 1))) % 10)

            bucket[partition[idx] - 1] = num
            partition[idx] -= 1

            i -= 1

        for i in range(n):
            nums[i] = bucket[i]

    def radix_sort(self, nums: List[int]) -> List[int]:
        _min = min(nums)
        if _min < 0:
            for idx in range(len(nums)):
                nums[idx] += -_min

        _max = max(nums)

        exp: int = 0
        while _max // (10**exp) > 0:
            self.radix_el_sort(nums, exp + 1)

            exp += 1

        if _min < 0:
            for idx in range(len(nums)):
                nums[idx] -= -_min

        return nums

    def _index(self, nums: List[int]) -> List[int]:
        _min = min(nums)
        if _min < 0:
            for idx in range(len(nums)):
                nums[idx] += -_min

        _max: int = max(nums)
        bucket: List[int] = [0] * (_max + 1)

        for num in nums:
            bucket[num] += 1

        i: int = 0
        for idx, flag in enumerate(bucket):
            if flag >= 1:
                while flag >= 1:
                    nums[i] = idx

                    i += 1
                    flag -= 1

        if _min < 0:
            for idx in range(len(nums)):
                nums[idx] -= -_min
        return nums


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    # print(s.sortArray([5, 2, 3, 1]))
    assert s.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5], "Test 1"
    assert s.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5], "Test 2"

    # # is_debug = True
    assert s.sortArray(
        [
            -74,
            48,
            -20,
            2,
            10,
            -84,
            -5,
            -9,
            11,
            -24,
            -91,
            2,
            -71,
            64,
            63,
            80,
            28,
            -30,
            -58,
            -11,
            -44,
            -87,
            -22,
            54,
            -74,
            -10,
            -55,
            -28,
            -46,
            29,
            10,
            50,
            -72,
            34,
            26,
            25,
            8,
            51,
            13,
            30,
            35,
            -8,
            50,
            65,
            -6,
            16,
            -2,
            21,
            -78,
            35,
            -13,
            14,
            23,
            -3,
            26,
            -90,
            86,
            25,
            -56,
            91,
            -13,
            92,
            -25,
            37,
            57,
            -20,
            -69,
            98,
            95,
            45,
            47,
            29,
            86,
            -28,
            73,
            -44,
            -46,
            65,
            -84,
            -96,
            -24,
            -12,
            72,
            -68,
            93,
            57,
            92,
            52,
            -45,
            -2,
            85,
            -63,
            56,
            55,
            12,
            -85,
            77,
            -39,
        ]
    ) == [
        -96,
        -91,
        -90,
        -87,
        -85,
        -84,
        -84,
        -78,
        -74,
        -74,
        -72,
        -71,
        -69,
        -68,
        -63,
        -58,
        -56,
        -55,
        -46,
        -46,
        -45,
        -44,
        -44,
        -39,
        -30,
        -28,
        -28,
        -25,
        -24,
        -24,
        -22,
        -20,
        -20,
        -13,
        -13,
        -12,
        -11,
        -10,
        -9,
        -8,
        -6,
        -5,
        -3,
        -2,
        -2,
        2,
        2,
        8,
        10,
        10,
        11,
        12,
        13,
        14,
        16,
        21,
        23,
        25,
        25,
        26,
        26,
        28,
        29,
        29,
        30,
        34,
        35,
        35,
        37,
        45,
        47,
        48,
        50,
        50,
        51,
        52,
        54,
        55,
        56,
        57,
        57,
        63,
        64,
        65,
        65,
        72,
        73,
        77,
        80,
        85,
        86,
        86,
        91,
        92,
        92,
        93,
        95,
        98,
    ], "Test 3"

    arr = [randint(0, 1000000) for _ in range(1_000_000)]

    print("RUNNING...")
    ctime = time()
    s.sortArray(arr.copy())
    print("TIME: ", time() - ctime)
    ctime = time()
    # quickSort(arr.copy(), 0, len(arr) - 1)
    sorted(arr.copy())
    print("TIME: ", time() - ctime)

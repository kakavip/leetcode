#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#
from typing import Dict, List


# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        fre_count: Dict[int, int] = {}
        for num in nums:
            if num not in fre_count:
                fre_count[num] = 0

            fre_count[num] += 1

        rev_fre_count: Dict[int, List[int]] = {}
        for key in fre_count:
            val = fre_count[key]
            if val not in rev_fre_count:
                rev_fre_count[val] = []

            rev_fre_count[val].append(key)

        result: List[int] = []
        for fre in sorted(list(rev_fre_count.keys())):
            for num in sorted(rev_fre_count[fre], reverse=True):
                result.extend([num] * fre)

        fre_count.clear()
        rev_fre_count.clear()

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.frequencySort([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2], "Test 1"
    assert s.frequencySort([2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2], "Test 2"
    assert s.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [
        5,
        -1,
        4,
        4,
        -6,
        -6,
        1,
        1,
        1,
    ], "Test 3"

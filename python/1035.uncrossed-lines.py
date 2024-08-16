#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        _cache: Dict[Tuple[int, int], str] = {}
        m = len(nums1)
        n = len(nums2)

        def lcs(i: int, j: int) -> int:
            if (i, j) in _cache:
                return _cache[(i, j)]

            if i >= m or j >= n:
                return 0

            result: int = 0
            if nums1[i] == nums2[j]:
                result += 1 + lcs(i + 1, j + 1)
            else:
                result += max(lcs(i + 1, j), lcs(i, j + 1))

            _cache[(i, j)] = result
            return result

        return lcs(0, 0)


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2)
    print(s.maxUncrossedLines(nums1=[2, 5, 1, 2, 5], nums2=[10, 5, 2, 1, 5, 2]) == 3)
    print(s.maxUncrossedLines(nums1=[1, 3, 7, 1, 7, 5], nums2=[1, 9, 2, 5, 1]) == 2)

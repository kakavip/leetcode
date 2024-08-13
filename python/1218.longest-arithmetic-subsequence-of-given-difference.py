#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#

# @lc code=start
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # arr = sorted(arr, reverse=difference < 0)
        n = len(arr)
        _max = max(arr)
        _min = min(arr)

        counter: List[int] = [0] * (_max + (0 - _min) + 1)
        n_c: int = _max + (0 - _min) + 1

        for i in range(n):
            idx: int = arr[i] + (0 - _min)
            pre_idx: int = idx - difference
            if 0 <= pre_idx < n_c and counter[pre_idx] >= 1:
                counter[idx] = counter[pre_idx] + 1
            else:
                counter[idx] = 1

        # print(counter)
        return max(counter)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestSubsequence([1, 2, 3, 4], 1) == 4)
    print(s.longestSubsequence([1, 3, 5, 7], 1) == 1)
    print(s.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4)
    print(s.longestSubsequence([3, 0, -3, 4, -4, 7, 6], 3) == 2)

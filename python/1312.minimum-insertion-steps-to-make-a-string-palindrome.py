#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#


# @lc code=start
from typing import Dict, Tuple


class Solution:
    def minInsertions(self, s: str) -> int:
        _cache: Dict[Tuple[int, int], int] = {}
        n: int = len(s)

        def solve(i: int, j: int) -> int:
            if i >= j or i >= n or j < 0:
                return 0

            if (i, j) in _cache:
                return _cache[(i, j)]

            r: int
            # print("i, j: ", i, j)
            if s[i] == s[j]:
                r = solve(i + 1, j - 1)
            else:
                r = 1 + min(solve(i + 1, j), solve(i, j - 1))

            _cache[(i, j)] = r
            return r

        return solve(0, n - 1)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minInsertions("zzazz") == 0)
    print(s.minInsertions("mbadm") == 2)
    print(s.minInsertions("leetcode") == 5)

#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#


# @lc code=start
from typing import Dict, Tuple


class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        new_s: str = s[0]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                new_s += s[i]

        _cache: Dict[Tuple[int, int], int] = {}

        def _calc_printer(start: int, end: int) -> int:
            if start > end:
                return 0

            if (start, end) in _cache:
                return _cache[(start, end)]

            _min_next: int = 1 + _calc_printer(start + 1, end)
            for k in range(start + 1, end + 1):
                if new_s[k] == new_s[start]:
                    _min_parts = _calc_printer(start, k - 1) + _calc_printer(k + 1, end)

                    _min_next = min(_min_parts, _min_next)

            _cache[(start, end)] = _min_next
            return _min_next

        return _calc_printer(0, len(new_s) - 1)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.strangePrinter("aaabbb") == 2)
    print(s.strangePrinter("aba") == 2)

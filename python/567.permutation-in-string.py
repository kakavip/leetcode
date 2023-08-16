#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#


# @lc code=start
from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        _s1_chars = list(s1)
        _s2_chars = list(s2)

        _s1_chars.sort()

        for i in range(len(_s2_chars) - len(_s1_chars) + 1):
            sub_s2_chars: List[str] = _s2_chars[i : i + len(_s1_chars)]
            # print(f"SUB S2 CHARS: {sub_s2_chars}")
            sub_s2_chars.sort()

            if sub_s2_chars == _s1_chars:
                return True

        return False


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("hello", "ooolleoooleh"))

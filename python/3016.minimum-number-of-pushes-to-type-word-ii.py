#
# @lc app=leetcode id=3016 lang=python3
#
# [3016] Minimum Number of Pushes to Type Word II
#


# @lc code=start
from typing import Dict, List

# is_debug: bool = False


class Solution:
    def minimumPushes(self, word: str) -> int:
        fre_chars: List[str] = [0] * 26
        for c in word:
            fre_chars[ord(c) - 97] += 1

        odr_fre_chars = sorted(range(26), key=lambda x: fre_chars[x], reverse=True)
        # is_debug and print(fre_chars)

        cost: int = 0
        fre: int = 0
        for idx in range(26):
            c = odr_fre_chars[idx]
            if idx % 8 == 0:
                fre += 1

            cost += fre * fre_chars[c]

        return cost


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.minimumPushes("abcde") == 5, "Test 1"
    assert s.minimumPushes("xyzxyzxyzxyz") == 12, "Test 2"
    # is_debug = True
    # print(s.minimumPushes("aabbccddeeffgghhiiiiii"))
    assert s.minimumPushes("aabbccddeeffgghhiiiiii") == 24, "Test 4"

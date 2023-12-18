#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#


# @lc code=start
from typing import Dict, List


class Solution:
    def frequencySort(self, s: str) -> str:
        unique_chars = []
        w_fre_map: Dict[str, int] = {}
        for c in s:
            if c not in w_fre_map:
                w_fre_map[c] = 0
                unique_chars.append(c)
            w_fre_map[c] += 1

        result: str = ""
        for c in sorted(unique_chars, key=lambda x: -w_fre_map[x]):
            result += c * w_fre_map[c]

        return result


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("tree"))

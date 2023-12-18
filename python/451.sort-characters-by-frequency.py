#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#


# @lc code=start
from typing import Dict, List


class Solution:
    def frequencySort(self, s: str) -> str:
        w_fre_map: Dict[str, int] = {}
        for c in s:
            if c not in w_fre_map:
                w_fre_map[c] = 0
            w_fre_map[c] += 1

        fre_map: Dict[int, List[str]] = {}
        for c in w_fre_map.keys():
            if w_fre_map[c] not in fre_map:
                fre_map[w_fre_map[c]] = []

            fre_map[w_fre_map[c]].append(c)

        result: str = ""
        for fre in sorted(list(fre_map.keys()), key=lambda x: -x):
            for c in fre_map[fre]:
                result += c * fre

        return result


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("tree"))

#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
from typing import Dict, List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result: List[str] = []

        s1s = s1.split()
        s2s = s2.split()

        counter_map: Dict[str, int] = {}
        for s in s1s + s2s:
            if s not in counter_map:
                counter_map[s] = 0
            counter_map[s] += 1

        for s in counter_map:
            if counter_map[s] == 1:
                result.append(s)

        return result


# @lc code=end

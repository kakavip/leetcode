#
# @lc app=leetcode id=2416 lang=python3
#
# [2416] Sum of Prefix Scores of Strings
#

# @lc code=start
from typing import Dict, List


class Solution:
    prefix_counter: Dict[str, int] = {}

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.prefix_counter.clear()

        for w in words:
            for i in range(1, len(w) + 1):
                c_w: str = w[:i]
                if c_w not in self.prefix_counter:
                    self.prefix_counter[c_w] = 0

                self.prefix_counter[c_w] += 1

        result: List[int] = [0] * len(words)
        for idx, w in enumerate(words):
            r: int = 0
            for i in range(1, len(w) + 1):
                r += self.prefix_counter[w[:i]]
            result[idx] = r

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.sumPrefixScores(["abc", "ab", "bc", "b"]) == [5, 4, 3, 2])
    print(s.sumPrefixScores(["abcd"]) == [4])

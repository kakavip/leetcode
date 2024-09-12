#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)

        counter: int = 0
        for w in words:
            if not (set(w) - a):
                counter += 1

        return counter


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))

#
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#

# @lc code=start
from typing import Dict


class Solution:
    _cache: Dict[int, str] = {1: "0"}
    _max: int = 1

    def findKthBit(self, n: int, k: int) -> str:
        if n > self._max:
            for i in range(self._max + 1, n + 1):
                self._cache[i] = (
                    self._cache[i - 1] + "1" + self.get_revert_s(self._cache[i - 1])
                )
            
            self._max = n

        return self._cache[n][k - 1]

    @staticmethod
    def get_revert_s(s) -> str:
        n_s: str = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                n_s += "0"
            else:
                n_s += "1"
        return n_s


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findKthBit(3, 1) == "0")
    print(s.findKthBit(4, 11) == "1")

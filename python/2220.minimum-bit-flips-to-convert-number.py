#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#


# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s_bin: str = format(start, "b")
        g_bin: str = format(goal, "b")

        _size: int = max(len(s_bin), len(g_bin))
        g_bin = "0" * (_size - len(g_bin)) + g_bin
        s_bin = "0" * (_size - len(s_bin)) + s_bin

        r: int = 0

        for i in range(_size):
            if s_bin[i] != g_bin[i]:
                r += 1

        return r


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minBitFlips(10, 7) == 3)
    print(s.minBitFlips(3, 4) == 3)

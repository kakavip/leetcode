#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
def countNumDecodings(s: str) -> int:
    if len(s) == 0:
        return 1
    # '0' or 'x'
    if len(s) == 1:
        if s[0] == '0':
            return 0
        return 1
    other_way = 0
    # Count for 'x'
    if s[0] == '0':
        return 0
    else:
        if int(s[0:2]) <= 26:
            other_way = countNumDecodings(s[2:])
        return countNumDecodings(s[1:]) + other_way
class Solution:
    def numDecodings(self, s: str) -> int:
        return countNumDecodings(s)
# @lc code=end

if __name__ == "__main__":
    a = Solution()
    print("result: ", a.numDecodings("9317949759856497357254398763219839323723136763131916377913495416692666785978758414629119614215967159"))
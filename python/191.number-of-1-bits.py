#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([int(x) for x in list("{0:b}".format(n))])


# @lc code=end

if __name__ == "__main__":
    pass

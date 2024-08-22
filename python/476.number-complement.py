#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#


# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        return int(
            "".join(map(lambda x: x == "0" and "1" or "0", list(format(num, "b")))), 2
        )


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findComplement(5))
    print(s.findComplement(1))

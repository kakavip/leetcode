#
# @lc app=leetcode id=1945 lang=python3
#
# [1945] Sum of Digits of String After Convert
#


# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        int_val: str = ""
        for c in s:
            int_val += str(ord(c) - 96)

        while k > 0:
            _sum: int = 0
            for i in int_val:
                _sum += int(i)

            int_val = str(_sum)
            k -= 1

        # print(int_val)

        return int(int_val)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.getLucky("zbax", 2) == 8)
    print(s.getLucky("iiii", 1) == 36)
    print(s.getLucky("leetcode", 2) == 6)
    print(s.getLucky("zbax", 2) == 8)

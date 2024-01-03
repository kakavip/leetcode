#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#


# @lc code=start
from typing import Tuple


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        v1, i1 = parse_complex_number(num1)
        v2, i2 = parse_complex_number(num2)

        v3 = v1 * v2 + i1 * i2 * -1
        i3 = i1 * v2 + i2 * v1

        return f"{v3}+{i3}i"


def parse_complex_number(num: str) -> Tuple[int, int]:
    parts = num.split("+")
    return int(parts[0]), int(parts[1].replace("i", ""))


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.complexNumberMultiply("1+1i", "1+1i"))
    print(s.complexNumberMultiply("1+-1i", "1+-1i"))

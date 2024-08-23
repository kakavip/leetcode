#
# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#


# @lc code=start
import math
from typing import List, Tuple


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions: List[str] = expression.split("+")
        n_fractions: List[str] = []
        for fraction in fractions:
            sub_fractions = fraction.split("-")
            if sub_fractions[0]:
                n_fractions.append(sub_fractions[0])
            for str_fraction in sub_fractions[1:]:
                n_fractions.append("-" + str_fraction)

        num_fractions: List[List[int]] = []
        for fraction in n_fractions:
            num_fraction: List[int] = []
            for num in fraction.split("/"):
                num_fraction.append(int(num))

            num_fractions.append(num_fraction)

        denominors: List[int] = []
        for num in num_fractions:
            denominors.append(num[-1])
        bcnn = math.lcm(*denominors[:2])
        for deno in denominors[2:]:
            bcnn = math.lcm(bcnn, deno)

        numerator_sum: int = 0
        for num in num_fractions:
            num[0] *= bcnn // num[-1]
            num[-1] = bcnn

            numerator_sum += num[0]

        if numerator_sum % bcnn == 0:
            return str(numerator_sum // bcnn) + "/1"

        ucln = abs(numerator_sum * bcnn) // math.lcm(numerator_sum, bcnn)
        numerator_sum //= ucln
        bcnn //= ucln

        return str(numerator_sum) + "/" + str(bcnn)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.fractionAddition("-1/2+1/2") == "0/1")
    print(s.fractionAddition("-1/2+1/2+1/3") == "1/3")
    print(s.fractionAddition("1/3-1/2") == "-1/6")

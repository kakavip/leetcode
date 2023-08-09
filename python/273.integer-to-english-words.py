#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
from typing import Dict, List


class Solution:
    def numberToWords(self, num: int) -> str:
        normal_group: Dict[int, str] = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        hundred_group: Dict[int, str] = {
            100: "Hundred",
            1000: "Thousand",
            1_000_000: "Million",
        }
        three_group: List[str] = ["Thousand", "Million", "Billion"]
        teen_group: Dict[int, str] = {
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        ty_group: Dict[int, str] = {
            10: "Ten",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        if num == 0:
            return "Zero"

        result: str = ""

        num_three_group: int = 1
        while True:
            part_r: str = ""
            surplus: int = num % 1_000
            # print(f"SURPLUS: {surplus}")

            if surplus > 0:
                if surplus / 100 >= 1:
                    part_r += f"{normal_group[int(surplus/100)]} Hundred "
                ty_surplus: int = surplus % 100
                if ty_surplus in teen_group.keys():
                    part_r += f"{teen_group[ty_surplus]} "
                elif 0 < ty_surplus < 10:
                    part_r += f"{normal_group[ty_surplus]} "
                else:
                    if int(ty_surplus / 10) * 10 in ty_group:
                        part_r += f"{ty_group[int(ty_surplus/10) * 10]} "
                    if ty_surplus % 10 > 0:
                        # print(f"NUMBUER {ty_surplus} - {ty_surplus % 10}")
                        part_r += f"{normal_group[ty_surplus%10]} "

                three_r: str = ""
                if num_three_group > 1:
                    if num_three_group - 2 < len(three_group):
                        three_r = f"{three_group[num_three_group - 2]} "
                result = part_r + three_r + result

            num = int(num / 1_000)
            num_three_group += 1

            if num <= 0:
                break

        return result.strip()


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.numberToWords(100))

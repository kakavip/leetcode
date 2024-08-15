#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
from typing import Dict, List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        budget_counters: Dict[int, int] = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 5:
                budget_counters[bill] += 1
                continue

            n_bill: int = bill - 5
            for price in [20, 10, 5]:
                while budget_counters[price] > 0 and n_bill - price >= 0:
                    n_bill -= price
                    budget_counters[price] -= 1

            if n_bill > 0:
                return False

            budget_counters[bill] += 1

        return True


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.lemonadeChange([5, 5, 5, 10, 20]) == True)
    print(s.lemonadeChange([5, 5, 10, 10, 20]) == False)

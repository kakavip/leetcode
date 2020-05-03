from typing import List

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max: int = 0
        max_range: int = len(prices)
        while max_range > 0:
            _min: int = min(prices[:max_range])
            _max: int = max(prices[prices.index(_min):])
            profit: int = _max - _min
            if profit > profit_max:
                profit_max = profit
            max_range = prices.index(_min)
        return profit_max


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    result = s.maxProfit([7, 6, 4, 3, 1])
    print("Result: ", result)
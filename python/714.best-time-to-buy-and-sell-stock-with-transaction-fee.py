#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp: List[List[int]] = [[-float("inf")] * 2 for _ in range(n + 1)]
        dp[0] = [0, -float("inf")]
        for idx in range(n):
            # buy
            if dp[idx][0] != -float("inf"):
                dp[idx + 1][0] = max(dp[idx + 1][0], dp[idx][0])
                dp[idx + 1][1] = max(dp[idx + 1][1], dp[idx][0] - prices[idx] - fee)

            # sell
            if dp[idx][1] != -float("inf"):
                dp[idx + 1][1] = max(dp[idx + 1][1], dp[idx][1])
                dp[idx + 1][0] = max(dp[idx + 1][0], dp[idx][1] + prices[idx])

        # print(dp)
        return max(dp[-1])


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8)
    print(s.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6)

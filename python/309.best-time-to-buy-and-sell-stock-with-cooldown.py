#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n: int = len(prices)

        dp: List[List[int]] = [[-float("inf")] * 3 for _ in range(n + 1)]
        dp[0] = [0, -float("inf"), -float("inf")]  # buy / sell / coutdown
        for idx in range(n):
            # buy
            if dp[idx][0] != -float("inf"):
                dp[idx + 1][1] = max(dp[idx + 1][1], dp[idx][0] - prices[idx])
                dp[idx + 1][0] = max(dp[idx + 1][0], dp[idx][0])
            # sell
            if dp[idx][1] != -float("inf"):
                dp[idx + 1][1] = max(dp[idx + 1][1], dp[idx][1])
                dp[min(idx + 2, n)][0] = max(
                    dp[min(idx + 2, n)][0], dp[idx][1] + prices[idx]
                )
                dp[idx + 1][2] = max(dp[idx][2], dp[idx][1] + prices[idx])

        # print(dp)

        return max(dp[-1])


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]) == 3)
    print(s.maxProfit([1]) == 0)
    print(s.maxProfit([1, 2]) == 1)
    print(
        s.maxProfit(
            [
                48,
                12,
                60,
                93,
                97,
                42,
                25,
                64,
                17,
                56,
                85,
                93,
                9,
                48,
                52,
                42,
                58,
                85,
                81,
                84,
                69,
                36,
                1,
                54,
                23,
                15,
                72,
                15,
                11,
                94,
            ]
        )
        == 428
    )

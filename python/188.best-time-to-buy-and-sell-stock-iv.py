#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
from typing import List


class Solution:
    _min: int = -float("inf")

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp: List[List[List[int]]] = [[] for _ in range(n + 1)]
        for c in dp:
            c.append([self._min] * (k + 1))
            c.append([self._min] * (k + 1))

        dp[0][0][0] = 0

        for idx in range(n):
            # dp.append([])
            # # buy 1, buy 2, buy 3
            # dp[idx + 1].append([-float("inf")] * min(k, len(dp[idx][0]) + 1))
            # # sell 1, sell 2, sell 3
            # dp[idx + 1].append([-float("inf")] * min(k, len(dp[idx][1]) + 1))

            # buy
            for i, buy in enumerate(dp[idx][0]):
                if buy == self._min:
                    break

                dp[idx + 1][0][i] = max(dp[idx + 1][0][i], dp[idx][0][i])
                if i < k:
                    dp[idx + 1][1][i] = max(
                        dp[idx + 1][1][i], dp[idx][0][i] - prices[idx]
                    )

            # sell
            for i, sell in enumerate(dp[idx][1]):
                if sell == self._min:
                    break

                dp[idx + 1][1][i] = max(dp[idx + 1][1][i], dp[idx][1][i])
                if i < k:
                    dp[idx + 1][0][i + 1] = max(
                        dp[idx + 1][0][i + 1], dp[idx][1][i] + prices[idx]
                    )

        return max(*dp[-1][0], *dp[-1][1])


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(2, [2, 4, 1]) == 2)
    print(s.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7)

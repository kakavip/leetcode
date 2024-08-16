#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] += 1

                    if i < m - 1 and j < n - 1:
                        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
                    # if j == n - 1 and i < m - 1:
                    #     dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                    # if i == m - 1 and j < n - 1:
                    #     dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
                else:
                    if i < m - 1:
                        dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
                    if j < n - 1:
                        dp[i][j + 1] = max(dp[i][j], dp[i][j + 1])

        for i in range(1, m):
            dp[i][n - 1] = max(dp[i][n - 1], dp[i - 1][n - 1])

        for j in range(1, n):
            dp[m - 1][j] = max(dp[m - 1][j], dp[m - 1][j - 1])

        # print(dp)
        return dp[m - 1][n - 1]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace") == 3)
    print(s.longestCommonSubsequence("abc", "abc") == 3)
    print(s.longestCommonSubsequence("abc", "def") == 0)
    print(s.longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr") == 5)
    print(
        s.longestCommonSubsequence(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        )
        == 210
    )

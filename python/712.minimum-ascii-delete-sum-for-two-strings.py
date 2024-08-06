#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#


# @lc code=start
from typing import List

is_debug: bool = False


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        mask: List[List[int]] = [[1] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    mask[i][j] = 0
                else:
                    mask[i][j] = 1

        dp: List[List[int]] = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0

        # zero: bool = False
        for i in range(m):
            if mask[i][0] == 0:
                dp[i + 1][0] = dp[i][0]
            else:
                dp[i + 1][0] = dp[i][0] + ord(s1[i])

            if i >= 1 and mask[i - 1][0] == 0:
                dp[i + 1][0] += ord(s1[i - 1])

            # if not zero:
            #     if mask[i][0] == 0:
            #         zero = True
            #         dp[i + 1][0] = dp[i][0]
            #     else:
            #         dp[i + 1][0] = dp[i][0] + ord(s1[i])
            # else:
            #     dp[i + 1][0] = dp[i][0] + ord(s1[i])

        # zero = False
        for i in range(n):
            if mask[0][i] == 0:
                dp[0][i + 1] = dp[0][i]
            else:
                dp[0][i + 1] = dp[0][i] + ord(s2[i])

            if i >= 1 and mask[0][i - 1] == 0:
                dp[0][i + 1] += ord(s2[i - 1])

            # if not zero:
            #     if mask[0][i] == 0:
            #         zero = True
            #         dp[0][i + 1] = dp[0][i]
            #     else:
            #         dp[0][i + 1] = dp[0][i] + ord(s2[i])
            # else:
            #     dp[0][i + 1] = dp[0][i] + ord(s2[i])

        is_debug and print(mask)
        is_debug and print(dp)

        for i in range(m + 1):
            for j in range(n + 1):
                if i >= 1 and mask[i][j] != 0 and j < n:
                    dp[i][j + 1] = min(dp[i][j] + ord(s2[j]) * mask[i][j], dp[i][j + 1])

                if j >= 1 and mask[i][j] != 0 and i < m:
                    dp[i + 1][j] = min(dp[i][j] + ord(s1[i]) * mask[i][j], dp[i + 1][j])

                if j < n and i < m:
                    addition: int = 0
                    if i == 0 and j >= 1 and mask[i][j] == 0 and mask[i][j - 1] == 0:
                        addition += ord(s2[j - 1])
                    if i >= 1 and j == 0 and mask[i][j] == 0 and mask[i - 1][j] == 0:
                        addition += ord(s1[i - 1])

                    dp[i + 1][j + 1] = min(
                        dp[i][j] + (ord(s1[i]) + ord(s2[j])) * mask[i][j] + addition,
                        dp[i + 1][j + 1],
                    )

        # for i in range(m):
        #     dp[i+1][n-1] = min(dp[i+1][n-1], dp[i][n-1] + ord(s1[i]))

        # for i in range(n):
        #     dp[m-1][i+1] = min(dp[m-1][i+1], dp[m-1][i] + ord(s2[i]))

        is_debug and print(dp)

        return dp[m][n]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.minimumDeleteSum("sea", "eat") == 231, "Test 1"
    assert s.minimumDeleteSum("delete", "leet") == 403, "Test 2"
    assert s.minimumDeleteSum("sjfqkfxqoditw", "fxymelgo") == 1638, "Test 3"

    is_debug = True
    assert s.minimumDeleteSum("ikkwcrjtazuwu", "khuqi") == 1543, "Test 4"

# [
#     [1, 1, 1, 1, 0, 1],
#     [0, 1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
# ]
# [
#     [0, 107, 211, 328, 441, 441],
#     [105, inf, inf, inf, inf, inf],
#     [105, inf, inf, inf, inf, inf],
#     [212, inf, inf, inf, inf, inf],
#     [438, inf, inf, inf, inf, inf],
#     [537, inf, inf, inf, inf, inf],
#     [651, inf, inf, inf, inf, inf],
#     [757, inf, inf, inf, inf, inf],
#     [873, inf, inf, inf, inf, inf],
#     [970, inf, inf, inf, inf, inf],
#     [1092, inf, inf, inf, inf, inf],
#     [1209, inf, inf, inf, inf, inf],
#     [1328, inf, inf, inf, inf, inf],
#     [1445, inf, inf, inf, inf, inf],
# ]
# [
#     [0, 107, 211, 328, 441, 441],
#     [105, 212, 316, 433, 546, 441],
#     [105, 105, 209, 326, 439, 544],
#     [212, 105, 209, 326, 439, 544],
#     [438, 224, 328, 445, 558, 663],
#     [537, 323, 427, 544, 657, 762],
#     [651, 437, 541, 658, 771, 876],
#     [757, 543, 647, 764, 877, 982],
#     [873, 659, 763, 880, 993, 1098],
#     [970, 756, 860, 977, 1090, 1195],
#     [1092, 878, 982, 1099, 1212, 1317],
#     [1209, 995, 1099, 982, 1095, 1200],
#     [1328, 1114, 1218, 1101, 1214, 1319],
#     [1445, 1231, 1335, 1218, 1331, 1436],
# ]

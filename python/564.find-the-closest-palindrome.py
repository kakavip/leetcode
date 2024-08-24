#
# @lc app=leetcode id=564 lang=python3
#
# [564] Find the Closest Palindrome
#


# @lc code=start


from typing import List


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n) - 1)

        new_n = list(n)
        start, end = 0, len(n) - 1
        while start <= end:
            if new_n[start] != new_n[end]:
                new_n[end] = new_n[start]

            start += 1
            end -= 1

        new_n = "".join(new_n)
        new_n2 = "9" * (len(n) - 1)
        new_n3 = "1" + "0" * (len(n) - 1) + "1"

        results: List[str] = [new_n, new_n2, new_n3]
        if int(new_n[len(n) // 2]) >= 1:
            new_n4 = list(new_n)
            if len(n) % 2 == 0:
                new_n4[len(n) // 2] = new_n4[len(n) // 2 - 1] = str(
                    int(new_n4[len(n) // 2 - 1]) - 1
                )
            else:
                new_n4[len(n) // 2] = str(int(new_n4[len(n) // 2]) - 1)
            results.append("".join(new_n4))

        if int(new_n[len(n) // 2]) == 0:
            new_n4 = list(new_n)
            if len(n) % 2 == 0:
                new_n4[len(n) // 2] = new_n4[len(n) // 2 - 1] = "9"

                if int(new_n4[len(n) // 2 - 2]) > 0:
                    new_n4[len(n) // 2 + 1] = new_n4[len(n) // 2 - 2] = str(
                        int(new_n4[len(n) // 2 - 2]) - 1
                    )
            else:
                new_n4[len(n) // 2] = "9"
                if int(new_n4[len(n) // 2 + 1]) > 0:
                    new_n4[len(n) // 2 + 1] = new_n4[len(n) // 2 - 1] = str(
                        int(new_n4[len(n) // 2 - 1]) - 1
                    )

            results.append("".join(new_n4))

        if int(new_n[len(n) // 2]) <= 8:
            new_n4 = list(new_n)
            if len(n) % 2 == 0:
                new_n4[len(n) // 2] = new_n4[len(n) // 2 - 1] = str(
                    int(new_n4[len(n) // 2 - 1]) + 1
                )
            else:
                new_n4[len(n) // 2] = str(int(new_n4[len(n) // 2]) + 1)
            results.append("".join(new_n4))

        min_value: str = "0"
        min_diff: int = float("inf")
        for v in sorted(filter(lambda x: x != n, results), key=int):
            if min_diff > abs(int(v) - int(n)):
                min_value = v
                min_diff = abs(int(v) - int(n))

        return min_value


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.nearestPalindromic("123") == "121")
    print(s.nearestPalindromic("1") == "0")
    print(s.nearestPalindromic("11") == "9")
    print(s.nearestPalindromic("88") == "77")
    print(s.nearestPalindromic("99") == "101")
    print(s.nearestPalindromic("9009") == "8998")
    print(s.nearestPalindromic("10001") == "9999")

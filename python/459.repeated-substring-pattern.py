#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#


# @lc code=start


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False
        if n == 2:
            return set(s) == {s[0]}

        for i in range(n // 2 + 1):
            if n % (i + 1) != 0:
                continue

            if s.split(s[: i + 1]) == [""] * (n // (i + 1) + 1):
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.repeatedSubstringPattern("abcabcabcabc"))
    print(s.repeatedSubstringPattern("abab"))
    # print(s.repeatedSubstringPattern("bb"))
    print(s.repeatedSubstringPattern("ab"))
    print(s.repeatedSubstringPattern("aa"))
    # print(s.repeatedSubstringPattern("abaababaab"))

#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#


# @lc code=start
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if len(s) < len(p):
        #     return False

        # n_p = len(p)
        # p_idx = 0
        # regex_pattern: str = ""
        # while p_idx < n_p:
        #     c = p[p_idx]
        #     if (p_idx < n_p - 1) and p[p_idx + 1] == "*":
        #         if c != ".":
        #             regex_pattern += "{}*".format(c)
        #         else:
        #             regex_pattern += ".*"

        #         p_idx += 2

        #     else:
        #         regex_pattern += c
        #         p_idx += 1

        # n_s = len(s)
        # n_p = len(p)
        # s_idx: int = 0
        # p_idx: int = 0

        # while p_idx < n_p:
        #     c = p[p_idx]

        #     if (p_idx < n_p - 1) and p[p_idx + 1] == "*":
        #         if c != ".":
        #             while s_idx < n_s and s[s_idx] == c:
        #                 s_idx += 1
        #         else:
        #             if p_idx < n_p - 2:
        #                 while s_idx < n_s and s[s_idx] != p[p_idx + 2]:
        #                     s_idx += 1
        #             else:
        #                 return True

        #         p_idx += 2
        #     else:
        #         if c != s[s_idx] and c != ".":
        #             return False
        #         else:
        #             s_idx += 1
        #             p_idx += 1

        #     if s_idx >= n_s:
        #         break

        # # print(p_idx, s_idx)

        # if p_idx != n_p or s_idx != n_s:
        #     return False

        # print(regex_pattern == p)
        regex = re.compile(re.sub("[*]+", "*", p))

        if regex.fullmatch(s):
            return True

        return False


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    assert s.isMatch("aa", "a") == False, "Test 1"
    assert s.isMatch("aa", "a*") == True, "Test 2"
    assert s.isMatch("ab", ".*") == True, "Test 3"
    assert s.isMatch("aab", "c*a*b") == True, "Test 4"
    assert s.isMatch("ab", ".*c") == False, "Test 5"
    assert s.isMatch("aaa", "a*a") == True, "Test 6"
    assert s.isMatch("mississippi", "mis*is*ip*.") == True, "Test 6"
    assert s.isMatch("abc", "a***abc") == True, "Test 6"

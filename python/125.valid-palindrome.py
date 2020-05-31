#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-z0-9]", "", s.lower())

        return s[::-1] == s


# @lc code=end

if __name__ == "__main__":
    s = Solution()

    result: bool = s.isPalindrome("A man, a plan, a canal: Panama")

    print(result)

#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
from typing import List


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        if len(s) < len(p):
            return result

        p_word_map = {}
        slide_word_map = {}
        for i in range(len(p)):
            if p[i] not in p_word_map:
                p_word_map[p[i]] = 0
            p_word_map[p[i]] += 1

            if s[i] not in slide_word_map:
                slide_word_map[s[i]] = 0
            slide_word_map[s[i]] += 1

        if p_word_map == slide_word_map:
            result.append(0)

        for i in range(1, len(s) - len(p) + 1):
            slide_word_map[s[i - 1]] = slide_word_map[s[i - 1]] - 1
            if slide_word_map[s[i - 1]] <= 0:
                slide_word_map.pop(s[i - 1])

            if s[i + len(p) - 1] not in slide_word_map:
                slide_word_map[s[i + len(p) - 1]] = 0

            slide_word_map[s[i + len(p) - 1]] += 1

            if p_word_map == slide_word_map:
                result.append(i)

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abab", "ab"))
    print(s.findAnagrams("aaaaaaaaaa", "ab"))

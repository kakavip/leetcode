#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        word_list.reverse()
        return " ".join(word_list)


# @lc code=end

if __name__ == "__main__":
    pass

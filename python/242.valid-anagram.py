#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#



# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(list(s)) == sorted(list(t))
        
# @lc code=end

if __name__ == "__main__":
    s =Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("cat", "ccat"))
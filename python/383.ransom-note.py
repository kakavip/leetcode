#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_map = {}
        for c in ransomNote:
            if c not in c_map:
                c_map[c] = 0
            c_map[c] += 1

        for c in magazine:
            if c not in c_map:
                continue

            c_map[c] -= 1
            if c_map[c] <= 0:
                c_map.pop(c)

            if not c_map:
                break

        return not c_map


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("a", "b"))
    print(s.canConstruct("aa", "aab"))

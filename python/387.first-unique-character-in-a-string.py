#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


# @lc code=start
from typing import Dict, List, Union


class Solution:
    def firstUniqChar(self, s: str) -> int:
        characters = list(s)

        data: Dict[str, Union[int, bool]] = {}

        for idx, c in enumerate(characters):
            if c not in data.keys():
                data.update({c: idx})
            else:
                if data[c] >= 0:
                    data[c] = -1 * data[c] - 1

        indexes: List[int] = sorted(filter(lambda x: x >= 0, data.values()))
        # print(f"INDEX: {indexes}")

        return not indexes and -1 or indexes[0]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("aabb"))
    print(s.firstUniqChar("loveleetcode"))
    print(s.firstUniqChar("leetcode"))

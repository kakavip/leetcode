#
# @lc app=leetcode id=2491 lang=python3
#
# [2491] Divide Players Into Teams of Equal Skill
#

# @lc code=start
from typing import Dict, List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n: int = len(skill)
        _sum: int = sum(skill)

        num_parse: int = int(_sum * 2 / n)
        _map: Dict[int, int] = {}
        for v in skill:
            if v not in _map:
                _map[v] = 0
            _map[v] += 1

        r: int = 0
        for v in skill:
            if not _map[v]:
                continue

            remain: int = num_parse - v
            if remain not in _map or not _map[remain]:
                return -1

            if remain == v:
                if _map[remain] % 2 != 0:
                    return -1

            _map[remain] -= 1
            _map[v] -= 1
            r += v * remain

        return r


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.dividePlayers(skill=[3, 2, 5, 1, 3, 4]) == 22)
    print(s.dividePlayers(skill=[3, 4]) == 12)
    print(s.dividePlayers(skill=[1, 1, 2, 3]) == -1)
    print(s.dividePlayers(skill=[1, 4, 4, 1]) == 8)

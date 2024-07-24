#
# @lc app=leetcode id=2191 lang=python3
#
# [2191] Sort the Jumbled Numbers
#
from typing import Dict, List


# @lc code=start


def map_num(num: int, idx_map: Dict[int, int]) -> int:
    r = ""
    for v in str(num):
        r += str(idx_map[int(v)])

    return int(r)


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        idx_map: Dict[int, int] = {}
        for idx, v in enumerate(mapping):
            idx_map[idx] = v

        return sorted(nums, key=lambda x: map_num(x, idx_map))


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.sortJumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]) == [
        338,
        38,
        991,
    ], "Test 1"

    assert s.sortJumbled([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123]) == [
        123,
        456,
        789,
    ], "Test 2"

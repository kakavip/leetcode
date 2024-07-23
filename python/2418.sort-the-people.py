#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#
from typing import Dict, List


# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_map: Dict[int, List[str]] = {}
        for idx, name in enumerate(names):
            if heights[idx] not in height_map:
                height_map[heights[idx]] = []
            height_map[heights[idx]].append(name)

        result: List[str] = []
        for h in sorted(list(height_map.keys()), reverse=True):
            result.extend(height_map[h])

        return result


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    assert s.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]) == [
        "Mary",
        "Emma",
        "John",
    ], "Test 1"

    assert s.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]) == [
        "Bob",
        "Alice",
        "Bob",
    ], "Test 2"

#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random


class RandomizedSet:
    _array = []
    _map = {}

    def __init__(self):
        self._array = []
        self._map = {}

    def insert(self, val: int) -> bool:
        is_existed = self._map.get(val, None)
        if not is_existed:
            self._map[val] = True

        return not is_existed

    def remove(self, val: int) -> bool:
        is_existed = self._map.get(val, None)
        if is_existed:
            del self._map[val]

        return is_existed

    def getRandom(self) -> int:
        return random.choice(list(self._map.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

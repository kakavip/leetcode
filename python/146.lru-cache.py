#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

import time
from typing import List


class CacheData:
    val: int = 0
    updated_at: float = 0.0

    def __init__(self, val: int):
        self.val = val
        self.updated_at = time.time()

    def update(self):
        self.updated_at = time.time()

    def __str__(self):
        return self.val


class LRUCache:
    capacity: int = 0
    hash_data: dict = dict()
    _list: List[CacheData] = []

    def __init__(self, capacity: int):
        self.hash_data = dict()
        self._list = list()
        self.capacity = capacity
        pass

    def get(self, key: int) -> int:
        # self.log(f"GET ${key}")

        existed_keys_in_list = [c.val for c in self._list]
        if key in existed_keys_in_list:
            self._list[existed_keys_in_list.index(key)].update()
            return self.hash_data[key]

        return -1

    def put(self, key: int, value: int) -> None:
        self.hash_data.update({key: value})

        existed_keys_in_list = [c.val for c in self._list]
        if key not in existed_keys_in_list:
            self._list.append(CacheData(key))
        else:
            self._list[existed_keys_in_list.index(key)].update()

        # self.log(f"PUT {key}: {value} |")

        if len(self._list) > self.capacity:

            def select_by_updated_at(c: CacheData):
                return c.updated_at

            self._list.sort(key=select_by_updated_at)

            self._list = self._list[len(self._list) - self.capacity :]

    def log(self, prefix: str) -> None:
        print(f" {prefix} --> Cache: {self.hash_data} --> Capacity: {self.capacity}")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

if __name__ == "__main__":
    pass

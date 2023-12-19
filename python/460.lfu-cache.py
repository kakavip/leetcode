#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#


# @lc code=start
from collections import deque
from typing import Dict, List


class LFUCache:
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.capacity = 0

        self.fr_queue: Dict[int, List[int]] = {}
        self.cache = {}
        self.counter_map = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.counter_map[key] += 1

            self.update_fr_queue(key)
            return self.cache[key]
        return -1

    def update_fr_queue(self, key):
        c = self.counter_map[key]
        if c not in self.fr_queue:
            self.fr_queue[c] = deque([])

        self.fr_queue[c].appendleft(key)

    def invalidated(self):
        counter = 1

        while True:
            try:
                key = self.fr_queue[counter].pop()

                if key in self.counter_map and counter == self.counter_map[key]:
                    self.cache.pop(key)
                    self.counter_map.pop(key)

                    return
            except IndexError:
                counter += 1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.counter_map[key] += 1

            self.update_fr_queue(key)
        else:
            if self.capacity >= self.max_capacity:
                self.invalidated()
            else:
                self.capacity += 1

            self.cache.update({key: value})
            self.counter_map.update({key: 1})

            self.update_fr_queue(key)

        return None


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

if __name__ == "__main__":
    s = LFUCache(2)
    s.put(1, 1)
    s.put(2, 2)
    print(s.get(1))
    s.put(3, 3)
    print(s.get(2))
    print(s.get(3))
    s.put(4, 4)
    print(s.get(1))
    print(s.get(3))
    print(s.get(4))

#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#


# @lc code=start
import bisect
from typing import List, Tuple


class MyCalendar:
    events: List[Tuple[int, int]]
    n: int

    def __init__(self):
        self.events = []
        self.n = 0

    def is_conflict(self, a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        return not (b[1] <= a[0] or b[0] >= a[1])

    def book(self, start: int, end: int) -> bool:
        if not self.events:
            self.events.append((start, end))
            self.n = 1
            return True

        n_book: Tuple[int, int] = (start, end)

        idx: int = bisect.bisect_left(self.events, start, key=lambda x: x[0])
        if idx == self.n:
            if self.events[self.n - 1][1] > start:
                return False
        else:
            if self.is_conflict(self.events[idx], n_book):
                return False
            if idx > 0 and self.is_conflict(self.events[idx - 1], n_book):
                return False

        self.events.insert(idx, n_book)
        self.n += 1
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

if __name__ == "__main__":
    s = MyCalendar()
    print(s.book(47, 50))
    print(s.book(33, 41))
    print(s.book(39, 45))
    print(s.book(33, 42))
    print(s.book(25, 32))
    print(s.book(26, 35))
    print(s.book(19, 25))
    print(s.book(3, 8))
    print(s.book(8, 13))
    print(s.book(18, 27))

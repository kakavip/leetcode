#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from typing import List, Optional


class MyQueue:
    _stack_base: List[int]
    _stack_clone: List[int]

    def __init__(self):
        self._stack_base = []
        self._stack_clone = []

    def push(self, x: int) -> None:
        if len(self._stack_clone):
            while len(self._stack_clone):
                self._stack_base.append(self._stack_clone.pop())

        self._stack_base.append(x)

    def pop(self) -> int:
        if not (len(self._stack_base) or len(self._stack_clone)):
            return None

        front: Optional[int] = None
        if len(self._stack_base):
            while len(self._stack_base):
                self._stack_clone.append(self._stack_base.pop())

        front = self._stack_clone.pop()

        return front

    def peek(self) -> int:
        if not (len(self._stack_base) or len(self._stack_clone)):
            return None

        front: Optional[int] = None
        if len(self._stack_base):
            while len(self._stack_base):
                self._stack_clone.append(self._stack_base.pop())

        front = self._stack_clone.pop()
        self._stack_clone.append(front)

        return front

    def empty(self) -> bool:
        return not (len(self._stack_base) or len(self._stack_clone))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

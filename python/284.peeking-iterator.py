#
# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.cur_pointer = 0
        self.length = len(nums)

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

        return self.cur_pointer < self.length

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        r = self.nums[self.cur_pointer]
        self.cur_pointer += 1

        return r


# @lc code=start
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator

        self.data = []
        self.cur_pointer = -1
        self.temp_cache = 0

        if iterator.hasNext():
            self.data.append(iterator.next())
            self.temp_cache += 1

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # print(self.cur_pointer, self.temp_cache)
        return self.data[self.cur_pointer + 1]

    def next(self):
        """
        :rtype: int
        """
        _next = self.data[self.cur_pointer + 1]
        if self.iterator.hasNext():
            self.data.append(self.iterator.next())
        else:
            self.temp_cache -= 1

        self.cur_pointer += 1
        return _next

    def hasNext(self):
        """
        :rtype: bool
        """
        has_next: bool = self.iterator.hasNext()

        if not has_next and self.temp_cache <= 0:
            return False

        return True


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end

if __name__ == "__main__":
    nums = [1, 2, 3]

    iter = PeekingIterator(Iterator(nums))
    while iter.hasNext():
        val = iter.peek()  # Get the next element but not advance the iterator.
        print(val)
        iter.next()  # Should return the same value as [val].

    iter = PeekingIterator(Iterator(nums))
    print(iter.next())
    print(iter.peek())
    print(iter.next())
    print(iter.next())
    print(iter.hasNext())

#
# @lc app=leetcode id=1497 lang=python3
#
# [1497] Check If Array Pairs Are Divisible by k
#


# @lc code=start
from typing import List


class Solution:
    def canArrange(self, arr, k):
        remainder_count: List[int] = [0] * k

        # Store the count of remainders in a map.
        for i in arr:
            remainder_count[(i % k + k) % k] += 1

        for i in arr:
            rem = (i % k + k) % k

            # If the remainder for an element is 0, then the count of numbers that give this remainder must be even.
            if rem == 0:
                if remainder_count[rem] % 2 == 1:
                    return False

            # If the remainder rem and k-rem do not have the same count then pairs can not be made.
            elif remainder_count[rem] != remainder_count[k - rem]:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.canArrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
    print(s.canArrange(arr=[1, 2, 3, 4, 5, 6], k=7))
    print(s.canArrange(arr=[1, 2, 3, 4, 5, 6], k=10))

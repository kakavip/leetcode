#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#

# @lc code=start
from collections.abc import Set
from typing import Dict, List


class Solution:
    prefix_cache: Dict[str, int] = {}
    prefix_list: Set[int] = set()

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        self.prefix_cache.clear()
        self.prefix_list = set()

        for v in list(set(arr1)):
            self._update_prefix(v)

        for v in list(set(arr2)):
            self._update_prefix(v, update=True)

        # print(self.prefix_cache)

        _max: int = 0
        for k in self.prefix_list:
            _max = max(_max, len(str(k)))

        return _max

    def _update_prefix(self, value: int, update: bool = False):
        n = len(str(value)) - 1
        while n >= 0:
            div: int = value // 10**n
            if div not in self.prefix_cache:
                self.prefix_cache[div] = 0
            if not update:
                self.prefix_cache[div] = 1
            else:
                if self.prefix_cache[div]:
                    self.prefix_list.add(div)

            n -= 1
        return


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix([1, 10, 100], [1000]) == 3)
    print(s.longestCommonPrefix(arr1=[1, 2, 3], arr2=[4, 4, 4]) == 0)
    print(s.longestCommonPrefix(arr1=[3, 34], arr2=[1, 6]) == 0)
    print(s.longestCommonPrefix(arr1=[13, 28], arr2=[33, 3]) == 0)

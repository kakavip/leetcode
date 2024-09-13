#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    # _cache: Dict[Tuple[int, int], int] = {}

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # self._cache.clear()
        n = len(arr)

        pre_xor: List[int] = [0] * n
        pre_xor[0] = arr[0]
        for i in range(1, n):
            pre_xor[i] = pre_xor[i - 1] ^ arr[i]

        result: List[int] = []
        for q in queries:
            if q[0] == 0:
                result.append(pre_xor[q[1]])
            else:
                result.append(pre_xor[q[1]] ^ pre_xor[q[0] - 1])

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]))

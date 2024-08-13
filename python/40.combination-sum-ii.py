#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start

from typing import Any, Dict, List, Tuple


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)

        result: List[List[int]] = []
        ds: List[int] = []

        def find_a_n(idx: int, target: int):
            if target == 0:
                result.append(ds[:])

            for i in range(idx, n):
                if candidates[i] > target:
                    break

                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                ds.append(candidates[i])
                find_a_n(i + 1, target - candidates[i])
                ds.pop()

        find_a_n(0, target)

        return result


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))
    print(s.combinationSum2([1, 1], 1))
    print(
        s.combinationSum2(
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            30,
        )
    )

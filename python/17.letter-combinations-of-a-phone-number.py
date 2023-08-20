#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

from typing import List


# @lc code=start
debug = False


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map: List[int, List[str]] = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        if not digits:
            return []

        # r: List[str] = []
        nums: List[int] = list(map(int, list(digits)))

        old: List[str] = letter_map[nums[0]].copy()

        for num in nums[1:]:
            _n_old: List[str] = []

            for _n in old:
                debug and print(letter_map)
                for l in letter_map[num]:
                    debug and print(f"_N: {_n}, L: {l}")
                    _n_old.append(_n + l)

            debug and print(f"OLD NUMS: {old}")
            debug and print(f"N_OLD NUMS: {_n_old}")
            old.clear()
            old.extend(_n_old)

        debug and print(f"RESULT: {old}")
        return old


# @lc code=end

debug = True
if __name__ == "__main__":
    s = Solution()
    s.letterCombinations("999")

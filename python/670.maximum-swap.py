#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_s: str = str(num)

        n: int = len(num_s)
        if n == 1:
            return num

        _max_values: List[int] = [0] * n
        _max_idxs: List[int] = [0] * n

        _max_idxs[-1] = n - 1
        _max_values[-1] = int(num_s[-1])

        for i in range(n - 2, -1, -1):
            if int(num_s[i]) > _max_values[i + 1]:
                _max_values[i] = int(num_s[i])
                _max_idxs[i] = i
            else:
                _max_values[i] = _max_values[i + 1]
                _max_idxs[i] = _max_idxs[i + 1]

        new_num_s: str = ""
        for i in range(n):
            if int(num_s[i]) < _max_values[i]:
                new_num_s += num_s[:i]
                new_num_s += str(_max_values[i])
                new_num_s += num_s[i + 1 : _max_idxs[i]]
                new_num_s += num_s[i]
                new_num_s += num_s[_max_idxs[i] + 1 :]
                break

        return int(new_num_s or num_s)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maximumSwap(2736) == 7236)
    print(s.maximumSwap(9973) == 9973)

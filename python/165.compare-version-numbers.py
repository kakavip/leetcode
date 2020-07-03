#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num_list_1: List[int] = version1.split(".")
        num_list_2: List[int] = version2.split(".")

        while len(num_list_1) > 0 and len(num_list_2) > 0:
            val_parse_1: int = int(num_list_1[0])
            val_parse_2: int = int(num_list_2[0])

            if val_parse_1 > val_parse_2:
                return 1
            if val_parse_2 > val_parse_1:
                return -1

            num_list_1 = num_list_1[1:]
            num_list_2 = num_list_2[1:]

        if sum(map(lambda x: int(x), num_list_1)) == sum(
            map(lambda x: int(x), num_list_2)
        ):

            return 0

        return 1 if len(num_list_1) > 0 else -1


# @lc code=end

if __name__ == "__main__":
    pass


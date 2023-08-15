#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
from typing import List


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        counter: int = 0
        chars_clone: List[str] = chars.copy() + ["aa"]

        if len(chars) == 1:
            return 1

        desc_len = 0
        _len = len(chars)
        sidx, eidx = -1, -1
        for idx, _ in enumerate(chars_clone):
            if sidx < 0:
                sidx = idx
                continue

            # print(f"ONE: {idx}")

            if chars_clone[idx] != chars_clone[idx - 1]:
                # or (
                #     idx == (_len - 1) and chars_clone[idx] == chars_clone[idx - 1]
                # ):
                eidx = idx - 1
                # if idx == _len - 1:
                #     eidx = idx

                num_dupl: int = eidx - sidx + 1
                # print(f"NUMBER OF DUPLICATION: {chars_clone[eidx]} {num_dupl}")
                if num_dupl > 1:
                    _len_dup: int = len(str(num_dupl))
                    counter += 1 + _len_dup

                    for i in range(_len_dup):
                        # print(f"CHARS {chars} ZERO: {sidx - desc_len + 1 + i}")
                        chars[sidx - desc_len + 1 + i] = str(num_dupl)[i]
                    sidx_del: int = sidx - desc_len + 1 + _len_dup
                    # print(f"DESC LENGTH: {desc_len} - {chars}")

                    len_lost: int = 0
                    for i in range(sidx_del, eidx + 1 - desc_len):
                        del chars[sidx_del]
                        len_lost += 1

                    desc_len += len_lost
                else:
                    counter += 1
                sidx = eidx + 1
        return len(chars)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    # chars = ["a", "a", "a", "b", "b", "a", "a"]
    # chars = ["a", "a"]
    # chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    # chars = ["a", "b", "c"]
    new_len = s.compress(chars)
    print(f"NEW CHARS: {chars} with length {new_len}.")

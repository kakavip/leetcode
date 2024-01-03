#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start

from typing import Dict, List, Optional


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        _data: Dict[str, List[str]] = {}
        for w in wordDict:
            if w in s:
                if w[0] not in _data:
                    _data[w[0]] = []

                _data[w[0]].append(w)

        arr: List[Optional[bool]] = [None] * len(s)
        n: int = len(s)

        def check_data(s_idx: int) -> bool:
            if s[s_idx] not in _data:
                arr[s_idx] = False
                return False

            if arr[s_idx] is False:
                return False

            for w in _data[s[s_idx]]:
                n_w = len(w)
                if n_w + s_idx > n:
                    continue

                if s[s_idx : n_w + s_idx] == w:
                    if s_idx + n_w == n:
                        arr[s_idx] = True
                        return True

                    if check_data(s_idx + n_w):
                        arr[s_idx] = True
                        return True
                    else:
                        arr[s_idx] = False
                        continue

            arr[s_idx] = False
            return False

        return check_data(0)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))
    print(s.wordBreak("applepenapple", ["apple", "pen"]))
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
from typing import List


class Solution:
    def is_sub_folder(self, a: str, b: str):
        return a.startswith(b + "/")

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result: List[str] = []
        folder.sort()

        for f in folder:
            if result and self.is_sub_folder(f, result[-1]):
                continue

            result.append(f)

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(
        s.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
        == ["/a", "/c/d", "/c/f"]
    )
    print(s.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]) == ["/a"])
    print(
        s.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"])
        == ["/a/b/c", "/a/b/ca", "/a/b/d"]
    )
    print(
        s.removeSubfolders(
            [
                "/aa/ab/ac/ae",
                "/aa/ab/af/ag",
                "/ap/aq/ar/as",
                "/ap/aq/ar",
                "/ap/ax/ay/az",
                "/ap",
                "/ap/aq/ar/at",
                "/aa/ab/af/ah",
                "/aa/ai/aj/ak",
                "/aa/ai/am/ao",
            ]
        )
        == [
            "/aa/ab/ac/ae",
            "/aa/ab/af/ag",
            "/aa/ab/af/ah",
            "/aa/ai/aj/ak",
            "/aa/ai/am/ao",
            "/ap",
        ]
    )

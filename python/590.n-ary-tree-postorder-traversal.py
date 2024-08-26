#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result: List[int] = []
        if not root:
            return result

        if root.children:
            for child in root.children:
                result.extend(self.postorder(child))

        result.append(root.val)

        return result


# @lc code=end

if __name__ == "__main__":
    # s = Solution()
    # s.postorder()
    pass

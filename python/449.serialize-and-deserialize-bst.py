#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

import json
from typing import List, Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        data: List[Optional[int]] = []

        nodes: List[TreeNode] = [root]
        while nodes != [None] * len(nodes):
            n_nodes: List[TreeNode] = []

            for node in nodes:
                if node is not None:
                    n_nodes.extend([node.left, node.right])

                    data.append(node.val)
                else:
                    data.append(None)

            nodes = n_nodes

        return json.dumps(data)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        d: List[Optional[int]] = json.loads(data)
        if not d:
            return None

        d.reverse()
        root = TreeNode(d.pop())
        nodes: List[TreeNode] = [root]

        while d:
            n_nodes: List[TreeNode] = []
            for node in nodes:
                if node is None:
                    continue

                if not d:
                    break
                val = d.pop()
                if val is not None:
                    node.left = TreeNode(val)
                    n_nodes.append(node.left)
                else:
                    node.left = None

                if not d:
                    break

                val = d.pop()
                if val is not None:
                    node.right = TreeNode(val)
                    n_nodes.append(node.right)
                else:
                    node.right = None

            nodes = n_nodes

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

if __name__ == "__main__":
    # s = Codec()
    # s.serialize(TreeNode(2, TreeNode(1), TreeNode(3)))
    # print(s.serialize(TreeNode(2, TreeNode(1), TreeNode(3))))
    # print(s.deserialize("[2, 1, 3]"))

    ser = Codec()
    deser = Codec()
    root = TreeNode(1, None, TreeNode(2))

    tree = ser.serialize(root)
    ans = deser.deserialize(tree)

    print(ser.serialize(ans))

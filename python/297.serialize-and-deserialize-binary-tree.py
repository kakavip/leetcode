#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TreeNode(object):
    val: int
    left: Optional[Any] = None
    right: Optional[Any] = None

    def __str__(self) -> str:
        return str(self.val)


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import json

debug = False


class Codec:
    def _serialize(
        self,
        root: TreeNode,
        layer: int = 0,
        cached_data: Dict[int, List[Optional[int]]] = {},
    ):
        if layer not in cached_data:
            cached_data.update({layer: []})

        if not root:
            cached_data[layer].append(None)
            return

        # result: List[Optional[int]] = []
        # result.append(root.val)
        cached_data[layer].append(root.val)

        self._serialize(root.left, layer + 1, cached_data)
        self._serialize(root.right, layer + 1, cached_data)

        # result.extend(self._serialize(root.left))
        # result.extend(self._serialize(root.right))

        # return result
        return

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # print("RUN SERIALIZE")

        cached_data: Dict[int, List[Optional[int]]] = {}
        self._serialize(root, layer=0, cached_data=cached_data)

        data: List[Optional[int]] = []
        layers: List[int] = sorted(cached_data.keys())
        for layer in layers:
            if set(cached_data[layer]) == {None}:
                break

            data.extend(cached_data[layer])

        # data: List[Optional[int]] = self._serialize(root)
        if len(data) > 0:
            while data[-1] is None:
                data.pop()

        result: str = json.dumps(data).replace(" ", "")
        return result

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # print("RUN DESERIALIZE")
        data = json.loads(data)
        # print(f"DATA: {data}")
        if not data:
            return None

        root: Optional[TreeNode] = None

        layer, idx = 0, 0
        next_idx: int = 2**layer
        old_nodes: List[TreeNode] = []
        while data[idx:next_idx]:
            layer_nodes: List[Optional[int]] = data[idx:next_idx]
            debug and print(
                f"IDX {idx} COUNTER {next_idx} Layer {layer}: {layer_nodes}"
            )
            if root is None:
                root = TreeNode(layer_nodes[0])
                old_nodes = [root]
            else:
                new_nodes: List[TreeNode] = []
                for layer_node in layer_nodes:
                    new_nodes.append(
                        layer_node is not None and TreeNode(layer_node) or None
                    )

                debug and print(f"NEW NODES: {', '.join(map(str,new_nodes))}")

                new_idx: int = 0
                for idx, old_node in enumerate(old_nodes):
                    if old_node is None:
                        continue
                    # debug and print(f"NEW IDX: {new_idx} - {len(new_nodes)}")
                    if not new_nodes[2 * new_idx :]:
                        break

                    if len(new_nodes) > 2 * new_idx:
                        old_node.left = new_nodes[2 * new_idx]
                    if len(new_nodes) > 2 * new_idx + 1:
                        old_node.right = new_nodes[2 * new_idx + 1]
                    new_idx += 1

                old_nodes = new_nodes

            idx = next_idx
            layer += 1
            # next_idx += 2**layer
            next_idx += 2 * len(list(filter(lambda x: x is not None, old_nodes)))

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end


if __name__ == "__main__":
    debug = True
    node = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

    c = Codec()
    # print(c.serialize(node))
    # print(c.deserialize(c.serialize(node)))
    # print(c.serialize(c.deserialize("[1,2,3,null,null,4,5,6,7]")))
    # print(c.serialize(c.deserialize("[]")))
    # print(c.serialize(c.deserialize("[1,2]")))
    print(
        c.serialize(
            c.deserialize(
                "[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]"
            )
        )
    )
    # print(c.deserialize("[1,2,3,null,null,4,5,6,7]"))

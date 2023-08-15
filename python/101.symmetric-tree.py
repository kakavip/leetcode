#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#


from typing import Any, List, Optional


class TreeNode:
    def __init__(self, x: int, left: Optional[Any] = None, right: Optional[Any] = None):
        self.val: int = x
        self.left: TreeNode = left
        self.right: TreeNode = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True

        v_s1, v_s2 = [root.left and root.left.val], [root.right and root.right.val]
        stack_1, stack_2 = [root.left], [root.right]
        while True:
            # print(f"s1: {v_s1} - s2: {v_s2}")
            if v_s1 != v_s2:
                return False

            if set(v_s1) == {None} and set(v_s2) == {None}:
                break

            n_s1, n_s2 = [], []
            v_n_s1, v_n_s2 = [], []
            for idx in range(len(stack_1)):
                if stack_1[idx]:
                    l1, r1 = stack_1[idx].left, stack_1[idx].right
                    n_s1.extend([l1, r1])
                    v_n_s1.append(None if l1 is None else l1.val)
                    v_n_s1.append(None if r1 is None else r1.val)

                if stack_2[idx]:
                    l2, r2 = stack_2[idx].left, stack_2[idx].right
                    n_s2.extend([l2, r2])
                    v_n_s2.append(None if l2 is None else l2.val)
                    v_n_s2.append(None if r2 is None else r2.val)

            # print(f"s1: {v_s1} - s2: {v_s2}")
            v_s1, v_s2 = v_n_s1, v_n_s2
            v_s2.reverse()
            stack_1, stack_2 = n_s1, n_s2
            # stack_2.reverse()

        return True


# @lc code=end

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)

    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)

    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)

    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(7)

    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(9)

    # root = TreeNode(1, TreeNode(0))

    sl = Solution()
    print("result: {}".format(sl.isSymmetric(root)))
    # sub, _ = subtract_tree(root)
    # print("result: {}".format(sub))


#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # print("root val: {}, sum: {}".format(None if root is None else root.val, sum))
        if root == None:
                return False
        if sum - root.val == 0 and root.left == None and root.right==None:
            return True
        return (root.left is not None and self.hasPathSum(root.left, sum - root.val)) or (root.right is not None and self.hasPathSum(root.right, sum - root.val))
# @lc code=end

if __name__ == "__main__":
    root = TreeNode(5)

    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    root.left.left.left=TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    s = Solution()
    result = s.hasPathSum(root, 22)
    print("Result: {}".format(result))
    pass
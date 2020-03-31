from typing import List

#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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

def connectNode(root: TreeNode, inorder: List[int], postorder: List[int]) -> TreeNode:
    if len(postorder) == 0 or len(inorder) == 0:
        return None
    # print("Inorder: {}, Postorder: {}".format(inorder, postorder))
    root_val = postorder[len(postorder)-1]
    root = TreeNode(root_val)
    
    pos_val = inorder.index(root_val)
    if pos_val == len(inorder)-1:
        root.left = connectNode( root.left, inorder[:pos_val], postorder[:pos_val])
        pass
    else:
        inorder_left = inorder[:pos_val]
        if len(inorder_left) > 0:
            postorder_left = [val for val in postorder if val in inorder_left]
            root.left = connectNode(root.left, inorder_left, postorder_left)
        
        inorder_right = inorder[pos_val+1:]
        if len(inorder_right) > 0:
            postorder_right = [val for val in postorder if val in inorder_right]
            root.right = connectNode(root.right, inorder_right, postorder_right)
    return root

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root: TreeNode = None
        return connectNode(root, inorder, postorder)

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.buildTree([9,3,15,20,7],[9,15,7,20,3])
    pass

#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def restructure_tree_node(root: TreeNode) -> TreeNode:
            if root == None:
                return None
            node_left = None
            node_right = None

            if root.left:
                node_left = restructure_tree_node(root.left)
            
            iter_left = node_left
            if iter_left != None:
                while iter_left.right is not None:
                    iter_left = iter_left.right
                    pass
                
            if root.right:
                node_right = restructure_tree_node(root.right)
            
            if node_left is not None:
                root.right = node_left
                iter_left.right = node_right
            else:
                root.right = node_right
            root.left = None
            return root
            
        
        root = restructure_tree_node(root)
        pass
        
# @lc code=end
if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(5)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    s = Solution()
    s.flatten(root)

    while root != None:
        print(root.val)
        root = root.right
    pass

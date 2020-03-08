package main

/*
 * @lc app=leetcode id=94 lang=golang
 *
 * [94] Binary Tree Inorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func inorderTraversal(root *TreeNode) []int {
	result := []int{}
	left := []int{}
	right := []int{}

	if root == nil {
		return []int{}
	}

	if root.Left != nil {
		left = inorderTraversal(root.Left)
	}
	if root.Right != nil {
		right = inorderTraversal(root.Right)
	}
	result = append(left, root.Val)
	result = append(result, right...)
	return result
}

// @lc code=end

func main() {

}

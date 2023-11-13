/*
 * @lc app=leetcode id=199 lang=golang
 *
 * [199] Binary Tree Right Side View
 */

package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
	result := []int{}

	if root == nil {
		return result
	}

	nodes := []*TreeNode{root}
	for {
		result = append(result, nodes[len(nodes)-1].Val)

		nNodes := []*TreeNode{}
		for _, v := range nodes {
			if v.Left != nil {
				nNodes = append(nNodes, v.Left)
			}
			if v.Right != nil {
				nNodes = append(nNodes, v.Right)
			}
		}

		if len(nNodes) == 0 {
			break
		}

		nodes = nNodes
	}

	return result
}

// @lc code=end

func main() {

}

package main

import (
	"fmt"
)

/*
 * @lc app=leetcode id=103 lang=golang
 *
 * [103] Binary Tree Zigzag Level Order Traversal
 */
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

type Node struct {
	Val   int
	Layer int
}

func getAllOfValuesInRLR(root *TreeNode, layer int) []Node {
	if root == nil {
		return []Node{}
	}
	result := []Node{Node{Val: root.Val, Layer: layer}}
	if root.Left != nil {
		result = append(result, getAllOfValuesInRLR(root.Left, layer+1)...)
	}
	if root.Right != nil {
		result = append(result, getAllOfValuesInRLR(root.Right, layer+1)...)
	}
	return result
}
func zigzagLevelOrder(root *TreeNode) [][]int {
	result := [][]int{}
	nodeList := getAllOfValuesInRLR(root, 0)
	for i := 0; i < len(nodeList); i++ {
		node := nodeList[i]
		if node.Layer+1 > len(result) {
			result = makeMemForList(result, node.Layer+1-len(result))
		}
		if node.Layer%2 == 0 {
			result[node.Layer] = append(result[node.Layer], node.Val)
		} else {
			result[node.Layer] = append([]int{node.Val}, result[node.Layer]...)
		}
	}
	return result
}

func makeMemForList(matrix [][]int, num int) [][]int {
	for i := 0; i < num; i++ {
		matrix = append(matrix, []int{})
	}
	return matrix
}

// @lc code=end

func main() {
	var root *TreeNode
	root = &TreeNode{
		Val: 3,
		Left: &TreeNode{
			Val: 9,
		},
		Right: &TreeNode{
			Val: 20,
			Left: &TreeNode{
				Val: 15,
			},
			Right: &TreeNode{
				Val: 7,
			},
		},
	}
	result := zigzagLevelOrder(root)
	fmt.Println("Zigzag matrix: ", result)
}

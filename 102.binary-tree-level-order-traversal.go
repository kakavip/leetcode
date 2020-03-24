package main

import (
	"fmt"
)

/*
 * @lc app=leetcode id=102 lang=golang
 *
 * [102] Binary Tree Level Order Traversal
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

func getAllOfValues(root *TreeNode, layer int) []Node {
	if root == nil {
		return []Node{}
	}
	result := []Node{}
	leftNodeList, rightNodeList := []Node{}, []Node{}
	if root.Left != nil {
		leftNodeList = getAllOfValues(root.Left, layer+1)
	}
	if root.Right != nil {
		rightNodeList = getAllOfValues(root.Right, layer+1)
	}

	result = append(result, leftNodeList...)

	curNode := Node{Val: root.Val, Layer: layer}
	result = append(result, curNode)
	result = append(result, rightNodeList...)
	return result
}

func levelOrder(root *TreeNode) [][]int {
	result := [][]int{}
	nodeList := getAllOfValues(root, 0)
	// fmt.Println("NodeList: ", nodeList)
	for i := 0; i < len(nodeList); i++ {
		node := nodeList[i]
		if node.Layer+1 > len(result) {
			result = makeMemForMatrix(result, node.Layer+1-len(result))
		}
		result[node.Layer] = append(result[node.Layer], node.Val)
	}
	return result
}

func makeMemForMatrix(matrix [][]int, num int) [][]int {
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
	result := levelOrder(root)
	fmt.Println("result: ", result)
}

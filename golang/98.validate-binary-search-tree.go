package main

import "fmt"

/*
 * @lc app=leetcode id=98 lang=golang
 *
 * [98] Validate Binary Search Tree
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
func isValidBST(root *TreeNode) bool {
	if root == nil {
		return true
	}
	isBST, _ := checkBST(root)
	// return isBST
	return isBST
}

func checkBST(root *TreeNode) (bool, []int) {
	if root == nil {
		return true, []int{}
	}
	// fmt.Println("Root val: ", root.Val)
	hasLeft, hasRight := root.Left != nil, root.Right != nil
	if !hasLeft && !hasRight {
		return true, []int{root.Val}
	}
	isValidLeft, isValidRight, valLeftList, valRightList := true, true, []int{}, []int{}

	_min, _max := -1000000, -1000000
	if hasLeft {
		isValidLeft, valLeftList = checkBST(root.Left)
		// fmt.Println("Is valid left: ", isValidLeft)
		_max = max(valLeftList)
	}
	if hasRight {
		isValidRight, valRightList = checkBST(root.Right)
		// fmt.Println("Is valid Right: ", isValidRight)
		_min = min(valRightList)
	}

	if !isValidLeft || !isValidRight {
		return false, []int{}
	}

	isValid := true
	if _max != -1000000 {
		if root.Val <= _max {
			isValid = false
		}
	}
	if _min != -1000000 {
		if root.Val >= _min {
			isValid = false
		}
	}
	// fmt.Println("root Val: ", root.Val, "right list: ", valRightList, " left list: ", valLeftList, " is valid: ", isValid, "min: ", _min, "max: ", _max)
	return isValid, append(append(valLeftList, valRightList...), root.Val)
}

func min(arr []int) int {
	if len(arr) == 0 {
		return -1000000
	}
	_min := arr[0]
	for i := 1; i < len(arr); i++ {
		if _min > arr[i] {
			_min = arr[i]
		}
	}
	return _min
}
func max(arr []int) int {
	if len(arr) == 0 {
		return -1000000
	}
	_max := arr[0]
	for i := 1; i < len(arr); i++ {
		if _max < arr[i] {
			_max = arr[i]
		}
	}
	return _max
}

// @lc code=end

func main() {
	// var root *TreeNode = &TreeNode{Val: 5, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 4, Left: &TreeNode{Val: 3}, Right: &TreeNode{Val: 6}}}
	var root *TreeNode = &TreeNode{
		Val: 0,
		Left: &TreeNode{
			Val: -1,
			// Left: &TreeNode{
			// 	Val: 0,
			// },
			// Right: &TreeNode{
			// 	Val: 2,
			// },
		},
		// Right: &TreeNode{
		// 	Val: 3,
		// 	// Left: &TreeNode{
		// 	// 	Val: 3,
		// 	// },
		// 	// Right: &TreeNode{
		// 	// 	Val: 6,
		// 	// },
		// },
	}
	fmt.Println("Result: ", isValidBST(root))
}

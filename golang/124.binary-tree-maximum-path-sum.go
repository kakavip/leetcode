package main

import "fmt"

/*
 * @lc app=leetcode id=124 lang=golang
 *
 * [124] Binary Tree Maximum Path Sum
 */

// TreeNode test
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

func findMaxPathSum(root *TreeNode, parent *TreeNode, max *int) (int, bool) {
	if root == nil {
		return 0, false
	}

	canAdd := false
	total := 0
	canLeftAdd, canRightAdd := true, true
	maxLeft, maxRight := 0, 0
	hasLeft, hasRight := false, false

	if root.Left != nil {
		hasLeft = true
		maxLeft, canLeftAdd = findMaxPathSum(root.Left, root, max)
	}
	if root.Right != nil {
		hasRight = true
		maxRight, canRightAdd = findMaxPathSum(root.Right, root, max)
	}

	// fmt.Println("Root val: ", root.Val, "has left: ", hasLeft, " has right: ", hasRight, " maxLeft: ", maxLeft, "maxRight: ", maxRight)
	// fmt.Println("--> Can add left: ", canLeftAdd, " Can add right: ", canRightAdd)

	if canLeftAdd || canRightAdd {
		if maxLeft > *max && hasLeft {
			*max = maxLeft
		}
		if maxRight > *max && hasRight {
			*max = maxRight
		}

		total = root.Val

		if maxLeft > 0 && maxRight > 0 {
			if maxLeft+maxRight+root.Val > *max {
				*max = maxLeft + maxRight + root.Val
			}
		}

		if parent == nil {
			if maxLeft > 0 {
				// debug(maxLeft, true)
				total += maxLeft
			}
			if maxRight > 0 {
				// debug(maxRight, true)
				total += maxRight
			}

			if total > maxLeft && total > maxRight || !hasLeft && !hasRight {
				canAdd = true
				if total > *max {
					*max = total
				}
			}
		} else {
			canAdd = true

			if maxLeft >= maxRight && maxLeft >= 0 {
				total += maxLeft

				// debug(maxLeft, false)
			}

			if maxRight > maxLeft && maxRight >= 0 {
				total += maxRight

				// debug(maxRight, false)
			}

			if total > *max {
				*max = total
			}
		}
	}
	return total, canAdd
}

func maxPathSum(root *TreeNode) int {
	if root == nil {
		return 0
	}

	var _max int = root.Val
	_, _ = findMaxPathSum(root, nil, &_max)

	return _max
}

func debug(value int, isRoot bool) {
	if isRoot {
		fmt.Println("Value is added root: ", value)
	} else {
		fmt.Println("Value is added normal: ", value)
	}
}

// @lc code=end

func main() {
	var root *TreeNode
	root = &TreeNode{
		Val: -10,
		Left: &TreeNode{
			Val: 9,
		},
		Right: &TreeNode{
			Val: 20,
			Right: &TreeNode{
				Val: 7,
			},
			Left: &TreeNode{
				Val: 15,
			},
		},
	}
	_max := maxPathSum(root)
	fmt.Println("Result: ", _max)
}

/**
[5,4,8,11,null,13,4,7,2,null,null, null, 1]
			5
		4		8
	11	null 13		4
7	2					1

[1,0,1,1,2,0,-1,0,1,-1,0,-1,0,1,0]
			1
		0			1
	1	  2	  	  0	 	-1
0 	  1 -1	0  -1  0  1   0

[5,-5,-9,6,3,2,null,null,5,4,null,null,null,null,null,null,1]
		              5
	     -5  		       -9
   6           3         2   null
null   5        4   null null null
   null null null 1
	-10
9        20
	  15     7

*/

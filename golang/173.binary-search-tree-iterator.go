package main

import "fmt"

/*
 * @lc app=leetcode id=173 lang=golang
 *
 * [173] Binary Search Tree Iterator
 */

// TreeNode ...
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

// Node ...
type Node struct {
	Val  int
	Next *Node
}

// BSTIterator ...
type BSTIterator struct {
	node *Node
}

func parseTreeNodeToNode(root *TreeNode) *Node {
	if root == nil {
		return nil
	}
	var leftNode, rightNode *Node = nil, nil
	var middleNode *Node = &Node{Val: root.Val}

	if root.Left != nil {
		leftNode = parseTreeNodeToNode(root.Left)
	}

	if root.Right != nil {
		rightNode = parseTreeNodeToNode(root.Right)
	}

	middleNode.Next = rightNode

	var tempNode *Node = leftNode
	if tempNode != nil {
		for tempNode.Next != nil {
			tempNode = tempNode.Next
		}

		tempNode.Next = middleNode
		return leftNode
	}

	return middleNode
}

// Constructor ..
func Constructor(root *TreeNode) BSTIterator {
	return BSTIterator{
		node: parseTreeNodeToNode(root),
	}
}

/** @return the next smallest number */

//Next ...
func (bst *BSTIterator) Next() int {
	val := bst.node.Val
	bst.node = bst.node.Next

	return val
}

/** @return whether we have a next smallest number */

// HasNext ...
func (bst *BSTIterator) HasNext() bool {
	return bst.node != nil
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
// @lc code=end

func main() {
	var root *TreeNode = &TreeNode{
		Val: 7,
		Left: &TreeNode{
			Val: 3,
		},
		Right: &TreeNode{
			Val: 15,
			Right: &TreeNode{
				Val: 20,
			},
			Left: &TreeNode{
				Val: 9,
			},
		},
	}

	bst := Constructor(root)
	fmt.Println(bst.Next(), bst.Next(), bst.HasNext(), bst.Next(), bst.HasNext(), bst.Next(), bst.HasNext(), bst.Next(), bst.HasNext())

}

package main

import "fmt"

/*
 * @lc app=leetcode id=116 lang=golang
 *
 * [116] Populating Next Right Pointers in Each Node
 */
type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

// NodeLayer test
type NodeLayer struct {
	Layer int
	node  *Node
}

func connectLayer(root *Node, curLayerList *[]NodeLayer, layer int) {
	if root == nil {
		return
	}
	// check existing
	isExisted := false
	for i := 0; i < len(*curLayerList); i++ {
		if (*curLayerList)[i].Layer == layer && (*curLayerList)[i].node != nil {
			isExisted = true
			(*curLayerList)[i].node.Next = root
			(*curLayerList)[i].node = root
			break
		}
	}
	if !isExisted {
		curLayerNode := NodeLayer{
			Layer: layer,
			node:  root,
		}
		*curLayerList = append(*curLayerList, curLayerNode)
	}
	if root.Left != nil {
		connectLayer(root.Left, curLayerList, layer+1)
	}
	if root.Right != nil {
		connectLayer(root.Right, curLayerList, layer+1)
	}
}

func connect(root *Node) *Node {
	connectLayer(root, &[]NodeLayer{}, 0)
	return root
}

// @lc code=end

func main() {
	var root *Node = &Node{
		Val: 1,
		Left: &Node{
			Val: 2,
			Left: &Node{
				Val: 4,
			},
			Right: &Node{
				Val: 5,
			},
		},
		Right: &Node{
			Val: 3,
			Left: &Node{
				Val: 6,
			},
			Right: &Node{
				Val: 7,
			},
		},
	}
	connect(root)
	fmt.Println(root.Left.Next.Val)
}

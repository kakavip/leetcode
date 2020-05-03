/*
 * @lc app=leetcode id=117 lang=golang
 *
 * [117] Populating Next Right Pointers in Each Node II
 */

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


package main

/*
 * @lc app=leetcode id=138 lang=golang
 *
 * [138] Copy List with Random Pointer
 */

// Node ...
type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

// HashNode ...
type HashNode struct {
	baseNode  *Node
	cloneNode *Node
}

var randomInCommingList = []HashNode{}
var historyNodeList = []HashNode{}

func copyRandomList(head *Node) *Node {

	sliceNode := head
	var headCopy *Node = nil

	for ; sliceNode != nil; sliceNode = sliceNode.Next {
		sliceCopy := &Node{
			Val:    sliceNode.Val,
			Next:   nil,
			Random: nil,
		}
		if headCopy == nil {
			headCopy = sliceCopy
		}
		// check current head
		if len(historyNodeList) > 0 {
			historyNodeList[len(historyNodeList)-1].cloneNode.Next = sliceCopy
		}

		for i := 0; i < len(randomInCommingList); i++ {
			if randomInCommingList[i].cloneNode.Random == nil && randomInCommingList[i].baseNode.Random == sliceNode {
				randomInCommingList[i].cloneNode.Random = sliceCopy
			}
		}

		if sliceNode.Random == sliceNode {
			sliceCopy.Random = sliceCopy
		} else if sliceNode.Random != nil {

			// Search in history
			var isExisted bool = false
			for i := 0; i < len(historyNodeList); i++ {
				if sliceNode.Random == historyNodeList[i].baseNode {
					sliceCopy.Random = historyNodeList[i].cloneNode
					isExisted = true

					break
				}
			}

			if isExisted == false {
				randomInCommingList = append(randomInCommingList, HashNode{baseNode: sliceNode, cloneNode: sliceCopy})
			}
		}

		// Save history
		historyNodeList = append(historyNodeList, HashNode{baseNode: sliceNode, cloneNode: sliceCopy})
	}

	return headCopy
}

// @lc code=end

func main() {

}

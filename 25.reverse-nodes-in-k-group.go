package main

/*
 * @lc app=leetcode id=25 lang=golang
 *
 * [25] Reverse Nodes in k-Group
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseKGroup(head *ListNode, k int) *ListNode {
	var resultNode *ListNode
	tempNode := head
	var endOfOld *ListNode

	for true {

		var isEnd bool = false
		node := tempNode
		for i := 0; i < k; i++ {
			if node == nil {
				isEnd = true
				break
			}
			node = node.Next
		}
		if isEnd == true {
			if resultNode == nil {
				resultNode = head
			}
			break
		}

		// A-> B-> C -> D -> E -> F -> G -> H
		// A <- B  C -> D -> E -> F -> G -> H
		// B -> A -> C -> D -> E -> F -> G -> H
		// B -> A D -> C  E -> F -> G -> H
		preRunNode := tempNode      //A
		curRunNode := tempNode.Next //B
		// var nextNode *ListNode
		for i := 1; i < k; i++ {
			nextNode := curRunNode.Next // C
			curRunNode.Next = preRunNode

			// fmt.Println("In Loop: ", curRunNode.Val, "->", preRunNode.Val)
			//
			preRunNode = curRunNode // B
			curRunNode = nextNode   // C
		}

		if endOfOld == nil {
			endOfOld = tempNode
		} else {
			endOfOld.Next = preRunNode
			endOfOld = tempNode
		}

		tempNode.Next = curRunNode
		// fmt.Println(tempNode.Val, "->", curRunNode.Val)

		if resultNode == nil {
			resultNode = preRunNode
		} else {

		}
		tempNode = curRunNode
		// // fmt.Println("TempNode: ", preRunNode.Val)
	}

	return resultNode
}

// @lc code=end

type ListNode struct {
	Val  int
	Next *ListNode
}

func makeListNode(valueList []int) *ListNode {

	var result *ListNode
	var head *ListNode
	for i := 0; i < len(valueList); i++ {
		if result == nil {
			result = new(ListNode)
			head = result
		}
		result.Val = valueList[i]
		if i < len(valueList)-1 {
			result.Next = new(ListNode)
			result = result.Next
		}
	}
	return head
}
func printListNode(front string, node *ListNode) {
	// fmt.Print(front)
	temp := node
	for ; temp != nil; temp = temp.Next {
		// fmt.Print(temp.Val)
		if temp.Next != nil {
			// fmt.Print("->")
		}
	}
	// fmt.Println()
}

func main() {
	var head *ListNode = makeListNode([]int{1})
	printListNode("Original ListNode: ", head)
	result := reverseKGroup(head, 2)
	printListNode("Reverse ListNode: ", result)
}

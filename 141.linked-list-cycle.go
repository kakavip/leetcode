package main

/*
 * @lc app=leetcode id=141 lang=golang
 *
 * [141] Linked List Cycle
 */

// ListNode ..
type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	var historyListNode []*ListNode = []*ListNode{}
	sliceNode := head

	for sliceNode != nil {

		for i := 0; i < len(historyListNode); i++ {
			if sliceNode == historyListNode[i] {
				return true
			}
		}

		historyListNode = append(historyListNode, sliceNode)

		sliceNode = sliceNode.Next
	}

	return false
}

// @lc code=end

func main() {

}

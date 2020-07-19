package main

import "fmt"

/*
 * @lc app=leetcode id=206 lang=golang
 *
 * [206] Reverse Linked List
 */

// ListNode ...
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

func reverseList(head *ListNode) *ListNode {
	sliceNode := head
	var previousNode *ListNode = nil
	var currentNode *ListNode = nil

	for sliceNode != nil {
		currentNode = sliceNode
		sliceNode = sliceNode.Next
		currentNode.Next = previousNode
		previousNode = currentNode
	}

	return currentNode
}

// @lc code=end

func main() {
	var head *ListNode = &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 3,
				Next: &ListNode{Val: 4, Next: &ListNode{
					Val: 5,
				}},
			},
		},
	}

	var newHead *ListNode = reverseList(head)

	for ; newHead != nil; newHead = newHead.Next {
		fmt.Println(newHead.Val)
	}

}

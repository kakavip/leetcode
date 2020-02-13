package main

import "fmt"

// import "fmt"

/*
 * @lc app=leetcode id=21 lang=golang
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	var resultNode *ListNode
	if l1 != nil || l2 != nil {
		resultNode = new(ListNode)
	}
	tempNode := resultNode
	for true {
		// fmt.Println("ListNode l1: ", l1 == nil)
		// fmt.Println("ListNode l2: ", l2 == nil)

		var value *int
		if l1 == nil && l2 == nil {
			break
		}

		if l1 == nil && l2 != nil {
			value = new(int)
			*value = l2.Val
			l2 = l2.Next
		}
		if l2 == nil && l1 != nil {
			value = new(int)
			*value = l1.Val
			l1 = l1.Next
		}

		if value == nil {
			value = new(int)
			if l1.Val > l2.Val {
				*value = l2.Val
				l2 = l2.Next
			} else {
				*value = l1.Val
				l1 = l1.Next
			}
		}

		tempNode.Val = *value
		if l2 != nil || l1 != nil {
			tempNode.Next = new(ListNode)
			tempNode = tempNode.Next
		}
	}
	return resultNode
}

// @lc code=end

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	l1 := new(ListNode)
	l1.Val = 1
	l1.Next = new(ListNode)
	l1.Next.Val = 2
	l1.Next.Next = new(ListNode)
	l1.Next.Next.Val = 4

	l2 := new(ListNode)
	l2.Val = 1
	l2.Next = new(ListNode)
	l2.Next.Val = 3
	l2.Next.Next = new(ListNode)
	l2.Next.Next.Val = 4

	fmt.Println(mergeTwoLists(l1, l2).Val)
}

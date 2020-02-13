package main

import "fmt"

/*
 * @lc app=leetcode id=24 lang=golang
 *
 * [24] Swap Nodes in Pairs
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
	temp := head
	preTemp := head
	var signal bool = true
	var result *ListNode
	for true {
		if temp == nil || temp.Next == nil {
			if result == nil {
				result = temp
			}
			break
		}

		if signal == false {
			nodeOne, nodeTwo := temp, temp.Next
			temp = temp.Next.Next
			// Swap
			preTemp.Next = nodeTwo
			nodeTwo.Next = nodeOne
			nodeOne.Next = temp
			preTemp = nodeOne

			if result == nil {
				result = nodeTwo
			}
		}

		signal = !signal
	}

	return result
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
	l1.Next.Next.Val = 3
	l1.Next.Next.Next = new(ListNode)
	l1.Next.Next.Next.Val = 4

	printListNode(swapPairs(l1))
}

func printListNode(node *ListNode) {
	temp := node
	for ; temp != nil; temp = temp.Next {
		fmt.Print(temp.Val)
		if temp.Next != nil {
			fmt.Print("->")
		}
	}
}

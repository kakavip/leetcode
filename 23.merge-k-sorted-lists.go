package main

import "fmt"

/*
 * @lc app=leetcode id=23 lang=golang
 *
 * [23] Merge k Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
	var resultNode, tempNode *ListNode
	for true {
		var min *int
		for i := 0; i < len(lists); i++ {
			if lists[i] != nil {
				if min == nil {
					min = new(int)
					*min = lists[i].Val
				} else {
					if *min > lists[i].Val {
						*min = lists[i].Val
					}
				}
			}
		}

		if min == nil {
			break
		}

		if resultNode == nil {
			resultNode = new(ListNode)
			tempNode = resultNode
		} else {
			tempNode.Next = new(ListNode)
			tempNode = tempNode.Next
		}

		for i := 0; i < len(lists); i++ {
			if lists[i] == nil {
				continue
			}

			if *min == lists[i].Val {
				lists[i] = lists[i].Next
				break
			}
		}

		tempNode.Val = *min
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

	fmt.Println(mergeKLists([]*ListNode{l1, l2}).Val)
}

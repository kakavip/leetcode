/*
 * @lc app=leetcode id=234 lang=golang
 *
 * [234] Palindrome Linked List
 */

package main

import "fmt"

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
func isPalindrome(head *ListNode) bool {
	if head == nil {
		return true
	}

	numMap := make(map[int]*[]int, 10)

	for i := 0; i < 10; i++ {
		numMap[i] = &[]int{}
	}

	index := 0
	var sNode *ListNode = head
	for ; sNode != nil; sNode = sNode.Next {
		idxs := numMap[sNode.Val]
		*idxs = append(*idxs, index)

		index += 1
	}

	if index == 1 {
		return true
	}

	oneCounter := 0
	counter := 0
	hasTwoPos := false
	index -= 1
	for i := 0; i < 10; i++ {
		if len(*numMap[i]) > 0 {
			if len(*numMap[i]) > 1 {
				hasTwoPos = true
			}

			if len(*numMap[i]) == 1 {
				oneCounter += 1
			}

			counter += 1
			if !checkPalindrome(*numMap[i], index, i) {
				return false
			}
		}
	}

	if counter > 1 && !hasTwoPos {
		return false
	}
	if oneCounter > 1 {
		return false
	}

	return true
}

func checkPalindrome(a []int, maxIdx int, value int) bool {
	// fmt.Println("MAX IDX: ", maxIdx, a, value)
	if len(a) == 1 {
		return true
	}

	if len(a)%2 != 0 {
		if (maxIdx+1)%2 == 0 {
			return false
		} else {
			if a[(len(a)+1)/2-1] != maxIdx/2 {
				return false
			}
		}

	}

	for i := 0; i <= len(a)/2; i++ {
		if a[i] != maxIdx-a[len(a)-1-i] {
			return false
		}
	}

	return true
}

// @lc code=end

func main() {
	// head := &ListNode{
	// 	Val: 1,
	// 	Next: &ListNode{
	// 		Val: 0,
	// 		Next: &ListNode{
	// 			Val: 1,
	// 			Next: &ListNode{
	// 				Val: 1,
	// 			},
	// 		},
	// 	},
	// }
	// head := &ListNode{
	// 	Val: 1,
	// 	Next: &ListNode{
	// 		Val: 0,
	// 		Next: &ListNode{
	// 			Val: 1,
	// 		},
	// 	},
	// }

	fmt.Println(checkPalindrome([]int{1, 15, 30, 56, 71, 85}, 86, 0))

}

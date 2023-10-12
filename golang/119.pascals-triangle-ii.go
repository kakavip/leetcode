/*
 * @lc app=leetcode id=119 lang=golang
 *
 * [119] Pascal's Triangle II
 */
package main

import "fmt"

// @lc code=start
func getRow(rowIndex int) []int {
	if rowIndex == 0 {
		return []int{1}
	} else if rowIndex == 1 {
		return []int{1, 1}
	} else if rowIndex == 2 {
		return []int{1, 2, 1}
	}

	baseR := []int{1, 2}
	for i := 3; i <= rowIndex; i++ {
		tempR := []int{}
		for idx, v := range baseR {
			if idx == 0 {
				tempR = append(tempR, baseR[idx])
			} else {
				tempR = append(tempR, baseR[idx-1]+v)
			}
		}

		if i%2 == 0 {
			tempR = append(tempR, baseR[len(baseR)-1]*2)
		}

		baseR = tempR
	}

	if rowIndex%2 == 0 {
		return append(baseR, reverseArr(baseR[:len(baseR)-1])...)
	} else {
		return append(baseR, reverseArr(baseR)...)
	}
}

func reverseArr(s []int) []int {
	var n_s []int = append([]int{}, s...)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		n_s[i], n_s[j] = n_s[j], n_s[i]
	}

	return n_s
}

// @lc code=end

func main() {
	fmt.Println(getRow(5))
}

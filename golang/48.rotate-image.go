package main

import "fmt"

/*
 * @lc app=leetcode id=48 lang=golang
 *
 * [48] Rotate Image
 */

// @lc code=start
func rotate(matrix [][]int) {
	var offset int = 0
	var max int = len(matrix)
	for offset < max-offset-1 {
		left, right := offset, max-offset-1

		// fmt.Println("Circle: ", offset+1, " left: ", left, " right: ", right)
		// fmt.Println("Offset: ", offset, " left: ", left, " right: ", right)
		for i := 0; i < right-left; i++ {
			l, t, r, b := matrix[right-i][left], matrix[left][i+left], matrix[left+i][right], matrix[right][right-i]
			// fmt.Println("left: ", l, " top: ", t, " right: ", r, " bottom: ", b)
			matrix[left][i+left], matrix[left+i][right], matrix[right][right-i], matrix[right-i][left] = l, t, r, b
		}
		offset++
	}

	// fmt.Println(matrix)
}

// @lc code=end

func main() {
	test := [][]int{
		[]int{5, 1, 9, 11},
		[]int{2, 4, 8, 10},
		[]int{13, 3, 6, 7},
		[]int{15, 14, 12, 16}}
	fmt.Println("Nguyen Minh Tuan")
	rotate(test)
}

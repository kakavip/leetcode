package main

import "fmt"

/*
 * @lc app=leetcode id=73 lang=golang
 *
 * [73] Set Matrix Zeroes
 */

// @lc code=start
func setZeroes(matrix [][]int) {
	posList := [][]int{}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == 0 {
				posList = append(posList, []int{i, j})
			}
		}
	}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if _contains([]int{i, j}, posList) {
				matrix[i][j] = 0
			}
		}
	}
}

func _contains(p []int, pList [][]int) bool {
	for i := 0; i < len(pList); i++ {
		if p[0] == pList[i][0] || p[1] == pList[i][1] {
			return true
		}
	}
	return false
}

// @lc code=end

func main() {
	// test := [][]int{[]int{1, 1, 1}, []int{1, 0, 1}, []int{1, 1, 1}}
	test := [][]int{[]int{0, 1, 2, 0}, []int{3, 4, 5, 2}, []int{1, 3, 1, 5}}
	setZeroes(test)
	fmt.Println(test)
}

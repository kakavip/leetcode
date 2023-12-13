/*
 * @lc app=leetcode id=240 lang=golang
 *
 * [240] Search a 2D Matrix II
 */
package main

// @lc code=start
func searchMatrix(matrix [][]int, target int) bool {
	maxRowIdx := -1
	for i := 1; i < len(matrix); i++ {
		if matrix[i][0] > target {
			maxRowIdx = i - 1
			break
		}
		if matrix[i][0] == target {
			return true
		}
	}

	if maxRowIdx == -1 {
		maxRowIdx = len(matrix) - 1
	}

	maxCol := len(matrix[0]) - 1
	for i := maxRowIdx; i >= 0; i-- {
		if matrix[i][maxCol] < target {
			return false
		}

		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] > target {
				break
			}

			if matrix[i][j] == target {
				return true
			}
		}

	}

	return false
}

// @lc code=end

func main() {

}

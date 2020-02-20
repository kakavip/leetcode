package main

import "fmt"

/*
 * @lc app=leetcode id=54 lang=golang
 *
 * [54] Spiral Matrix
 */

// @lc code=start
func spiralOrder(matrix [][]int) []int {
	var m, n int
	m = len(matrix)

	if m > 0 {
		n = len(matrix[0])
	}

	currentCircle := 0
	result := []int{}
	for {
		fmt.Println("Current: ", currentCircle)

		l, t, r, b := []int{}, []int{}, []int{}, []int{}
		if (currentCircle >= n-currentCircle-1) || (currentCircle >= m-currentCircle-1) {
			break
		}

		for i := currentCircle; i < n-currentCircle-1; i++ {
			t = append(t, matrix[currentCircle][i])
		}
		for i := n - currentCircle - 1; i > currentCircle; i-- {
			b = append(b, matrix[m-currentCircle-1][i])
		}

		for i := currentCircle; i < m-currentCircle-1; i++ {
			r = append(r, matrix[i][n-currentCircle-1])
		}
		for i := m - currentCircle - 1; i > currentCircle; i-- {
			l = append(l, matrix[i][currentCircle])
		}

		fmt.Println("l: ", l, " t: ", t, " r: ", r, " b: ", b)

		result = append(result, t...)
		result = append(result, r...)
		result = append(result, b...)
		result = append(result, l...)
		currentCircle++
	}
	if m == n && n > 0 && m%2 != 0 {
		result = append(result, matrix[n/2][n/2])
	} else {
		one := []int{}
		if m > n && n%2 != 0 {
			for i := currentCircle; i < m-currentCircle; i++ {
				one = append(one, matrix[i][n/2])
			}
		}
		if m < n && m%2 != 0 {
			for i := currentCircle; i < n-currentCircle; i++ {
				one = append(one, matrix[m/2][i])
			}
		}
		result = append(result, one...)
	}

	return result
}

// @lc code=end
func main() {
	// test := [][]int{[]int{1, 2, 3}, []int{4, 5, 6}, []int{7, 8, 9}}
	// test := [][]int{[]int{6, 9, 7}}
	// test := [][]int{[]int{1, 2}, []int{3, 4}}
	test := [][]int{[]int{2, 5}, []int{8, 4}, []int{0, -1}}
	// test := [][]int{[]int{1, 2, 3, 4}, []int{5, 6, 7, 8}, []int{9, 10, 11, 12}}
	fmt.Println("result: ", spiralOrder(test))
}

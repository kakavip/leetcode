/*
 * @lc app=leetcode id=89 lang=golang
 *
 * [89] Gray Code
 */
package main

// @lc code=start
import (
	"fmt"
	"math"
)

func grayCode(n int) []int {
	if n == 0 {
		return []int{}
	}
	result := []int{0, 1}
	for i := 1; i <= 16; i++ {
		if i >= n {
			return result
		}

		reverse_arr := []int{}
		for k := 0; k <= len(result)-1; k++ {
			reverse_arr = append(reverse_arr, int(math.Pow(2, float64(i)))+result[len(result)-(k+1)])
		}

		result = append(result, reverse_arr...)
	}

	return result
}

// @lc code=end

func main() {
	fmt.Println(grayCode(3))
}

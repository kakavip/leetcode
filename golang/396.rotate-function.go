/*
 * @lc app=leetcode id=396 lang=golang
 *
 * [396] Rotate Function
 */

package main

import (
	"fmt"
)

// @lc code=start
func maxRotateFunction(nums []int) int {
	n := len(nums)

	_sumNums := 0
	_max := 0
	for i := 0; i < n; i++ {
		_max += i * nums[i]
		_sumNums += nums[i]
	}

	var sum int = _max
	for k := 1; k < n; k++ {
		nSum := (_sumNums - n*nums[n-k]) + sum
		if _max < nSum {
			_max = nSum
		}
		sum = nSum
	}

	return _max
}

// @lc code=end

func main() {
	fmt.Println(maxRotateFunction([]int{4, 3, 2, 6}))
	fmt.Println(maxRotateFunction([]int{100}))
}

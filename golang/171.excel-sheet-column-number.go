package main

import (
	"fmt"
	"math"
)

/*
 * @lc app=leetcode id=171 lang=golang
 *
 * [171] Excel Sheet Column Number
 */

// @lc code=start
func titleToNumber(s string) int {
	result := 0
	for i := 0; i < len(s)-1; i++ {
		val := int(s[i]) - 64
		result += val * int(math.Pow(26, float64((len(s)-1-i))))
	}
	return result + int(s[len(s)-1]) - 64
}

// @lc code=end

func main() {
	fmt.Println(titleToNumber("AAA"))
}

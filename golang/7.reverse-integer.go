/*
 * @lc app=leetcode id=7 lang=golang
 *
 * [7] Reverse Integer
 */
package main

import (
	"math"
	"strconv"
)

// @lc code=start
func reverse(x int) int {
	signed := 1
	if x < 0 {
		signed = -1
		x *= signed
	}

	val, _ := strconv.Atoi(Reverse(strconv.Itoa(x)))

	if val > math.MaxInt32 || val < math.MinInt32 {
		return 0
	}
	return val * signed
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// @lc code=end

func main() {

}

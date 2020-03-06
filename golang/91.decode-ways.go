package main

import (
	"fmt"
	"strconv"
)

/*
 * @lc app=leetcode id=91 lang=golang
 *
 * [91] Decode Ways
 */
// @lc code=start
func numDecodings(s string) int {
	if len(s) == 0 {
		return 1
	}
	// '0' or 'x'
	if len(s) == 1 {
		if s[0] == '0' {
			return 0
		}
		return 1
	}
	otherWay := 0
	if s[0] == '0' {
		return 0
	} else {
		val, err := strconv.ParseInt(s[:2], 10, 32)
		if err == nil && val <= 26 {
			otherWay = numDecodings(s[2:])
		}
		return numDecodings(s[1:]) + otherWay
	}
}

// @lc code=end

func main() {
	fmt.Println("test: ", numDecodings("9317949759856497357254398763219839323723136763131916377913495416692666785978758414629119614215967159"))
}

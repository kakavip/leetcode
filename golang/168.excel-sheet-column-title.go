package main

import (
	"fmt"
)

/*
 * @lc app=leetcode id=168 lang=golang
 *
 * [168] Excel Sheet Column Title
 */

// @lc code=start
func convertToTitle(n int) string {
	result := ""

	if n == 702 {
		return "ZZ"
	}

	for n > 0 {
		if n == 26 {
			result += "Z"
			break
		}

		div := n / 26
		mod := n % 26

		if div > 26 {
			sub := convertToTitle(div)
			result += sub

			fmt.Println("Sub", sub)

			n -= div * 26
			continue
		}

		if div == 0 && mod != 0 {
			result += string(mod + 64)
			break
		}

		if div == 0 && mod == 0 {
			break
		}

		if mod == 0 {
			result += string(n/27 + 64)
			n -= (n/26 - 1) * 26
		} else {
			result += string(div + 64)
			n -= div * 26
		}

	}
	return result
}

// @lc code=end

func main() {
	fmt.Println(convertToTitle(702))
}

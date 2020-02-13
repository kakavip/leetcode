package main

import "fmt"

/*
 * @lc app=leetcode id=28 lang=golang
 *
 * [28] Implement strStr()
 */

// @lc code=start
func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}
	if len(needle) == len(haystack) {
		if needle == haystack {
			return 0
		} else {
			return -1
		}
	}

	for i := 0; i < len(haystack)-len(needle)+1; i++ {
		if haystack[i] == needle[0] {
			if haystack[i:i+len(needle)] == needle {
				return i
			}
		}
	}

	return -1
}

// @lc code=end

func main() {
	haystack := "hello"
	needle := "ll"

	fmt.Println("Index: ", strStr(haystack, needle))
}

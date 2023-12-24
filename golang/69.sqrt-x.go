/*
 * @lc app=leetcode id=69 lang=golang
 *
 * [69] Sqrt(x)
 */
package main

import "fmt"

// @lc code=start
func mySqrt(x int) int {
	if x == 0 {
		return 0
	}
	if x == 1 {
		return 1
	}

	for i := x / 2; i > 0; i /= 2 {
		if i*i <= x {
			for j := i; ; j++ {
				if (j+1)*(j+1) > x {
					return j
				}
			}
		}
	}

	return 0
}

// @lc code=end

func main() {
	fmt.Println(mySqrt(1041080284))
}

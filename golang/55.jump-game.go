package main

import "fmt"

/*
 * @lc app=leetcode id=55 lang=golang
 *
 * [55] Jump Game
 */

// @lc code=start
func canJump(nums []int) bool {

	if len(nums) == 0 || len(nums) == 1 {
		return true
	}

	offsetJump := nums[0]
	if offsetJump >= len(nums) {
		return true
	}
	if offsetJump == 0 {
		return false
	}

	idx := 0
	max := -1
	// fmt.Println("Offset Jump: ", offsetJump)
	// fmt.Print("Max - Sum: ")
	for i := 0; i <= offsetJump; i++ {
		// fmt.Print(max, " - ", nums[i]+i, ", ")
		if max <= nums[i]+i {
			idx = i
			max = nums[i] + i
		}
	}
	// fmt.Println()
	// fmt.Println("Nums: ", nums[idx:], " Max: ", max, " Idx: ", idx)
	return canJump(nums[idx:])
}

// @lc code=end

func main() {
	test := []int{1, 1, 2, 2, 0, 1, 1}
	// test := []int{3, 2, 1, 0, 4}

	fmt.Println("Result: ", canJump(test))
}

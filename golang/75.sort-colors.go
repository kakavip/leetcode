package main

import "fmt"

/*
 * @lc app=leetcode id=75 lang=golang
 *
 * [75] Sort Colors
 */

// @lc code=start
func sortColors(nums []int) {
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] > nums[j] {
				tem := nums[i]
				nums[i] = nums[j]
				nums[j] = tem
			}
		}
	}
}

// @lc code=end
func main() {
	test := []int{2, 0, 2, 1, 1, 0}
	sortColors(test)
	fmt.Println(test)
}

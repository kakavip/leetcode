package main

import "fmt"

// package main

// import "fmt"

/*
 * @lc app=leetcode id=26 lang=golang
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
func removeDuplicates(nums []int) int {
	if len(nums) < 2 {
		return len(nums)
	}

	count := 1
	for i := 1; i < len(nums); i++ {
		if nums[count-1] != nums[i] {
			nums[count] = nums[i]
			count++
		}
	}
	return count
}

// @lc code=end
func main() {
	nums := []int{1, 1, 2}
	fmt.Println("Length: ", removeDuplicates(nums))
}

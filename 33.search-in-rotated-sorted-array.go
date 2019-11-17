package main

import "fmt"

/*
 * @lc app=leetcode id=33 lang=golang
 *
 * [33] Search in Rotated Sorted Array
 */

// @lc code=start
func search(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}
	if len(nums) == 1 {
		if nums[0] == target {
			return 0
		} else {
			return -1
		}
	}

	if target == nums[0] {
		return 0
	}
	if target == nums[len(nums)-1] {
		return len(nums) - 1
	}

	if nums[0] < nums[len(nums)-1] {
		return quickSearch(nums, target, 0)
	}

	mid := len(nums) - nums[0]

	if mid < 1 {
		mid = 1
	}

	findBiggerMid := nums[mid] < target

	for ; mid < len(nums); mid++ {
		if findBiggerMid == true {
			if nums[mid] == target {
				return mid
			}
			if nums[mid] > target {
				return -1
			}
		}
		if nums[mid] < nums[mid-1] {
			break
		}
	}

	if target > nums[0] {
		return quickSearch(nums[0:mid], target, 0)
	}

	return quickSearch(nums[mid:], target, mid)
}

func quickSearch(nums []int, target int, indexBegin int) int {
	if len(nums) == 0 {
		return -1
	}
	if len(nums) == 1 {
		if nums[0] == target {
			return indexBegin
		} else {
			return -1
		}
	}

	mid := len(nums) / 2

	if nums[mid] == target {
		return mid + indexBegin
	}

	if nums[mid] < target {
		return quickSearch(nums[mid:], target, indexBegin+mid)
	}

	return quickSearch(nums[:mid], target, indexBegin)
}

// @lc code=end
func main() {
	nums := []int{0, 1, 3, 4, 6, 8, 9}
	target := 5

	fmt.Println("Index: ", search(nums, target))
}

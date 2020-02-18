package main

import "fmt"

/*
 * @lc app=leetcode id=53 lang=golang
 *
 * [53] Maximum Subarray
 */

// @lc code=start
func maxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	max := nums[0]
	sum := 0
	currentSum := 0
	if nums[0] > 0 {
		currentSum = nums[0]
	}
	if (len(nums) > 1) && (nums[1] < 0) {
		sum += currentSum
	}
	tempNav := 0
	for i := 1; i < len(nums); i++ {
		if max < nums[i] {
			max = nums[i]
		}
		if nums[i] >= 0 {
			currentSum += nums[i]

			if (i < len(nums)-1) && (nums[i+1] < 0) || i+1 == len(nums) { // sum of positive
				if currentSum > max && max > 0 {
					max = currentSum
				}

				if tempNav == 0 {
					sum += currentSum
				}
				if sum > max && max > 0 {
					max = sum
				}
			}
		}
		if nums[i] < 0 {
			// if currentSum == 0 {
			// 	continue
			// }

			if currentSum+nums[i] > 0 || -sum < 3*nums[i]/2 {
				currentSum += nums[i]
				tempNav += nums[i]
			} else {
				// reset sum
				sum = 0
				// reset temp nav
				tempNav = 0
				// reset curren sum
				currentSum = 0
			}

			if (i < len(nums)-1) && nums[i+1] >= 0 {
				if tempNav != 0 {
					sum += tempNav
				}
				// reset currentSum
				currentSum = 0
				// reset tem Nav
				tempNav = 0
			}
		}
		if sum < 0 {
			sum = 0
		}
		// fmt.Println("i: ", i, " value: ", nums[i], " max: ", max, " currentSum: ", currentSum, " sum: ", sum, " tempNav: ", tempNav)
	}
	return max
}

// @lc code=end

func main() {
	// nums := []int{-9, -6, 2, -5, -8, 1, 6, 9, -8, 0, 5, 5, -4, 7, 4, 1, 7, -3, -1}
	// nums := []int{-9, -2, 1, 8, 7, -6, 4, 9, -9, -5, 0, 5, -2, 5, 9, 7}
	nums := []int{-5, 8, -5, 1, 1, -3, 5, 5, -3, -3, 6, 4, -7, -4, -8, 0, -1, -6}
	// nums := []int{6, -7, -4, 4, 5, 9, 7, 2, 0, -8, 1, -5, 9, 7}
	fmt.Println("Max: ", maxSubArray(nums))
}

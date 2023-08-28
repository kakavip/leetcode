/*
 * @lc app=leetcode id=78 lang=golang
 *
 * [78] Subsets
 */

package main

import "fmt"

// @lc code=start

func subsetInLength(nums []int, length int) [][]int {
	result := [][]int{}

	if length == 1 {
		for _, num := range nums {
			result = append(result, []int{num})
		}
	} else {
		for i := 0; i < len(nums)-length+1; i++ {
			rangeNums := subsetInLength(nums[i+1:], length-1)
			// fmt.Println("RANGE NUMS: ", rangeNums)
			for _, _nums := range rangeNums {
				newNums := []int{nums[i]}
				newNums = append(newNums, _nums...)
				result = append(result, newNums)
			}
		}
	}
	return result
}

func subsets(nums []int) [][]int {
	var result [][]int = [][]int{}

	for i := 0; i <= len(nums); i++ {
		if i == 0 {
			result = append(result, []int{})
		} else {
			result = append(result, subsetInLength(nums, i)...)
		}
	}
	return result
}

// @lc code=end

func main() {
	fmt.Println(subsets([]int{1, 2, 3}))
}

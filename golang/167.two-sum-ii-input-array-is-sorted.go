/*
 * @lc app=leetcode id=167 lang=golang
 *
 * [167] Two Sum II - Input Array Is Sorted
 */
package main

import "fmt"

// @lc code=start
func twoSum(numbers []int, target int) []int {
	for i := 0; i < len(numbers)-1; i++ {
		if numbers[i]*2 > target {
			break
		}

		for j := i + 1; j < len(numbers); j++ {
			if numbers[i]+numbers[j] == target {
				return []int{i + 1, j + 1}
			}
		}
	}

	return []int{}
}

// @lc code=end

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSum([]int{2, 3, 4}, 6))
	fmt.Println(twoSum([]int{-1, 0}, -1))
	fmt.Println(twoSum([]int{0, 0, 3, 4}, 0))
}

package main

import (
	"fmt"
)

/*
 * @lc app=leetcode id=56 lang=golang
 *
 * [56] Merge Intervals
 */

// @lc code=start
func merge(intervals [][]int) [][]int {
	if len(intervals) == 0 {
		return [][]int{}
	}
	result := [][]int{intervals[0]}
	for i := 1; i < len(intervals); i++ {
		if len(result) == 0 {
			result = append(result, intervals[i])
		} else {
			canMergedList := [][]int{}
			cantMergedList := [][]int{}

			// isMerged := false

			for j := 0; j < len(result); j++ {
				// if intervals[i][1] < result[j][0] {
				// 	resultClone := append([][]int{}, result[:j]...)
				// 	resultClone = append(resultClone, intervals[i])
				// 	result = append(resultClone, result[j:]...)
				// 	isInserted = true
				// 	break
				// }
				if canMerge(result[j], intervals[i]) {
					canMergedList = append(canMergedList, result[j])
					// result[j] = mergeNums(result[j], intervals[i])
					// isMerged = true
					// break
				} else {
					cantMergedList = append(cantMergedList, result[j])
				}
			}

			// Insert
			var nums []int
			if len(canMergedList) == 0 {
				nums = intervals[i]
			} else {
				nums = mergeNums(append(canMergedList, intervals[i]))
			}

			// if isMerged == true {
			// 	fmt.Println("list of can't merge: ", cantMergedList)
			// 	fmt.Println("list of can merge: ", canMergedList)
			// 	fmt.Println("Nums: ", nums)
			// }

			if len(cantMergedList) == 0 {
				result = append([][]int{}, nums)
			} else {
				isInserted := false
				for j := 0; j < len(cantMergedList); j++ {
					if cantMergedList[j][0] > nums[1] {
						cloneNums := append([][]int{}, cantMergedList[:j]...)
						cloneNums = append(cloneNums, nums)
						result = append(cloneNums, cantMergedList[j:]...)

						isInserted = true
						break
					}
				}

				if isInserted == false {
					result = append(cantMergedList, nums)
				}
			}
		}
	}

	return result
}

func mergeNums(nums [][]int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	x, y := nums[0][0], nums[0][1]
	for i := 1; i < len(nums); i++ {
		if x > nums[i][0] {
			x = nums[i][0]
		}
		if y < nums[i][1] {
			y = nums[i][1]
		}
	}

	// fmt.Println("X: ", x, " Y: ", y)
	return []int{x, y}
}

func canMerge(firstNums, secondNums []int) bool {
	if firstNums[0] > secondNums[1] || secondNums[0] > firstNums[1] {
		return false
	}
	return true
}

// @lc code=end

func main() {
	// test := [][]int{[]int{1, 3}, []int{2, 6}, []int{8, 10}, []int{15, 18}}
	// test := [][]int{[]int{2, 3}, []int{4, 5}, []int{6, 7}, []int{8, 9}, []int{1, 10}}
	test := [][]int{[]int{1, 4}, []int{4, 5}}
	fmt.Println("Result: ", merge(test))
}

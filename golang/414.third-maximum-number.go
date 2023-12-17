/*
 * @lc app=leetcode id=414 lang=golang
 *
 * [414] Third Maximum Number
 */
package main

import (
	"fmt"
	"slices"
)

// @lc code=start
func thirdMax(nums []int) int {
	var idx int
	var one, two, three *int
	for idx = 0; idx < len(nums); idx++ {
		if one == nil {
			one = &nums[idx]
			continue
		}

		if two == nil {
			if nums[idx] != *one {
				two = &nums[idx]
			}
			continue
		}

		if three == nil {
			if nums[idx] != *one && nums[idx] != *two {
				three = &nums[idx]
			}
			continue
		}
		break
	}

	if three == nil {
		var _max *int
		if two != nil {
			_max = two
		}

		if one != nil {
			if _max == nil {
				_max = one
			} else {
				*_max = max(*one, *_max)
			}
		}

		return *_max
	}

	var maxFirst, maxSecond, maxThird int

	var threeNums []int = []int{*one, *two, *three}

	maxFirst = slices.Max(threeNums)
	maxThird = slices.Min(threeNums)
	maxSecond = threeNums[0] + threeNums[1] + threeNums[2] - (maxFirst + maxThird)

	for i := idx; i < len(nums); i++ {
		v := nums[i]
		if v == maxFirst || v == maxSecond || v == maxThird {
			continue
		}

		var temp int
		if v > maxFirst {
			temp = maxFirst
			maxFirst = v
			v = temp
		}

		if v > maxSecond {
			temp = maxSecond
			maxSecond = v
			v = temp
		}

		if v > maxThird {
			temp = maxThird
			maxThird = v
		}

	}

	return maxThird
}

// @lc code=end

func main() {
	fmt.Println(thirdMax([]int{3, 2, 1}))
	fmt.Println(thirdMax([]int{1, 2}))
}

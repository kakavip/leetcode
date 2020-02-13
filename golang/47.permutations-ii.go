package main

import (
	"fmt"
	"reflect"
	"sort"
)

/*
 * @lc app=leetcode id=47 lang=golang
 *
 * [47] Permutations II
 */

// @lc code=start

func permuteUnique(nums []int) [][]int {
	result := [][]int{}

	sort.Ints(nums)
	getFullValue(&result, nums, []int{})

	return result
}

func swapInt(a *int, b *int) {
	var tmp int = *a
	*a = *b
	*b = tmp
}

func getFullValue(result *[][]int, curNums []int, resultNums []int) {

	if len(curNums) == 0 {

		numsClone := append([]int{}, resultNums...)

		if existed(*result, resultNums) == false {
			*result = append(*result, numsClone)
		}
	}

	uniqueNums := uniqueMapNums(curNums)

	// fmt.Println("Unique Nums: ", uniqueNums, ", Result Nums: ", resultNums)

	for i := 0; i < len(uniqueNums); i++ {
		indexNumsClone := append([]int{}, curNums[:uniqueNums[i].idx]...)
		indexNumsClone = append(indexNumsClone, curNums[uniqueNums[i].idx+1:]...)

		resultNumClones := append(resultNums, uniqueNums[i].val)
		getFullValue(result, indexNumsClone, resultNumClones)
	}
}

type UniqueMap struct {
	idx, val int
}

func setUniqueMap(idx, val int) UniqueMap {
	var _result UniqueMap
	_result.idx = idx
	_result.val = val
	return _result
}

func uniqueMapNums(nums []int) []UniqueMap {
	_result := []UniqueMap{}
	if len(nums) == 0 {
		return _result
	}

	_result = append(_result, setUniqueMap(0, nums[0]))

	for i := 1; i < len(nums); i++ {
		if nums[i] != _result[len(_result)-1].val {
			_result = append(_result, setUniqueMap(i, nums[i]))
		}
	}
	return _result
}

func existed(baseNums [][]int, newItem []int) bool {
	for i := 0; i < len(baseNums); i++ {
		if reflect.DeepEqual(baseNums[i], newItem) {
			return true
		}
	}
	return false
}

// @lc code=end

func main() {
	nums := []int{-1, 2, -1, 2, 1, -1, 2, 1}
	permuteUnique(nums)
	// fmt.Println("Result: ", result)
}

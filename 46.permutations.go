package main

import (
	"fmt"
	"sort"
)

/*
 * @lc app=leetcode id=46 lang=golang
 *
 * [46] Permutations
 */

// @lc code=start
// var resultPos [][]int = [][]int{}

func permute(nums []int) [][]int {
	initNums := initMem(len(nums))
	resultPos := [][]int{}
	getFullPosition(&resultPos, initNums)

	for i := 0; i < len(resultPos); i++ {
		for j := 0; j < len(resultPos[i]); j++ {
			pos := resultPos[i][j]
			resultPos[i][j] = nums[pos]
		}
	}

	return resultPos
}

func getFullPosition(result *[][]int, indexNums []int) {
	// Check available positions
	avaiPos := []int{}

	for i := 0; i < len(indexNums); i++ {
		if indexNums[i] == -1 {
			avaiPos = append(avaiPos, i) // get available position
		}
	}

	// fmt.Println("----------", len(avaiPos), "---------")

	// return if full position
	if len(avaiPos) == 0 {
		// fmt.Println(indexNums)
		*result = append(*result, indexNums)
		return
	}

	nextPos := getMaxOfNums(indexNums) + 1

	if len(avaiPos) == len(indexNums) {
		// fmt.Println("Index Nums: ", indexNums, "avai pos: ", avaiPos)
	}

	for i := 0; i < len(avaiPos); i++ {
		indexNumsClone := append([]int{}, indexNums...)
		indexNumsClone[avaiPos[i]] = nextPos
		// fmt.Println("Index Nums: ", indexNums, "avai pos: ", avaiPos)
		// fmt.Println("Chosen postion: ", avaiPos[i], "Updated index Nums: ", indexNumsClone)
		getFullPosition(result, indexNumsClone)
	}
}

func initMem(len int) []int {
	result := []int{}
	for i := 0; i < len; i++ {
		result = append(result, -1)
	}
	return result
}

func getMaxOfNums(nums []int) int {
	numsClone := append([]int{}, nums...)

	if len(numsClone) == 0 {
		return -1
	}

	sort.Ints(numsClone)

	return numsClone[len(numsClone)-1]
}

// func insertInNums(nums []int, insertValue int, begin int) [][]int {
// 	result := [][]int{}

// 	fmt.Println("Nums: ", nums, "Inserted Value: ", insertValue)

// 	for i := begin; i < len(nums); i++ {
// 		fakeNums := append([]int{}, nums...)

// 		fmt.Println("Fake Nums: ", fakeNums)

// 		frontNums := append([]int{}, fakeNums[:i]...)
// 		backNums := append([]int{}, fakeNums[i:]...)

// 		resultNums := append(frontNums, insertValue)
// 		resultNums = append(resultNums, backNums...)

// 		fmt.Println("Value: ", insertValue, "frontNums: ", frontNums, "backNums: ", backNums, "resultNums: ", resultNums)

// 		result = append(result, resultNums)
// 	}

// 	result = append(result, append(nums, insertValue))

// 	fmt.Println("Result: ", result)

// 	return result
// }

// @lc code=end

func main() {
	nums := []int{1, 2, 3, 4, 5}

	fmt.Println("Result: ", permute(nums))
}

package main

import (
	"fmt"
	"reflect"
	"sort"
)

func algorithmTwo(nums []int) [][]int {
	result := [][]int{}

	if len(nums) < 3 {
		return result
	}

	newNums := getArrayUnique(nums, 3)
	// sort.Ints(nums)
	// newNums := nums

	// // fmt.Println("New array: ", newNums)
	// indexPositiveMin := findIndexPositiveMin(newNums)
	// // fmt.Println("Boundary: ", indexPositiveMin)
	// markPosition := len(newNums) - 2
	// if markPosition > indexPositiveMin {
	// 	markPosition = indexPositiveMin
	// }

	for i := 0; i < len(newNums)-2; i++ {

		if i > 0 && newNums[i] == newNums[i-1] {
			continue
		}

		if i > 0 && newNums[i] > 0 && newNums[i-1] <= 0 {
			break
		}
		front := i + 1
		back := len(newNums) - 1

		for front < back && newNums[back] >= 0 {

			// // fmt.Println("front: ", front, "back: ", back)
			sum := newNums[back] + newNums[front] + newNums[i]
			if sum < 0 {
				front++
			} else if sum > 0 {
				back--
			} else {
				matchedNums := []int{
					newNums[i],
					newNums[front],
					newNums[back],
				}

				result = append(result, matchedNums)

				for front+1 < back && newNums[front] == newNums[front+1] {
					front++
				}
				for front < back-1 && newNums[back] == newNums[back-1] {
					back--
				}

				front++
				back--
			}
		}
	}
	return result
}

func findIndexPositiveMin(nums []int) int {
	indexPositiveMin := 0
	for i := 0; i < len(nums); i++ {
		// Get index positive min
		if nums[i] >= 0 && indexPositiveMin == 0 {
			indexPositiveMin = i
			break
		}
	}

	return indexPositiveMin
}

func algorithmOne(nums []int) [][]int {
	result := [][]int{}

	if len(nums) < 3 {
		return result
	}

	newNums := getArrayUnique(nums, 3)

	// // fmt.Println("New array: ", newNums)
	indexPositiveMin := findIndexPositiveMin(newNums)
	// fmt.Println("Boundary: ", indexPositiveMin)

	// Calculate range three
	thirdRangeTemp := newNums[indexPositiveMin:len(newNums)]
	// fmt.Println("---->Third Range Temp: ", thirdRangeTemp)
	for one := 0; one <= indexPositiveMin; one++ {
		markStartThree := 0
		dynamicIndex := -1
		thirdArray := []int{}
		// One is navigate
		for two := one + 1; two < len(newNums)-1; two++ {
			sumTwoFirst := newNums[one] + newNums[two]
			// Break Not loop
			if sumTwoFirst+newNums[two+1] > 0 {
				break
			}

			// Three is positive
			if two+1 > indexPositiveMin {
				markStartThree = two + 1 - indexPositiveMin
			}

			// Find third num
			if dynamicIndex != -1 && markStartThree <= dynamicIndex {
				// fmt.Println("Dynamic index: ", dynamicIndex, ", Mark start three: ", markStartThree, ", Second value: ", newNums[two], ", First value: ", newNums[one])
				// Not loop

				thirdArray = thirdRangeTemp[markStartThree : dynamicIndex+1]
			} else {
				thirdArray = thirdRangeTemp[markStartThree:len(thirdRangeTemp)]
			}

			// fmt.Println("Third Array: ", thirdArray)
			num, status, index := findNumPartner(sumTwoFirst, thirdArray, 0)
			if status == true && (newNums[one] <= newNums[two] && newNums[two] <= num) {
				dynamicIndex = index + markStartThree
				matchedNums := []int{newNums[one], newNums[two], num}

				if len(result) == 0 || reflect.DeepEqual(matchedNums, result[len(result)-1]) == false {
					result = append(result, matchedNums)
				}

				// fmt.Println("Matched Nums: ", matchedNums)
			}

			for ; two < len(newNums)-1 && newNums[two] == newNums[two+1]; two++ {
				// two++
			}
		}
		// reduce duplicate
		for ; one < len(newNums)-1 && newNums[one] == newNums[one+1]; one++ {
			// one ++
		}
	}
	// Return
	return result
}

/*
 * @lc app=leetcode id=15 lang=golang
 *
 * [15] 3Sum
 */
func threeSum(nums []int) [][]int {
	return algorithmOne(nums)
	// return algorithmTwo(nums)
}

func containTriplets(nums []int, numsList [][]int) bool {
	for i := 0; i < len(numsList); i++ {
		// // fmt.Println(nums)
		// // fmt.Println(numsList[i])
		if reflect.DeepEqual(nums, numsList[i]) {
			return true
		}
	}
	return false
}

func findNumPartner(partner int, nums []int, index int) (int, bool, int) {
	if len(nums) == 0 || partner+nums[0] > 0 || partner+nums[len(nums)-1] < 0 {
		return 0, false, -1
	}
	indexMid := int(len(nums) / 2)
	mid := nums[indexMid]
	// // fmt.Println("Third Nums: ", nums, ", Partner: ", partner, "Mid: ", mid)

	if partner+mid == 0 {
		return mid, true, indexMid + index
	}
	if len(nums) <= 1 {
		return 0, false, -1
	}
	// Bigger
	if partner+mid < 0 {
		return findNumPartner(partner, nums[indexMid:len(nums)], index+indexMid)
	}
	//Smaller
	return findNumPartner(partner, nums[0:indexMid], index)
}

func getArrayUnique(nums []int, amount int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	sort.Ints(nums)
	newNums := []int{nums[0]}
	// Get new array
	counter := 1
	for i := 1; i < len(nums); i++ {
		counter++
		if nums[i] != nums[i-1] {
			counter = 1
		}
		if counter <= amount {
			newNums = append(newNums, nums[i])
		}
	}
	return newNums
}

func main() {
	realResultList := [][][]int{
		[][]int{[]int{-2, 0, 2}, []int{-2, 1, 1}},
		[][]int{[]int{-4, -2, 6}, []int{-4, 0, 4}, []int{-4, 1, 3}, []int{-4, 2, 2}, []int{-2, -2, 4}, []int{-2, 0, 2}},
		[][]int{[]int{-10, 1, 9}, []int{-10, 2, 8}, []int{-10, 3, 7}, []int{-10, 4, 6}, []int{-8, -1, 9}, []int{-8, 1, 7}, []int{-8, 2, 6}, []int{-8, 3, 5}, []int{-5, -4, 9}, []int{-5, -1, 6}, []int{-5, 1, 4}, []int{-5, 2, 3}, []int{-4, -4, 8}, []int{-4, -1, 5}, []int{-4, 1, 3}, []int{-4, 2, 2}},
	}
	arrayTestList := [][]int{
		[]int{-2, 0, 1, 1, 2},
		[]int{-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6},
		[]int{5, 1, -4, -10, 9, -1, -4, -5, -8, 3, 1, 4, 2, -8, -4, 3, -4, -5, 1, 7, 8, 6, 2, 8},
	}

	fmt.Println("Unit Test: ", checkUnitTest(arrayTestList, realResultList))
}

func checkUnitTest(arrayTest [][]int, realResultList [][][]int) bool {
	if len(arrayTest) != len(realResultList) {
		panic("Please check value of tests.")
	}
	for i := 0; i < len(realResultList); i++ {
		if reflect.DeepEqual(threeSum(arrayTest[i]), realResultList[i]) == false {
			// fmt.Println("--------------Error-------------")
			// fmt.Println("Result: ", threeSum(arrayTest[i]))
			// fmt.Println("Expected: ", realResultList[i])
			return false
		}
	}
	return true
}

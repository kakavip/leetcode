/*
 * @lc app=leetcode id=42 lang=golang
 *
 * [42] Trapping Rain Water
 */
package main

import (
	"fmt"
)

// @lc code=start
var debug bool = false

func contains(slice []int, item int) bool {
	for _, s := range slice {
		if s == item {
			return true
		}
	}
	return false
}

func fillWater(height []int) int {
	result := 0

	heightWater := height[0]
	if heightWater > height[len(height)-1] {
		heightWater = height[len(height)-1]
	}
	for i := 1; i < len(height)-1; i++ {
		if heightWater-height[i] > 0 {
			result += heightWater - height[i]
		}
	}

	return result
}

func findNewPeaks(height []int, oldPeakIds []int) ([]int, bool) {
	newPeakIndex := []int{}
	newPeakIds := []int{}
	checkPeakIds := append(oldPeakIds, len(height)-1)
	state := "INC"

	for idx := 1; idx < len(checkPeakIds); idx++ {
		if state == "INC" {
			if height[checkPeakIds[idx]] < height[checkPeakIds[idx-1]] {
				// if debug {
				// 	fmt.Println("SUB DESC PEAK IDS: ", subDescPeakIds)
				// }
				if debug {
					fmt.Println("NEW PEAK IDS: ", newPeakIds, " - ", checkPeakIds[idx-1])
				}
				if len(newPeakIds) > 0 {
					for i := newPeakIds[len(newPeakIds)-1]; i < checkPeakIds[idx-1]; i++ {
						if height[i] >= height[checkPeakIds[idx-1]] {
							if !contains(newPeakIds, i) {
								newPeakIds = append(newPeakIds, i)
							}

						} else {
							// break
						}
					}
				}

				// CHOOSE NEW PEAK
				if !contains(newPeakIds, checkPeakIds[idx-1]) {
					newPeakIds = append(newPeakIds, checkPeakIds[idx-1])
				}
				newPeakIndex = append(newPeakIndex, idx-1)

				state = "DESC"
				continue
			} else if len(newPeakIds) > 0 && height[checkPeakIds[idx]] >= height[newPeakIds[len(newPeakIds)-1]] {
				// fmt.Println("DEBUG NEW PEAK IDS: ", newPeakIds, " ", checkPeakIds[idx])
				newPeakIds = append(newPeakIds, checkPeakIds[idx])
				newPeakIndex = append(newPeakIndex, idx)

				// fmt.Println("DEBUG NEW PEAK APPEND: ", checkPeakIds[idx])
			}
		}

		if state == "DESC" {
			if height[checkPeakIds[idx]] > height[checkPeakIds[idx-1]] {
				state = "INC"

				if len(newPeakIds) > 0 && height[checkPeakIds[idx]] >= height[newPeakIds[len(newPeakIds)-1]] {
					// fmt.Println("DEBUG NEW PEAK IDS: ", newPeakIds, " ", checkPeakIds[idx])
					newPeakIds = append(newPeakIds, checkPeakIds[idx])
					newPeakIndex = append(newPeakIndex, idx)

					// fmt.Println("DEBUG NEW PEAK APPEND: ", checkPeakIds[idx])
				}
			} else {
			}
		}
	}

	if debug {
		fmt.Println("NEW PEAK IDS: ", newPeakIds)
	}

	var isFinal bool
	finalPeakIds := []int{}
	if len(newPeakIds) < 2 {
		finalPeakIds = newPeakIds
		isFinal = true
	} else {
		finalPeakIds = append(finalPeakIds, checkPeakIds[:newPeakIndex[0]]...)
		finalPeakIds = append(finalPeakIds, newPeakIds...)
		finalPeakIds = append(finalPeakIds, checkPeakIds[newPeakIndex[len(newPeakIndex)-1]+1:]...)

		isFinal = false
	}

	return finalPeakIds, isFinal
}

func trap(height []int) int {
	height = append(height, -1)
	if debug {
		fmt.Println("HEIGHT: ", height)
	}

	var total int = 0

	state := "INC" // INC/DESC
	peakIds := []int{}
	for idx, _ := range height {
		if idx == 0 {
			continue
		}
		if state == "INC" && height[idx] < height[idx-1] {

			peakIds = append(peakIds, idx-1)
			state = "DESC"
			continue
		}
		if state == "DESC" && height[idx] > height[idx-1] {
			state = "INC"
		}
	}

	if debug {
		fmt.Println("PEAK IDS: ", peakIds)
		fmt.Print("PEAK VALUES: ")
		for _, id := range peakIds {
			fmt.Print(height[id], " ")
		}
		fmt.Print("\n")
	}

	findPeakCounter := 0
	var newPeakIds, finalPeakIds []int
	var oldPeakIds []int = peakIds
	var oldFinalPeakIds []int = peakIds
	for true {
		finalNPeakIds, isNFinal := findNewPeaks(height, oldPeakIds)
		if debug {
			fmt.Println("NEW PEAK IDS: ", newPeakIds, " - NEW FINAL PEAK IDS: ", finalPeakIds, "IS FINAL: ", isNFinal)
		}

		if !isNFinal {
			oldPeakIds = finalNPeakIds
			oldFinalPeakIds = finalNPeakIds
		} else {
			break
		}
		if debug {
			fmt.Println("RE-CALC NEW PEAKS")
		}
		findPeakCounter += 1
	}

	finalPeakIds = oldFinalPeakIds

	if debug {
		fmt.Println("FINAL PEAK IDS: ", finalPeakIds)
		fmt.Print("FINAL PEAK VALUES: ")
		for _, id := range finalPeakIds {
			fmt.Print(height[id], " ")
		}
		fmt.Print("\n")
	}

	for i := 1; i < len(finalPeakIds); i++ {
		total += fillWater(height[finalPeakIds[i-1] : finalPeakIds[i]+1])
	}

	return total
}

// @lc code=end

func assert(a int, b int) {
	if a != b {
		errorMsg := fmt.Sprintf("Wrong answer %d != %d", a, b)
		panic(errorMsg)
	}
}

func main() {
	debug = true

	assert(trap([]int{4, 2, 0, 3, 2, 5}), 9)

	assert(trap([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}), 6)
	assert(trap([]int{5, 4, 1, 2}), 1)
	assert(trap([]int{0, 1, 2, 0, 3, 0, 1, 2, 0, 0, 4, 2, 1, 2, 5, 0, 1, 2, 0, 2}), 26)
	assert(trap([]int{5, 1, 8, 8, 1, 4, 0, 5, 0, 1, 0, 6, 6, 8, 5, 2, 2, 2}), 53)
	assert(trap([]int{4, 7, 7, 5, 3, 3, 4, 9, 5, 8, 6, 2, 0, 6, 2, 7, 4}), 35)

}

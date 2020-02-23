package main

import "fmt"

/*
 * @lc app=leetcode id=88 lang=golang
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
func merge(nums1 []int, m int, nums2 []int, n int) {
	nums := []int{}
	for i := 0; i < m; i++ {
		nums = append(nums, nums1[i])
	}
	// fmt.Println("Nums: ", nums)
	pos := 0
	for {
		if pos == m+n {
			break
		}
		fmt.Println("Nums: ", nums, " Nums2: ", nums2)
		if len(nums) > 0 && len(nums2) > 0 {
			if nums[0] < nums2[0] {
				// fmt.Println(pos)
				nums1[pos] = nums[0]
				nums = nums[1:]
			} else {
				nums1[pos] = nums2[0]
				nums2 = nums2[1:]
			}
		} else {
			if len(nums) > 0 {
				nums1[pos] = nums[0]
				nums = nums[1:]
			}
			if len(nums2) > 0 {
				nums1[pos] = nums2[0]
				nums2 = nums2[1:]
			}
		}
		pos++
	}

}

// @lc code=end

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	nums2 := []int{2, 5, 6}
	merge(nums1, 3, nums2, 3)
	fmt.Println(nums1)
}

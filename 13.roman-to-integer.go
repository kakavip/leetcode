package main

import "fmt"

// package main

// import "fmt"

/*
 * @lc app=leetcode id=13 lang=golang
 *
 * [13] Roman to Integer
 */

// @lc code=start
func romanToInt(s string) int {
	if len(s) == 0 {
		return 0
	}
	sum := 0

	for i := 0; i < len(s); i++ {
		value := -1
		if i < len(s)-1 {
			value = romanToInteger(s[i : i+2])
		} else {
			value = romanToInteger(s[i : i+1])
		}
		if value != -1 {
			sum += value
			i++
			continue
		}
		sum += romanToInteger(s[i : i+1])
	}
	return sum
}

func romanToInteger(r string) int {
	switch r {
	case "I":
		return 1
	case "V":
		return 5
	case "X":
		return 10
	case "L":
		return 50
	case "C":
		return 100
	case "D":
		return 500
	case "M":
		return 1000
	case "IV":
		return 4
	case "IX":
		return 9
	case "XL":
		return 40
	case "XC":
		return 90
	case "CD":
		return 400
	case "CM":
		return 900
	default:
		return -1
	}
}

// @lc code=end

func main() {
	s := "MCMXCIV"

	fmt.Println(romanToInt(s))
}

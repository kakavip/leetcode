package main

import "fmt"

// import "fmt"

/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

// @lc code=start
func isValid(s string) bool {
	str := []byte{}
	for i := 0; i < len(s); i++ {
		if len(str) == 0 || trueBracket(str[len(str)-1], s[i]) == false {
			str = append(str, s[i])
		} else {
			str = str[0 : len(str)-1]
		}
	}

	return len(str) == 0
}

func trueBracket(open, close byte) bool {
	switch open {
	case '(':
		return close == ')'
	case '{':
		return close == '}'
	case '[':
		return close == ']'
	default:
		return false
	}
}

// @lc code=end

func main() {
	fmt.Println(isValid("()"))
}

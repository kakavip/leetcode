/*
 * @lc app=leetcode id=290 lang=golang
 *
 * [290] Word Pattern
 */
package main

import (
	"fmt"
	"strings"
)

// @lc code=start
func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")
	if len(words) != len(pattern) {
		return false
	}

	dict := make(map[byte]string)
	reverse_dict := make(map[string]byte)

	for i := 0; i < len(pattern); i++ {
		val, err := dict[pattern[i]]
		if err == false {
			_, err2 := reverse_dict[words[i]]
			if err2 == true {
				return false
			}

			dict[pattern[i]] = words[i]
			reverse_dict[words[i]] = pattern[i]
		} else if val != words[i] {
			return false
		}
	}

	return true
}

// @lc code=end

func main() {

	fmt.Println(wordPattern("abba", "dog cat cat dog"))
	fmt.Println(wordPattern("aaaa", "dog cat cat dog"))
	fmt.Println(wordPattern("abba", "dog dog dog dog"))

}

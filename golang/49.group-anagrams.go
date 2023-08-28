/*
 * @lc app=leetcode id=49 lang=golang
 *
 * [49] Group Anagrams
 */

package main

// @lc code=start
import (
	"fmt"
	"sort"
)

func sortedString(word string) string {
	s := []rune(word)
	sort.Slice(s, func(i int, j int) bool { return s[i] < s[j] })

	return string(s)
}

func groupAnagrams(strs []string) [][]string {
	wordMap := make(map[string][]string)
	for _, str := range strs {
		sortedStr := sortedString(str)

		words, e := wordMap[sortedStr]
		if e {
			words = append(words, str)
			wordMap[sortedStr] = words
		} else {
			wordMap[sortedStr] = []string{str}
		}
	}

	result := [][]string{}
	for _, words := range wordMap {
		result = append(result, words)
	}

	return result
}

// @lc code=end

func main() {
	fmt.Println(groupAnagrams([]string {"eat","tea","tan","ate","nat","bat"}))
}

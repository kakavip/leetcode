/*
 * @lc app=leetcode id=140 lang=golang
 *
 * [140] Word Break II
 */
package main

import (
	"fmt"
	"strings"
)

// @lc code=start
func parseWords(s string, matchedWords []string) ([]string, bool) {
	result := []string{}

	for _, mWord := range matchedWords {
		if strings.HasPrefix(s, mWord) {
			_lenMWord := len(mWord)

			if len(s[_lenMWord:]) > 0 {
				partS, _ := parseWords(s[_lenMWord:], matchedWords)

				for _, p := range partS {
					result = append(result, s[:_lenMWord]+" "+p)
				}

			} else {
				result = append(result, s[:_lenMWord])
			}
		}
	}

	return result, true

}

func wordBreak(s string, wordDict []string) []string {
	result := []string{}

	matchedWords := []string{}
	for _, word := range wordDict {
		if strings.Contains(s, word) {
			matchedWords = append(matchedWords, word)
		}
	}

	result, _ = parseWords(s, matchedWords)

	return result
}

// @lc code=end

func main() {
	var result []string

	result = wordBreak("catsanddog", []string{"cat", "cats", "and", "sand", "dog"})
	result = wordBreak("pineapplepenapple", []string{"apple", "pen", "applepen", "pine", "pineapple"})
	result = wordBreak("catsandog", []string{"cats", "dog", "sand", "and", "cat"})
	for _, r := range result {
		fmt.Println(r)
	}
}

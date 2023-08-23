/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 */
package main

import "fmt"

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}

	char_caches := make(map[byte]bool)
	s = s + string(s[len(s)-1])

	_maxLen := 0
	_sIdx, _eIdx := -1, -1
	for idx := 0; idx < len(s); idx++ {
		if _sIdx == -1 {
			_sIdx = idx

			char_caches[s[idx]] = true
			continue
		}

		_, err := char_caches[s[idx]]
		if err == true {
			_eIdx = idx

			if _eIdx-_sIdx > _maxLen {
				_maxLen = _eIdx - _sIdx
			}

			for i := _sIdx; i < _eIdx; i++ {
				if s[i] != s[idx] {
					delete(char_caches, s[i])
				} else {
					_sIdx = i + 1
					break
				}
			}

		} else {
			char_caches[s[idx]] = true
		}
	}

	return _maxLen
}

// @lc code=end

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
	fmt.Println(lengthOfLongestSubstring("bbbbb"))
	fmt.Println(lengthOfLongestSubstring("pwwkew"))
	fmt.Println(lengthOfLongestSubstring(" "))

}

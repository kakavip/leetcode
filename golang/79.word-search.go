package main

import "fmt"

/*
 * @lc app=leetcode id=79 lang=golang
 *
 * [79] Word Search
 */

// @lc code=start
func exist(board [][]byte, word string) bool {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			if board[i][j] == word[0] {
				result := _find(word, board, 'X', [][]int{[]int{i, j}})
				if result == true {
					return true
				}
			}
		}
	}
	return false
}

// 'L' 'T' 'R' 'B'
func _find(word string, board [][]byte, his byte, hisPos [][]int) bool {
	l, t, r, b := false, false, false, false

	cur := hisPos[len(hisPos)-1]

	if board[cur[0]][cur[1]] != word[0] {
		return false
	}
	if len(word) == 1 {
		return true
	}

	if his != 'L' && cur[1] >= 1 && !_checkExist(hisPos, []int{cur[0], cur[1] - 1}) {
		// fmt.Print("L")
		wordClone := word[1:]
		l = _find(wordClone, board, 'R', append(hisPos, []int{cur[0], cur[1] - 1}))
	}
	if l == true {
		return true
	}

	if his != 'T' && cur[0] >= 1 && !_checkExist(hisPos, []int{cur[0] - 1, cur[1]}) {
		// fmt.Print("T")
		wordClone := word[1:]
		t = _find(wordClone, board, 'B', append(hisPos, []int{cur[0] - 1, cur[1]}))
	}
	if t == true {
		return true
	}

	if his != 'R' && cur[1] < len(board[0])-1 && !_checkExist(hisPos, []int{cur[0], cur[1] + 1}) {
		// fmt.Print("R")
		wordClone := word[1:]
		r = _find(wordClone, board, 'L', append(hisPos, []int{cur[0], cur[1] + 1}))
	}
	if r == true {
		return true
	}

	if his != 'B' && cur[0] < len(board)-1 && !_checkExist(hisPos, []int{cur[0] + 1, cur[1]}) {
		// fmt.Print("B")
		wordClone := word[1:]
		b = _find(wordClone, board, 'T', append(hisPos, []int{cur[0] + 1, cur[1]}))
	}
	return l || t || r || b
}

func _checkExist(base [][]int, nums []int) bool {
	for i := 0; i < len(base); i++ {
		if nums[0] == base[i][0] && nums[1] == base[i][1] {
			return true
		}
	}
	return false
}

// @lc code=end

func main() {
	// board := [][]byte{[]byte{'A', 'B', 'C', 'E'}, []byte{'S', 'F', 'C', 'S'}, []byte{'A', 'D', 'E', 'E'}}
	// board := [][]byte{[]byte{'A', 'B'}, []byte{'C', 'D'}}
	board := [][]byte{[]byte{'A'}}
	// board := [][]byte{
	// 	[]byte{'a', 'a', 'a', 'a'},
	// 	[]byte{'a', 'a', 'a', 'a'},
	// 	[]byte{'a', 'a', 'a', 'a'},
	// }
	// word := "ABCCED"
	// word := "SEE"
	// word := "aaaaaaaaaaaaa"
	word := "A"
	// fmt.Println(len(word))
	fmt.Println(exist(board, word))
}

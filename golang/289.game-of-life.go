/*
 * @lc app=leetcode id=289 lang=golang
 *
 * [289] Game of Life
 */
package main

import "fmt"

// @lc code=start
func gameOfLife(board [][]int) {
	if len(board) == 0 {
		return
	}

	maxX, maxY := len(board[0]), len(board)
	temp := make([]int, len(board)*len(board[0]))

	for y, _ := range board {
		for x, vx := range board[y] {
			temp[maxX*y+x] = vx

			numLive, numDead := 0, 0

			// LEFT
			if x > 0 {
				if temp[maxX*y+x-1] == 0 {
					numDead += 1
				} else {
					numLive += 1
				}
			}
			// UP-LEFT
			if x > 0 && y > 0 {
				if temp[maxX*(y-1)+x-1] == 0 {
					numDead += 1
				} else {
					numLive += 1
				}
			}
			// UP
			if y > 0 {
				if temp[maxX*(y-1)+x] == 0 {
					numDead += 1
				} else {
					numLive += 1
				}
			}
			// UP-RIGHT
			if y > 0 && x < maxX-1 {
				if temp[maxX*(y-1)+x+1] == 0 {
					numDead += 1
				} else {
					numLive += 1
				}
			}
			// RIGHT
			if x < maxX-1 {
				if board[y][x+1] == 0 {
					numDead += 1
				} else {
					numLive += 1
				}
			}
			// RIGHT-BOTTOM
			if x < maxX-1 && y < maxY-1 {
				if board[y+1][x+1] == 0 {
					numDead += 1
				} else {
					numLive += 1
				}
			}
			// BOTTOM
			if y < maxY-1 {
				if board[y+1][x] == 0 {
					numDead += 1
				} else {
					numLive += 1
				}
			}
			// BOTTOM-LEFT
			if y < maxY-1 && x > 0 {
				if board[y+1][x-1] == 0 {
					numDead += 1
				} else {
					numLive += 1
				}
			}

			if vx == 0 {
				if numLive == 3 {
					board[y][x] = 1
				}
			} else {
				if numLive < 2 {
					board[y][x] = 0
				} else if 3 >= numLive && numLive >= 2 {
					board[y][x] = 1
				} else {
					board[y][x] = 0
				}
			}

		}
	}

}

// @lc code=end

func main() {
	var board [][]int
	board = [][]int{{1, 1}, {1, 0}}
	gameOfLife(board)

	fmt.Println(board)

}

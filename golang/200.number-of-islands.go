package main

import "fmt"

/*
 * @lc app=leetcode id=200 lang=golang
 *
 * [200] Number of Islands
 */

// @lc code=start
const (
	ONE  = 49
	ZERO = 48
)

func findOneValue(grid [][]byte) (bool, int, int) {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] != ZERO {
				return true, i, j
			}
		}
	}

	return false, -1, -1
}

func fillIsLands(grid *[][]byte, i int, j int) {
	(*grid)[i][j] = ZERO

	if i > 0 {
		if (*grid)[i-1][j] != ZERO {
			fillIsLands(grid, i-1, j)
		}
	}

	if j > 0 {
		if (*grid)[i][j-1] != ZERO {
			fillIsLands(grid, i, j-1)
		}
	}

	if i < len((*grid))-1 {
		if (*grid)[i+1][j] != ZERO {
			fillIsLands(grid, i+1, j)
		}
	}

	if j < len((*grid)[0])-1 {
		if (*grid)[i][j+1] != ZERO {
			fillIsLands(grid, i, j+1)
		}
	}
}

func numIslands(grid [][]byte) int {
	// fmt.Println(grid)
	isLandCounter := 0
	for true {
		hasLand, i, j := findOneValue(grid)

		if hasLand == false {
			break
		}

		fillIsLands(&grid, i, j)

		isLandCounter++
	}

	// fmt.Println(grid)

	return isLandCounter
}

// @lc code=end

func main() {
	grid := [][]byte{
		[]byte{1, 1, 0, 0, 0},
		[]byte{1, 1, 0, 0, 0},
		[]byte{0, 0, 1, 0, 0},
		[]byte{0, 0, 0, 1, 1},
	}

	fmt.Println(numIslands(grid))
}

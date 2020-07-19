package main

import (
	"fmt"
	"math"
)

/*
 * @lc app=leetcode id=204 lang=golang
 *
 * [204] Count Primes
 */

// @lc code=start

func isPrime(val int) bool {
	if val < 2 {
		return false
	}

	if val == 2 || val == 3 {
		return true
	}

	for i := 2; i <= int(math.Pow(float64(val), 1.0/2)); i++ {
		if val%i == 0 {
			return false
		}
	}

	return true
}
func countPrimes(n int) int {
	counter := 0

	if n < 100000 {
		for i := 1; i < n; i++ {
			if isPrime(i) {
				counter++
			}
		}

	} else {
		counter += 9592

		for i := 100000; i < n; i++ {
			if isPrime(i) {
				counter++
			}
		}
	}

	return counter
}

// @lc code=end

func main() {
	fmt.Println(countPrimes(499979))
}

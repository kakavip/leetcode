/*
 * @lc app=leetcode id=155 lang=golang
 *
 * [155] Min Stack
 */
package main

// @lc code=start
type MinStack struct {
	bucket []int

	minIdxList []int
	minBucket  []int
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	this.bucket = append(this.bucket, val)
	if len(this.minBucket) == 0 || this.minBucket[len(this.minBucket)-1] > val {
		this.minBucket = append(this.minBucket, val)
		this.minIdxList = append(this.minIdxList, len(this.bucket)-1)
	}
}

func (this *MinStack) Pop() {
	if this.minIdxList[len(this.minIdxList)-1] == len(this.bucket)-1 {
		this.minIdxList = this.minIdxList[:len(this.minIdxList)-1]
		this.minBucket = this.minBucket[:len(this.minBucket)-1]
	}
	this.bucket = this.bucket[:len(this.bucket)-1]
}

func (this *MinStack) Top() int {
	return this.bucket[len(this.bucket)-1]
}

func (this *MinStack) GetMin() int {
	return this.minBucket[len(this.minBucket)-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
// @lc code=end

func main() {

}

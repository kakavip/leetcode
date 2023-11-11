/*
 * @lc app=leetcode id=127 lang=golang
 *
 * [127] Word Ladder
 */

package main

import (
	"fmt"
	"math"
	"slices"
)

// @lc code=start

var debug bool = false

type Node struct {
	val   string
	nexts []*Node
	coef  int
}

func NewNode(val string) *Node {
	return &Node{
		val:  val,
		coef: math.MaxInt,
	}
}

func standardrizeNodes(bNode *Node, endWord string) {
	coef := 0
	bNode.coef = coef

	coef += 1
	nNodes := []*Node{bNode}
	for {
		hasEnd := false

		iNodes := []*Node{}
		for i := 0; i < len(nNodes); i++ {
			for j := 0; j < len(nNodes[i].nexts); j++ {
				if nNodes[i].nexts[j].coef > coef {
					n := nNodes[i].nexts[j]
					n.coef = coef
					nNodes[i].nexts[j] = n

					iNodes = append(iNodes, nNodes[i].nexts[j])

					if nNodes[i].nexts[j].val == endWord {
						hasEnd = true
					}
				}
			}
		}

		if len(iNodes) == 0 || hasEnd {
			break
		}

		nNodes = iNodes
		coef += 1
	}

	if debug {
		fmt.Println("MAX LAYERS", coef)
	}

}

func combineLadders(bNode *Node, r [][]string) [][]string {
	result := [][]string{}

	nR := [][]string{}
	if len(r) == 0 {
		nR = append(nR, []string{bNode.val})
	} else {
		for i := 0; i < len(r); i++ {
			nR = append(nR, append(append([]string{}, r[i]...), bNode.val))
		}
	}

	if len(bNode.nexts) > 0 {
		for i := 0; i < len(bNode.nexts); i++ {
			result = append(result, combineLadders(bNode.nexts[i], nR)...)
		}
	} else {
		// fmt.Println(nR)
		result = append(result, nR...)
	}
	return result
}

func ladderLength(beginWord string, endWord string, wordList []string) int {

	if !slices.Contains(wordList, endWord) {
		return 0
	}

	var nodeMap map[string]*Node = make(map[string]*Node)
	nodeMap[beginWord] = NewNode(beginWord)

	if !slices.Contains(wordList, beginWord) {
		wordList = append(wordList, beginWord)
	}
	for i := 0; i < len(wordList)-1; i++ {
		for j := i + 1; j < len(wordList); j++ {
			if compareLadders(wordList[j], wordList[i]) {
				if _, ok := nodeMap[wordList[i]]; !ok {
					nodeMap[wordList[i]] = NewNode(wordList[i])
				}

				if _, ok := nodeMap[wordList[j]]; !ok {
					nodeMap[wordList[j]] = NewNode(wordList[j])
				}

				iNode := nodeMap[wordList[i]]
				jNode := nodeMap[wordList[j]]

				iNode.nexts = append(nodeMap[wordList[i]].nexts, jNode)
				nodeMap[wordList[i]] = iNode

				jNode.nexts = append(nodeMap[wordList[j]].nexts, iNode)
				nodeMap[wordList[j]] = jNode
			}
		}
	}

	standardrizeNodes(nodeMap[beginWord], endWord)

	if n, ok := nodeMap[endWord]; !ok {
		return 0
	} else {
		if n.coef == math.MaxInt {
			return 0
		}
		return n.coef + 1
	}
}

func compareLadders(w1, w2 string) bool {
	nw1 := w1 + "a"
	nw2 := w2 + "a"

	c := 0
	for i := 0; i < len(nw1); i++ {
		if nw1[i] == nw2[i] {
			c += 1
		}
	}

	return c+1 == len(nw1)
}

// @lc code=end

func main() {
	fmt.Println(ladderLength("hit", "cog", []string{"hot", "dot", "dog", "lot", "log", "cog"}))
	fmt.Println(ladderLength("hot", "dog", []string{"hot", "dog"}))
	fmt.Println(ladderLength("hit", "cog", []string{"hot", "dot", "tog", "cog"}))
	fmt.Println(ladderLength("hog", "cog", []string{"cog"}))
}

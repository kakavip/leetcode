#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
from typing import List


class Trie:
    stack: List[str] = []

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.stack.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        return list(filter(lambda x: x == word, self.stack)) != []

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(self.stack) < 1:
            return False

        return list(filter(lambda x: x.startswith(prefix), self.stack)) != []


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end


if __name__ == "__main__":
    pass

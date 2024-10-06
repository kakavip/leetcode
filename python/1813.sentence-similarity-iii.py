#
# @lc app=leetcode id=1813 lang=python3
#
# [1813] Sentence Similarity III
#


# @lc code=start
from collections import deque


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = deque(sentence1.split())
        b = deque(sentence2.split())
        while a and b and a[0] == b[0]:
            a.popleft()
            b.popleft()

        while a and b and a[-1] == b[-1]:
            a.pop()
            b.pop()

        return not a or not b


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(
        s.areSentencesSimilar(sentence1="My name is Haley", sentence2="My Haley")
        == True
    )
    print(s.areSentencesSimilar(sentence1="of", sentence2="A lot of words") == False)
    print(
        s.areSentencesSimilar(sentence1="Eating right now", sentence2="Eating") == True
    )

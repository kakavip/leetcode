#
# @lc app=leetcode id=2976 lang=python3
#
# [2976] Minimum Cost to Convert String I
#

from typing import List


# @lc code=start
class Solution:
    _inf: int = float("inf")
    _v: int = 26

    def floydWarshall(self, graph):
        # dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
        dist = graph

        for k in range(self._v):
            # pick all vertices as source one by one
            for i in range(self._v):
                # Pick all vertices as destination for the
                # above picked source
                for j in range(self._v):
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    @staticmethod
    def get_index(c: str) -> int:
        return ord(c) - 97

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        graph = []
        for _ in range(26):
            graph.append([self._inf] * 26)

        for i in range(26):
            graph[i][i] = 0

        for i in range(len(original)):
            old = graph[self.get_index(original[i])][self.get_index(changed[i])]

            graph[self.get_index(original[i])][self.get_index(changed[i])] = min(
                cost[i], old
            )

        self.floydWarshall(graph)

        # print(graph)

        min_cost: int = 0
        for idx in range(len(source)):
            c = graph[self.get_index(source[idx])][self.get_index(target[idx])]
            if c == self._inf:
                return -1

            min_cost += c

        return min_cost


# @lc code=end
if __name__ == "__main__":
    test_cases = [
        [
            "abcd",
            "acbe",
            ["a", "b", "c", "c", "e", "d"],
            ["b", "c", "b", "e", "b", "e"],
            [2, 5, 5, 1, 2, 20],
            28,
        ],
        ["aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2], 12],
        ["abcd", "abce", ["a"], ["e"], [1000], -1],
    ]

    s = Solution()

    for idx, tc in enumerate(test_cases):
        # s.minimumCost(*tc[: len(tc) - 1])

        assert s.minimumCost(*tc[: len(tc) - 1]) == tc[-1], "Test {}".format(idx + 1)

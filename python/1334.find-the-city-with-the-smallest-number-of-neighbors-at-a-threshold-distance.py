#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#

from typing import Any, List, Optional, Tuple


# @lc code=start

is_debug: bool = False


class Solution:
    _inf = 10001
    _v = 0

    def floydWarshall(self, graph) -> List[List[int]]:
        dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

        for k in range(self._v):
            # pick all vertices as source one by one
            for i in range(self._v):
                # Pick all vertices as destination for the
                # above picked source
                for j in range(self._v):
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        self._v = n

        graph = []
        for _ in range(n):
            graph.append([self._inf] * n)

        for i in range(n):
            graph[i][i] = 0

        for e in edges:
            graph[e[0]][e[1]] = e[2]
            graph[e[1]][e[0]] = e[2]

        max_node_counter: float = float("inf")
        result: float = -1
        n_gragh = self.floydWarshall(graph)
        for idx, path in enumerate(n_gragh):
            counter = 0
            for v in path:
                if v <= distanceThreshold:
                    counter += 1

            if counter <= max_node_counter:
                result = idx
                max_node_counter = counter

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    is_debug = True

    assert (
        s.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) == 3
    ), "Test 1"

    # print(s.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))

    assert (
        s.findTheCity(
            5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2
        )
        == 0
    ), "Test 2"

    assert (
        s.findTheCity(
            6, [[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]], 417
        )
        == 5
    ), "Test 3"

    # is_debug = True
    assert (
        s.findTheCity(
            6, [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]], 20
        )
        == 5
    ), "Test 4"

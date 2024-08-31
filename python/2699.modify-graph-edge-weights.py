#
# @lc app=leetcode id=2699 lang=python3
#
# [2699] Modify Graph Edge Weights
#

# @lc code=start
import heapq
from typing import Dict, List


# def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
#     n = len(graph)

#     distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 # if distance[i][j] in [-1, float("inf")]:
#                 # distance[i][j] = 1
#                 # if graph[i][j] in [-1, float("inf")]:
#                 distance[i][j] = min(
#                     abs(distance[i][j]), abs(distance[i][k]) + abs(distance[k][j])
#                 )
#     return distance

MAX = 2 * 10**9


def dijkstra(adj_list, src, dst) -> int:
    distances = {node: MAX for node in adj_list}
    distances[src] = 0

    # Priority queue to track nodes and current shortest distance
    priority_queue = [(0, src)]

    while priority_queue:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if a shorter distance to current_node is already found
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors and update distances if a shorter path is found
        for neighbor, weight in adj_list[current_node].items():
            distance = current_distance + weight

            # If shorter path to neighbor is found, update distance and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[dst]


class Solution:
    _max: int = MAX

    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        refine_map: Dict[int, Dict[int, int]] = {}
        for i in range(n):
            refine_map[i] = {}

        for edge in edges:
            # original_graph[edge[0]][edge[1]] = edge[2]
            # graph[edge[0]][edge[1]] = max(1, edge[2])

            # original_graph[edge[1]][edge[0]] = edge[2]
            # graph[edge[1]][edge[0]] = max(1, edge[2])

            if edge[2] == -1:
                continue

            # if edge[0] not in refine_map:
            #     refine_map[edge[0]] = {}
            # if edge[1] not in refine_map:
            #     refine_map[edge[1]] = {}

            refine_map[edge[0]][edge[1]] = edge[2]
            refine_map[edge[1]][edge[0]] = edge[2]

        current_dis = dijkstra(refine_map, source, destination)
        if current_dis < target:
            return []

        if current_dis == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = self._max

            return edges

        for idx, edge in enumerate(edges):
            if edge[2] != -1:
                continue

            edge[2] = 1
            refine_map[edge[0]][edge[1]] = 1
            refine_map[edge[1]][edge[0]] = 1

            new_dis = dijkstra(refine_map, source, destination)

            if new_dis <= target:
                edge[2] += target - new_dis

                for j in range(idx + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = self._max

                return edges

        return []

    # def modifiedGraphEdges(
    #     self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    # ) -> List[List[int]]:
    #     original_graph: List[List[int]] = [[self._max] * n for _ in range(n)]
    #     original_graph_2: List[List[int]] = [[self._max] * n for _ in range(n)]
    #     # graph: List[List[int]] = [[self._max] * n for _ in range(n)]
    #     for i in range(n):
    #         original_graph[i][i] = 0
    #         original_graph_2[i][i] = 0

    #     refine_map: Dict[int, Dict[int, int]] = {}
    #     for edge in edges:
    #         original_graph_2[edge[0]][edge[1]] = edge[2]
    #         original_graph_2[edge[1]][edge[0]] = edge[2]

    #         if edge[2] != -1:
    #             original_graph[edge[1]][edge[0]] = edge[2]
    #             original_graph[edge[0]][edge[1]] = edge[2]

    #         if edge[0] not in refine_map:
    #             refine_map[edge[0]] = {}
    #         if edge[1] not in refine_map:
    #             refine_map[edge[1]] = {}

    #         refine_map[edge[0]][edge[1]] = edge[2]
    #         refine_map[edge[1]][edge[0]] = edge[2]

    #     shortest_graph: List[List[int]] = floyd_warshall(original_graph)
    #     shortest_dis: int = shortest_graph[source][destination]
    #     if shortest_dis != self._max and shortest_dis < target:
    #         return []

    #     old_shortest_graph = shortest_graph
    #     shortest_graph: List[List[int]] = floyd_warshall(original_graph_2)
    #     shortest_dis: int = shortest_graph[source][destination]

    #     if shortest_dis > target:
    #         return []

    #     if shortest_dis < target:
    #         # reverse check node
    #         def trace_path(node: int, s_dis: int, t: int, const_t: int) -> bool:
    #             # result: bool = False

    #             for n_node in refine_map[node]:
    #                 dis: int = refine_map[node][n_node]

    #                 n_shortest_dis: int = shortest_graph[destination][n_node]
    #                 if n_shortest_dis + abs(dis) == s_dis:
    #                     if dis == -1:
    #                         n_node_val = t - (s_dis - 1)
    #                         shortest_graph[node][n_node] = n_node_val
    #                         shortest_graph[n_node][node] = n_node_val

    #                         return (
    #                             trace_path(
    #                                 n_node,
    #                                 s_dis - 1,
    #                                 max(
    #                                     t - old_shortest_graph[node][n_node],
    #                                     t - n_node_val,
    #                                     const_t - old_shortest_graph[source][n_node],
    #                                 ),
    #                                 const_t,
    #                             )
    #                             or True
    #                         )
    #                         # if n_node_val > old_shortest_graph[node][n_node]:

    #                         # return True
    #                     elif trace_path(n_node, s_dis - dis, t - dis, const_t):
    #                         return True

    #             return False

    #         if not trace_path(source, shortest_dis, target, target):
    #             return []

    #     for edge in edges:
    #         if edge[2] == -1:
    #             edge[2] = shortest_graph[edge[0]][edge[1]]

    #     return edges


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # s.modifiedGraphEdges(4, [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]], 0, 2, 6)
    # print(
    #     s.modifiedGraphEdges(
    #         n=4,
    #         edges=[[0, 1, -1], [1, 2, -1], [3, 1, -1], [3, 0, 2], [0, 2, 5]],
    #         source=2,
    #         destination=3,
    #         target=8,
    #     )
    #     == []
    # )
    # print(
    #     s.modifiedGraphEdges(
    #         n=5,
    #         edges=[[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]],
    #         source=0,
    #         destination=1,
    #         target=5,
    #     )
    #     == [[4, 1, 1], [2, 0, 1], [0, 3, 3], [4, 3, 1]]
    # )
    # print(
    #     s.modifiedGraphEdges(
    #         n=3, edges=[[0, 1, -1], [0, 2, 5]], source=0, destination=2, target=6
    #     )
    #     == []
    # )
    # # print(
    # #     s.modifiedGraphEdges(4, [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]], 0, 2, 6)
    # # )

    # print(
    #     s.modifiedGraphEdges(
    #         n=5,
    #         edges=[
    #             [1, 3, 10],
    #             [4, 2, -1],
    #             [0, 3, 7],
    #             [4, 0, 7],
    #             [3, 2, -1],
    #             [1, 4, 5],
    #             [2, 0, 8],
    #             [1, 0, 3],
    #             [1, 2, 5],
    #         ],
    #         source=3,
    #         destination=4,
    #         target=11,
    #     )
    #     == [
    #         [1, 3, 10],
    #         [4, 2, 1],
    #         [0, 3, 7],
    #         [4, 0, 7],
    #         [3, 2, 10],
    #         [1, 4, 5],
    #         [2, 0, 8],
    #         [1, 0, 3],
    #         [1, 2, 5],
    #     ]
    # )

    # print(
    #     s.modifiedGraphEdges(
    #         5,
    #         [[1, 4, 1], [2, 4, -1], [3, 0, 2], [0, 4, -1], [1, 3, 10], [1, 0, 10]],
    #         0,
    #         2,
    #         15,
    #     )
    #     == [[1, 4, 1], [2, 4, 4], [3, 0, 2], [0, 4, 14], [1, 3, 10], [1, 0, 10]]
    # )

    # print(
    #     s.modifiedGraphEdges(
    #         5,
    #         [[1, 4, -1], [0, 2, -1], [0, 3, 9], [4, 0, -1], [1, 0, 10], [4, 2, 10]],
    #         1,
    #         2,
    #         9,
    #     )
    #     == [[1, 4, 7], [0, 2, 1], [0, 3, 9], [4, 0, 1], [1, 0, 10], [4, 2, 10]]
    # )

    # print(
    #     s.modifiedGraphEdges(
    #         4, [[3, 0, -1], [1, 2, -1], [2, 3, -1], [1, 3, 9], [2, 0, 5]], 0, 1, 7
    #     )
    #     == [[3, 0, 5], [1, 2, 2], [2, 3, 1], [1, 3, 9], [2, 0, 5]]
    # )

    # print(s.modifiedGraphEdges(4, [[0, 1, 1], [1, 2, 2], [2, 3, 3]], 0, 2, 1) == [])
    print(
        s.modifiedGraphEdges(
            5, [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]], 0, 1, 5
        )
    )
    print(
        s.modifiedGraphEdges(
            100,
            [
                [0, 1, 10000000],
                [1, 2, 10000000],
                [2, 3, 10000000],
                [3, 4, 10000000],
                [4, 5, 10000000],
                [5, 6, 10000000],
                [6, 7, 10000000],
                [7, 8, 10000000],
                [8, 9, 10000000],
                [9, 10, 10000000],
                [10, 11, 10000000],
                [11, 12, 10000000],
                [12, 13, 10000000],
                [13, 14, 10000000],
                [14, 15, 10000000],
                [15, 16, 10000000],
                [16, 17, 10000000],
                [17, 18, 10000000],
                [18, 19, 10000000],
                [19, 20, 10000000],
                [20, 21, 10000000],
                [21, 22, 10000000],
                [22, 23, 10000000],
                [23, 24, 10000000],
                [24, 25, 10000000],
                [25, 26, 10000000],
                [26, 27, 10000000],
                [27, 28, 10000000],
                [28, 29, 10000000],
                [29, 30, 10000000],
                [30, 31, 10000000],
                [31, 32, 10000000],
                [32, 33, 10000000],
                [33, 34, 10000000],
                [34, 35, 10000000],
                [35, 36, 10000000],
                [36, 37, 10000000],
                [37, 38, 10000000],
                [38, 39, 10000000],
                [39, 40, 10000000],
                [40, 41, 10000000],
                [41, 42, 10000000],
                [42, 43, 10000000],
                [43, 44, 10000000],
                [44, 45, 10000000],
                [45, 46, 10000000],
                [46, 47, 10000000],
                [47, 48, 10000000],
                [48, 49, 10000000],
                [49, 50, 10000000],
                [50, 51, 10000000],
                [51, 52, 10000000],
                [52, 53, 10000000],
                [53, 54, 10000000],
                [54, 55, 10000000],
                [55, 56, 10000000],
                [56, 57, 10000000],
                [57, 58, 10000000],
                [58, 59, 10000000],
                [59, 60, 10000000],
                [60, 61, 10000000],
                [61, 62, 10000000],
                [62, 63, 10000000],
                [63, 64, 10000000],
                [64, 65, 10000000],
                [65, 66, 10000000],
                [66, 67, 10000000],
                [67, 68, 10000000],
                [68, 69, 10000000],
                [69, 70, 10000000],
                [70, 71, 10000000],
                [71, 72, 10000000],
                [72, 73, 10000000],
                [73, 74, 10000000],
                [74, 75, 10000000],
                [75, 76, 10000000],
                [76, 77, 10000000],
                [77, 78, 10000000],
                [78, 79, 10000000],
                [79, 80, 10000000],
                [80, 81, 10000000],
                [81, 82, 10000000],
                [82, 83, 10000000],
                [83, 84, 10000000],
                [84, 85, 10000000],
                [85, 86, 10000000],
                [86, 87, 10000000],
                [87, 88, 10000000],
                [88, 89, 10000000],
                [89, 90, 10000000],
                [90, 91, 10000000],
                [91, 92, 10000000],
                [92, 93, 10000000],
                [93, 94, 10000000],
                [94, 95, 10000000],
                [95, 96, 10000000],
                [96, 97, 10000000],
                [97, 98, 10000000],
                [98, 99, 10000000],
                [0, 99, -1],
            ],
            0,
            99,
            990000000,
        )
        == [
            [0, 1, 10000000],
            [1, 2, 10000000],
            [2, 3, 10000000],
            [3, 4, 10000000],
            [4, 5, 10000000],
            [5, 6, 10000000],
            [6, 7, 10000000],
            [7, 8, 10000000],
            [8, 9, 10000000],
            [9, 10, 10000000],
            [10, 11, 10000000],
            [11, 12, 10000000],
            [12, 13, 10000000],
            [13, 14, 10000000],
            [14, 15, 10000000],
            [15, 16, 10000000],
            [16, 17, 10000000],
            [17, 18, 10000000],
            [18, 19, 10000000],
            [19, 20, 10000000],
            [20, 21, 10000000],
            [21, 22, 10000000],
            [22, 23, 10000000],
            [23, 24, 10000000],
            [24, 25, 10000000],
            [25, 26, 10000000],
            [26, 27, 10000000],
            [27, 28, 10000000],
            [28, 29, 10000000],
            [29, 30, 10000000],
            [30, 31, 10000000],
            [31, 32, 10000000],
            [32, 33, 10000000],
            [33, 34, 10000000],
            [34, 35, 10000000],
            [35, 36, 10000000],
            [36, 37, 10000000],
            [37, 38, 10000000],
            [38, 39, 10000000],
            [39, 40, 10000000],
            [40, 41, 10000000],
            [41, 42, 10000000],
            [42, 43, 10000000],
            [43, 44, 10000000],
            [44, 45, 10000000],
            [45, 46, 10000000],
            [46, 47, 10000000],
            [47, 48, 10000000],
            [48, 49, 10000000],
            [49, 50, 10000000],
            [50, 51, 10000000],
            [51, 52, 10000000],
            [52, 53, 10000000],
            [53, 54, 10000000],
            [54, 55, 10000000],
            [55, 56, 10000000],
            [56, 57, 10000000],
            [57, 58, 10000000],
            [58, 59, 10000000],
            [59, 60, 10000000],
            [60, 61, 10000000],
            [61, 62, 10000000],
            [62, 63, 10000000],
            [63, 64, 10000000],
            [64, 65, 10000000],
            [65, 66, 10000000],
            [66, 67, 10000000],
            [67, 68, 10000000],
            [68, 69, 10000000],
            [69, 70, 10000000],
            [70, 71, 10000000],
            [71, 72, 10000000],
            [72, 73, 10000000],
            [73, 74, 10000000],
            [74, 75, 10000000],
            [75, 76, 10000000],
            [76, 77, 10000000],
            [77, 78, 10000000],
            [78, 79, 10000000],
            [79, 80, 10000000],
            [80, 81, 10000000],
            [81, 82, 10000000],
            [82, 83, 10000000],
            [83, 84, 10000000],
            [84, 85, 10000000],
            [85, 86, 10000000],
            [86, 87, 10000000],
            [87, 88, 10000000],
            [88, 89, 10000000],
            [89, 90, 10000000],
            [90, 91, 10000000],
            [91, 92, 10000000],
            [92, 93, 10000000],
            [93, 94, 10000000],
            [94, 95, 10000000],
            [95, 96, 10000000],
            [96, 97, 10000000],
            [97, 98, 10000000],
            [98, 99, 10000000],
            [0, 99, 990000000],
        ]
    )

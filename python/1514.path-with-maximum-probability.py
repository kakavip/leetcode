#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from typing import Dict, List

import heapq


def dijkstra(adj_list, start):
    distances = {node: float("inf") for node in adj_list}
    distances[start] = -1

    # Priority queue to track nodes and current shortest distance
    priority_queue = [(-1, start)]

    while priority_queue:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if a shorter distance to current_node is already found
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors and update distances if a shorter path is found
        for neighbor, weight in adj_list[current_node].items():
            distance = (current_distance or -1) * weight

            # If shorter path to neighbor is found, update distance and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        refine_node: Dict[int, Dict[int, float]] = {}
        for idx, edge in enumerate(edges):
            if edge[0] not in refine_node:
                refine_node[edge[0]] = {}

            if edge[1] not in refine_node:
                refine_node[edge[1]] = {}

            refine_node[edge[0]].update({edge[1]: succProb[idx]})
            refine_node[edge[1]].update({edge[0]: succProb[idx]})

        # print(refine_node)
        if start_node not in refine_node or end_node not in refine_node:
            return 0.0

        distance_map = dijkstra(refine_node, start_node)

        # distance_map: Dict[int, float] = {start_node: 1.0}

        # def solve(start: int):
        #     cur_succ: float = distance_map[start]
        #     n_node_data = refine_node[start]
        #     for n_node, succ_prob in n_node_data.items():
        #         new_succ_val: int = cur_succ * succ_prob
        #         if n_node not in distance_map:
        #             distance_map[n_node] = new_succ_val
        #             # solve(n_node)
        #         else:
        #             if distance_map[n_node] < new_succ_val:
        #                 distance_map[n_node] = new_succ_val

        #                 # solve(n_node)

        # solve(start_node)
        # print(distance_map)

        result: float = distance_map.get(end_node)
        if result == float("inf"):
            result = 0.0

        return -round(result, 5)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2) == 0.25)
    print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2) == 0.3)
    print(s.maxProbability(3, [[0, 1]], [0.5], 0, 2) == 0.0)
    print(
        s.maxProbability(
            10, [[0, 3], [1, 7], [1, 2], [0, 9]], [0.31, 0.9, 0.86, 0.36], 2, 3
        )
        == 0.0
    )
    print(
        s.maxProbability(
            500, [[193, 229], [133, 212], [224, 465]], [0.91, 0.78, 0.64], 4, 364
        )
        == 0.0
    )

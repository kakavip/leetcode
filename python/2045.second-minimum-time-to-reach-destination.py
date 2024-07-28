#
# @lc app=leetcode id=2045 lang=python3
#
# [2045] Second Minimum Time to Reach Destination
#

from typing import List, Tuple

# @lc code=start


# Implementing Dijkstra's Algorithm in Python
import heapq


def edge_list_to_adjacency_list(edge_list):
    adj_list = {}
    for src, dest, weight in edge_list:
        if src not in adj_list:
            adj_list[src] = {}
        if dest not in adj_list:
            adj_list[dest] = {}

        adj_list[src][dest] = weight
        adj_list[dest][src] = weight

    return adj_list


class Solution:
    n: int = -1
    change: int = -1

    def dijkstra(self, adj_list, start):
        distances = {node: [float("inf")] for node in adj_list}
        distances[start] = [0]

        # Priority queue to track nodes and current shortest distance
        priority_queue = [(0, start)]

        while priority_queue:
            # Pop the node with the smallest distance from the priority queue

            current_distance, current_node = heapq.heappop(priority_queue)

            # Skip if a shorter distance to current_node is already found
            if current_distance > distances[current_node][-1]:
                continue

            # Explore neighbors and update distances if a shorter path is found
            for neighbor, weight in adj_list[current_node].items():
                if (current_distance // self.change) % 2 == 1:
                    current_distance = (
                        (current_distance // self.change) + 1
                    ) * self.change

                distance = current_distance + weight

                # If shorter path to neighbor is found, update distance and push to queue
                if (
                    len(distances[neighbor]) >= 2 and distance > distances[neighbor][-1]
                ) or distance in distances[neighbor]:
                    continue

                if distance < distances[neighbor][0]:
                    distances[neighbor] = [distance, distances[neighbor][0]]
                else:
                    distances[neighbor] = [distances[neighbor][0], distance]

                heapq.heappush(priority_queue, (distance, neighbor))

                # print(priority_queue)

        return distances

    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        self.n = n
        self.change = change
        # self.n_distances = []

        edge_list: List[List[int]] = list(map(lambda x: x.copy() + [time], edges))

        adj_list = edge_list_to_adjacency_list(edge_list)
        # print(adj_list)

        distances = self.dijkstra(adj_list, 1)
        print(distances)
        # print(self.n_distances)

        return distances[n][-1]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert (
        s.secondMinimum(5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5) == 13
    ), "Test 1"
    # assert s.secondMinimum(2, [[1, 2]], 3, 2) == 11, "Test 2"

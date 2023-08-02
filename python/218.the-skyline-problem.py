#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
from typing import List, Tuple
from time import time
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # (x0, h0, "start" | "end")
        x_sky_points: List[Tuple[int, int, str]] = []
        for block in buildings:
            x_sky_points.append((block[0], block[-1], "start"))
            x_sky_points.append((block[1], -block[-1], "end"))

        x_sky_points.sort(key=lambda x: (x[0], -x[1]))

        skyline: List[List[int]] = []
        heap = [0]  # init heap with zero item

        for x, h, flag in x_sky_points:
            if flag == "start":
                if h > -heap[0]:
                    skyline.append([x, h])
                heapq.heappush(heap, -h)
            else:
                heap.remove(h)
                heapq.heapify(heap)

                if -h > -heap[0]:
                    skyline.append([x, -heap[0]])
        return skyline


# @lc code=end

import ast


if __name__ == "__main__":
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    # buildings = [[0, 2, 3], [2, 5, 3]]
    # buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
    # buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]]
    # buildings = [
    #     [1, 38, 219],
    #     [2, 19, 228],
    #     [2, 64, 106],
    #     [3, 80, 65],
    #     [3, 84, 8],
    #     [4, 12, 8],
    #     [4, 25, 14],
    #     [4, 46, 225],
    #     [4, 67, 187],
    #     [5, 36, 118],
    #     [5, 48, 211],
    #     [5, 55, 97],
    #     [6, 42, 92],
    #     [6, 56, 188],
    #     [7, 37, 42],
    #     [7, 49, 78],
    #     [7, 84, 163],
    #     [8, 44, 212],
    #     [9, 42, 125],
    #     [9, 85, 200],
    #     [9, 100, 74],
    #     [10, 13, 58],
    #     [11, 30, 179],
    #     [12, 32, 215],
    #     [12, 33, 161],
    #     [12, 61, 198],
    #     [13, 38, 48],
    #     [13, 65, 222],
    #     [14, 22, 1],
    #     [15, 70, 222],
    #     [16, 19, 196],
    #     [16, 24, 142],
    #     [16, 25, 176],
    #     [16, 57, 114],
    #     [18, 45, 1],
    #     [19, 79, 149],
    #     [20, 33, 53],
    #     [21, 29, 41],
    #     [23, 77, 43],
    #     [24, 41, 75],
    #     [24, 94, 20],
    #     [27, 63, 2],
    #     [31, 69, 58],
    #     [31, 88, 123],
    #     [31, 88, 146],
    #     [33, 61, 27],
    #     [35, 62, 190],
    #     [35, 81, 116],
    #     [37, 97, 81],
    #     [38, 78, 99],
    #     [39, 51, 125],
    #     [39, 98, 144],
    #     [40, 95, 4],
    #     [45, 89, 229],
    #     [47, 49, 10],
    #     [47, 99, 152],
    #     [48, 67, 69],
    #     [48, 72, 1],
    #     [49, 73, 204],
    #     [49, 77, 117],
    #     [50, 61, 174],
    #     [50, 76, 147],
    #     [52, 64, 4],
    #     [52, 89, 84],
    #     [54, 70, 201],
    #     [57, 76, 47],
    #     [58, 61, 215],
    #     [58, 98, 57],
    #     [61, 95, 190],
    #     [66, 71, 34],
    #     [66, 99, 53],
    #     [67, 74, 9],
    #     [68, 97, 175],
    #     [70, 88, 131],
    #     [74, 77, 155],
    #     [74, 99, 145],
    #     [76, 88, 26],
    #     [82, 87, 40],
    #     [83, 84, 132],
    #     [88, 99, 99],
    # ]
    # buildings = [[2,9,10],[9,12,15]]

    stime = time()
    instance: Solution = Solution()
    # instance.getSkyline(buildings)
    print(f"Blocks: {instance.getSkyline(buildings)}")
    etime = time()
    print(f"TAKE TIME: {int(etime - stime)}s")

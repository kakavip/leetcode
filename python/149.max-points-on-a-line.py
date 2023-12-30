#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start

from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

debug = False


@dataclass
class StraightLine:
    points: List[List[int]]
    vector: Tuple[int, int]


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        vector_map: Dict[Tuple[int, int, int, int], Dict[str, Any]] = {}

        for idx1 in range(1, n):
            p1 = points[idx1]

            line_points = set()
            for vec in vector_map:
                v = self.calc_vector(vec[2:], p1)
                if self.compare_vector(v, vec[:2]):
                    vector_map[vec]["counter"] += 1
                    line_points.update(vector_map[vec]["points"])
                    vector_map[vec]["points"].append(tuple(p1))

            for idx2 in range(idx1):
                p2 = points[idx2]

                debug and print(line_points, p2)
                if {tuple(p2)} & line_points:
                    continue

                debug and print("P2: ", p2)

                v = self.calc_vector(p1, p2)
                debug and print("VECTOR: ", v)
                vector_map[(v[0], v[1], p1[0], p1[1])] = {
                    "counter": 2,
                    "points": [tuple(p2), tuple(p1)],
                }

        debug and print(vector_map)
        _max = 0
        for v in vector_map:
            if _max < vector_map[v]["counter"]:
                _max = vector_map[v]["counter"]
        return _max

    @staticmethod
    def calc_vector(p1: List[int], p2: List[int]) -> Tuple[int, int]:
        return (p2[0] - p1[0], p2[1] - p1[1])

    @staticmethod
    def compare_vector(v1: Tuple[int, int], v2: Tuple[int, int]) -> bool:
        # x1 = x0 = 0
        if v1[0] == 0 or v2[0] == 0:
            return v1[0] == v2[0]
        if v1[1] == 0 or v2[1] == 0:
            return v1[1] == v2[1]

        return v2[1] / v1[1] == v2[0] / v1[0]


# @lc code=end
debug = False
if __name__ == "__main__":
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    # points = [[1, 1], [2, 2], [3, 3]]
    # points = [[2, 3], [3, 3], [-5, 3]]
    points = [
        [4, -3],
        [970, 680],
        [-97, -35],
        [3, 8],
        [60, 253],
        [0, -13],
        [-270, -748],
        [-291, -165],
        [270, 890],
        [90, 228],
        [-220, -270],
        [-255, -118],
        [873, 615],
        [-42, -175],
        [440, 345],
        [4, -9],
        [170, 27],
        [425, 114],
        [56, 203],
        [531, 872],
        [295, 480],
        [231, 193],
        [291, 225],
        [680, 201],
        [-10, 9],
        [-388, -230],
        [-385, -127],
        [-590, -990],
        [-7, -40],
        [308, 222],
        [-616, -247],
        [-70, -283],
        [150, 526],
        [77, 113],
        [396, 304],
        [-264, -311],
        [-6, -8],
        [-88, -147],
        [30, 162],
        [49, 176],
        [81, 196],
        [-9, -124],
        [-27, -188],
        [-14, -67],
        [308, 233],
        [413, 676],
        [-77, 33],
        [-177, -304],
        [0, -31],
        [472, 774],
        [462, 313],
        [-35, -148],
        [1, -2],
        [-440, -475],
        [154, 153],
        [485, 355],
        [-231, -47],
        [340, 85],
        [-60, -111],
        [42, 149],
        [-354, -598],
        [388, 290],
        [44, -24],
        [3, -8],
        [510, 143],
        [-308, -352],
        [-18, -156],
        [-21, -94],
        [-63, -316],
        [-118, -206],
        [0, 73],
        [-240, -657],
        [-352, -393],
        [-531, -892],
        [-485, -295],
        [352, 263],
        [616, 393],
        [-154, -7],
        [3, 4],
        [-5, -9],
        [63, 230],
        [385, 273],
        [-679, -425],
        [-595, -234],
        [-582, -360],
        [-176, -229],
        [770, 473],
        [-539, -207],
        [-56, -229],
        [-236, -402],
        [-970, -620],
        [-425, -176],
        [240, 799],
        [118, 186],
        [10, -7],
        [-680, -263],
        [-5, 7],
        [220, 140],
        [-2, 7],
        [-28, -121],
        [-300, -839],
        [-54, -284],
        [-194, -100],
        [-308, -87],
        [-3, -10],
        [-873, -555],
        [-90, -202],
        [-5, -4],
    ]

    s = Solution()
    print(s.maxPoints(points))

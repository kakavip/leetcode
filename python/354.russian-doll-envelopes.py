#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
import bisect
from typing import Dict, List, Tuple


class Solution:
    n: int
    counters: List[int]
    _cache: Dict[Tuple[int, int], bool] = {}

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        h_nums: List[int] = [h for w, h in envelopes]

        # print("H: ", h_nums)
        return self.lis(h_nums)

    def lis(self, nums):
        _max = 0
        dp = [0] + [float("inf")] * len(nums)
        for num in nums:
            i = bisect.bisect_left(dp, num)
            dp[i] = num
            _max = max(_max, i)

            # print(dp)

        return _max


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3)
    # print(s.maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1)
    # print(s.maxEnvelopes([[4, 5], [6, 7], [2, 3]]) == 3)
    print(
        s.maxEnvelopes(
            [[1, 2], [2, 3], [3, 4], [3, 5], [4, 5], [5, 5], [5, 6], [6, 7], [7, 8]]
        )
        == 7
    )
    # print(
    #     s.maxEnvelopes(
    #         [
    #             [936, 357],
    #             [742, 148],
    #             [643, 776],
    #             [612, 34],
    #             [897, 140],
    #             [33, 508],
    #             [160, 35],
    #             [456, 191],
    #             [620, 496],
    #             [220, 898],
    #             [302, 940],
    #             [964, 767],
    #             [721, 327],
    #             [176, 423],
    #             [14, 345],
    #             [182, 616],
    #             [753, 459],
    #             [780, 480],
    #             [488, 103],
    #             [36, 657],
    #             [288, 942],
    #             [807, 831],
    #             [438, 880],
    #             [984, 342],
    #             [738, 780],
    #             [326, 599],
    #             [380, 915],
    #             [106, 299],
    #             [413, 428],
    #             [703, 795],
    #             [155, 362],
    #             [809, 764],
    #             [269, 392],
    #             [393, 379],
    #             [690, 793],
    #             [362, 249],
    #             [229, 519],
    #             [515, 98],
    #             [611, 817],
    #             [460, 925],
    #             [463, 784],
    #             [490, 585],
    #             [120, 987],
    #             [8, 298],
    #             [486, 144],
    #             [655, 407],
    #             [907, 786],
    #             [275, 998],
    #             [241, 565],
    #             [96, 305],
    #             [351, 393],
    #             [65, 971],
    #             [200, 485],
    #             [162, 91],
    #             [150, 423],
    #             [944, 524],
    #             [574, 216],
    #             [949, 729],
    #             [711, 38],
    #             [677, 115],
    #             [228, 779],
    #             [783, 984],
    #             [868, 22],
    #             [463, 743],
    #             [495, 727],
    #             [720, 319],
    #             [900, 470],
    #             [759, 663],
    #             [958, 622],
    #             [231, 798],
    #             [98, 987],
    #             [551, 367],
    #             [789, 689],
    #             [729, 413],
    #             [946, 118],
    #             [863, 84],
    #             [637, 158],
    #             [300, 629],
    #             [958, 53],
    #             [655, 819],
    #             [390, 2],
    #             [298, 764],
    #             [133, 828],
    #             [477, 695],
    #             [667, 690],
    #             [943, 731],
    #             [311, 998],
    #             [412, 366],
    #             [388, 238],
    #             [321, 417],
    #             [309, 12],
    #             [554, 589],
    #             [989, 521],
    #             [73, 752],
    #             [76, 343],
    #             [754, 159],
    #             [206, 600],
    #             [793, 367],
    #             [593, 711],
    #             [475, 976],
    #             [917, 31],
    #             [933, 556],
    #             [228, 343],
    #             [174, 810],
    #             [368, 532],
    #             [552, 397],
    #             [649, 672],
    #             [74, 439],
    #             [917, 259],
    #             [622, 38],
    #             [140, 14],
    #             [660, 497],
    #             [117, 10],
    #             [437, 957],
    #             [791, 487],
    #             [782, 475],
    #             [869, 207],
    #             [258, 375],
    #             [576, 334],
    #             [393, 812],
    #             [759, 38],
    #             [604, 289],
    #             [991, 786],
    #             [597, 125],
    #             [651, 91],
    #             [960, 351],
    #             [788, 379],
    #             [829, 920],
    #             [448, 809],
    #             [404, 88],
    #             [689, 172],
    #             [923, 345],
    #             [139, 452],
    #             [260, 375],
    #             [237, 190],
    #             [266, 921],
    #             [798, 935],
    #             [715, 827],
    #             [87, 309],
    #             [305, 572],
    #             [554, 167],
    #             [33, 642],
    #             [862, 978],
    #             [313, 951],
    #             [583, 346],
    #             [514, 629],
    #             [638, 589],
    #             [684, 430],
    #             [802, 841],
    #             [366, 419],
    #             [9, 866],
    #             [339, 805],
    #             [46, 108],
    #             [914, 674],
    #             [498, 700],
    #             [51, 966],
    #             [446, 632],
    #             [161, 537],
    #             [394, 837],
    #             [83, 549],
    #             [46, 314],
    #             [158, 568],
    #             [743, 118],
    #             [305, 728],
    #             [906, 52],
    #             [497, 81],
    #             [902, 14],
    #             [887, 338],
    #             [328, 204],
    #             [423, 820],
    #             [91, 678],
    #             [817, 584],
    #             [332, 645],
    #             [679, 71],
    #             [142, 722],
    #             [450, 654],
    #             [53, 613],
    #             [41, 654],
    #             [730, 868],
    #             [798, 89],
    #             [155, 532],
    #             [488, 673],
    #             [404, 263],
    #             [1000, 750],
    #             [569, 137],
    #             [417, 866],
    #             [543, 545],
    #             [146, 378],
    #             [417, 721],
    #             [681, 862],
    #             [147, 861],
    #             [935, 554],
    #             [288, 669],
    #             [857, 304],
    #             [638, 787],
    #             [965, 429],
    #             [222, 68],
    #             [577, 970],
    #             [771, 75],
    #             [207, 20],
    #             [77, 609],
    #             [296, 441],
    #             [979, 797],
    #             [573, 345],
    #             [410, 385],
    #             [868, 487],
    #             [382, 836],
    #             [196, 563],
    #             [755, 287],
    #             [346, 316],
    #             [82, 34],
    #             [515, 484],
    #             [703, 300],
    #             [159, 206],
    #             [582, 59],
    #             [20, 683],
    #             [2, 787],
    #             [773, 398],
    #             [960, 870],
    #             [641, 403],
    #             [695, 833],
    #             [331, 851],
    #             [633, 983],
    #             [529, 868],
    #             [41, 93],
    #             [765, 602],
    #             [403, 583],
    #             [871, 359],
    #             [342, 832],
    #             [509, 685],
    #             [289, 626],
    #             [887, 32],
    #             [232, 866],
    #             [863, 419],
    #             [393, 680],
    #             [90, 979],
    #             [555, 290],
    #             [498, 954],
    #             [336, 818],
    #             [953, 939],
    #             [490, 654],
    #             [690, 971],
    #             [964, 4],
    #             [145, 894],
    #             [136, 658],
    #             [448, 371],
    #             [323, 991],
    #             [873, 786],
    #             [718, 337],
    #             [988, 111],
    #             [480, 449],
    #             [891, 544],
    #             [867, 529],
    #             [965, 13],
    #             [712, 686],
    #             [369, 29],
    #             [112, 35],
    #             [391, 662],
    #             [552, 832],
    #             [562, 1],
    #             [490, 906],
    #             [795, 676],
    #             [87, 670],
    #             [423, 994],
    #             [615, 338],
    #             [639, 947],
    #             [118, 927],
    #             [850, 411],
    #             [467, 568],
    #             [844, 205],
    #             [760, 446],
    #             [46, 905],
    #             [28, 855],
    #             [856, 781],
    #             [485, 349],
    #             [92, 217],
    #             [814, 299],
    #             [601, 123],
    #             [622, 4],
    #             [802, 566],
    #             [917, 327],
    #             [569, 882],
    #             [39, 885],
    #             [456, 217],
    #             [372, 882],
    #             [862, 864],
    #             [7, 29],
    #             [855, 562],
    #             [909, 79],
    #             [630, 706],
    #             [519, 63],
    #             [225, 757],
    #             [89, 880],
    #             [179, 623],
    #             [309, 839],
    #             [364, 550],
    #             [253, 73],
    #             [578, 628],
    #             [895, 534],
    #             [606, 607],
    #             [166, 547],
    #             [578, 657],
    #             [695, 841],
    #             [203, 112],
    #             [805, 918],
    #             [61, 877],
    #             [384, 781],
    #             [224, 217],
    #             [142, 10],
    #             [516, 894],
    #             [575, 263],
    #             [379, 968],
    #             [825, 52],
    #             [53, 88],
    #             [19, 169],
    #             [206, 463],
    #             [461, 697],
    #             [308, 196],
    #             [902, 103],
    #             [62, 665],
    #             [397, 369],
    #             [79, 878],
    #             [486, 869],
    #             [633, 847],
    #             [222, 939],
    #             [246, 957],
    #             [461, 609],
    #             [251, 28],
    #             [477, 650],
    #             [650, 262],
    #             [362, 571],
    #             [675, 843],
    #             [39, 972],
    #             [312, 395],
    #             [833, 797],
    #             [167, 397],
    #             [554, 594],
    #             [129, 224],
    #             [808, 135],
    #         ]
    #     )
    #     == 28
    # )
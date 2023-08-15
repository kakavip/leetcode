#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start


from typing import Dict, List, Optional, Tuple


class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        _min: int = min(jug1Capacity, jug2Capacity)
        _max: int = jug1Capacity + jug2Capacity - _min
        _target: int = targetCapacity

        data: Dict[int, List[Tuple[int, int]]] = {0: []}
        # maybe_cap: List[Tuple[int, int]] = []
        next_node: Optional[Tuple[int, int]] = None

        while not next_node or next_node not in data[sum(next_node)]:
            if not next_node:
                next_node = (_min, 0)
                data.update({sum(next_node): []})
                continue

            elif sum(next_node) == _target:
                return True

            # maybe_cap.append(next_node)
            data[sum(next_node)].append(next_node)
            current_node: Tuple[int, int] = next_node

            if current_node[0] > 0:
                if current_node[1] == _max:
                    next_node = (current_node[0], 0)
                else:
                    _sum = sum(current_node)
                    if _sum <= _max:
                        next_node = (0, _sum)
                    else:
                        next_node = (_sum - _max, _max)
            else:
                next_node = (_min, current_node[1])

            # print(f"NEXT NODE: {next_node}")

            _sum = sum(next_node)
            if _sum not in data.keys():
                data.update({_sum: []})

        return False


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.canMeasureWater(104_579, 104_593, 12_444))
    # print(s.canMeasureWater(2, 6, 5))

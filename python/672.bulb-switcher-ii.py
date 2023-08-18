#
# @lc app=leetcode id=672 lang=python3
#
# [672] Bulb Switcher II
#


# @lc code=start
from typing import Any, Dict, List, Tuple

debug = False


def press(a: List[int], buttons: List[int]) -> bool:
    for button in buttons:
        for idx, _ in enumerate(a):
            if button == 1:
                a[idx] = 1 - a[idx]
            if button == 2:
                if (idx + 1) % 2 == 0:
                    a[idx] = 1 - a[idx]
            if button == 3:
                if (idx + 1) % 2 == 1:
                    a[idx] = 1 - a[idx]
            if button == 4:
                if ((idx + 1) - 1) % 3 == 0:
                    a[idx] = 1 - a[idx]
    return a


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1

        init_lights: List[int] = [1] * n

        cache_next_statuses: Dict[Any, List[Any]] = {}
        # NOTE: init lights
        old_statuses: List[Any] = [tuple(init_lights)]
        for _ in range(presses):
            u_statuses: List[Any] = []
            for k_status in old_statuses:
                k_tup_status = k_status

                # k_n_statuses: List[Any] = []
                if k_tup_status not in cache_next_statuses.keys():
                    cache_next_statuses[k_tup_status] = []

                    k_u_statuses: List[Any] = []
                    for j in range(4):
                        _n_stat: List[int] = press(list(k_status), [j + 1])

                        k_u_statuses.append(tuple(_n_stat))

                    cache_next_statuses[k_tup_status] = set(k_u_statuses)

                u_statuses.extend(cache_next_statuses[k_tup_status])

            old_statuses.clear()
            old_statuses.extend(list(set(u_statuses)))

        return len(old_statuses)


# @lc code=end

debug = True
if __name__ == "__main__":
    # a = [1] * 20

    # new_a_1_4 = press(a.copy(), [1, 4])  # NOTE: CASE X
    # new_a_2_4 = press(a.copy(), [2, 4])  # NOTE: CASE Y
    # new_a_3_4 = press(a.copy(), [3, 4])  # NOTE: CASE Z = NOT Y
    # new_a_4_3 = press(a.copy(), [4, 3])
    # new_a_4_2 = press(a.copy(), [4, 2])
    # new_a_4_1 = press(a.copy(), [4, 1])

    # print(f"ORIGIN:\t{a}")
    # print(f"FINAL 1->4:\t{new_a_1_4}")
    # print(f"FINAL 2->4:\t{new_a_2_4}")
    # print(f"FINAL 3->4:\t{new_a_3_4}")
    # # print(f"FINAL 4->3:\t{new_a_4_3}")
    # # print(f"FINAL 4->2:\t{new_a_4_2}")
    # # print(f"FINAL 4->1:\t{new_a_4_1}")
    # # print(f"CHECK X -> (1): {press(new_a_1_4.copy(), [1])}")
    # # print(f"CHECK X -> (2): {press(new_a_1_4.copy(), [2])}")
    # # print(f"CHECK X -> (3): {press(new_a_1_4.copy(), [3])}")
    # # print(f"CHECK X -> (4): {press(new_a_1_4.copy(), [4])}")

    # # print(f"CHECK Y -> (1): {press(new_a_2_4.copy(), [1])}")
    # # print(f"CHECK Y -> (2): {press(new_a_2_4.copy(), [2])}")
    # # print(f"CHECK Y -> (3): {press(new_a_2_4.copy(), [3])}")
    # # print(f"CHECK Y -> (4): {press(new_a_2_4.copy(), [4])}")

    # print(f"CHECK Z -> (1): {press(new_a_3_4.copy(), [1])}")
    # print(f"CHECK Z -> (2): {press(new_a_3_4.copy(), [2])}")
    # print(f"CHECK Z -> (3): {press(new_a_3_4.copy(), [3])}")
    # print(f"CHECK Z -> (4): {press(new_a_3_4.copy(), [4])}")

    s = Solution()
    assert s.flipLights(3, 1) == 4, "Wrong output!!!"
    assert s.flipLights(1, 1) == 2, "Wrong output!!!"
    assert s.flipLights(2, 1) == 3, "Wrong output!!!"
    assert s.flipLights(1, 0) == 1, "Wrong output!!!"
    assert s.flipLights(3, 2) == 7, "Wrong output!!!"

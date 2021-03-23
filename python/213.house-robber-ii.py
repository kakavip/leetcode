#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List

# 0: 0 -> 2 -> 4; 2 -> 5
# 1: 1 -> 3 -> 5; 1 -> 4; 1 -> 3;
# 2: 2 -> 4; 2 -> 5


class Solution:
    @classmethod
    def rob_lookup(cls, nums: List[int], skip_endless: bool = False, cached_max_values: dict = {}) -> int:
        if not nums:
            return 0
        if len(nums) == 1 and skip_endless:
            return 0

        if cached_max_values.get(len(nums)):
            return cached_max_values[len(nums)]

        a: int = nums[0] + \
            cls.rob_lookup(nums[2:], skip_endless, cached_max_values)
        b: int = nums[0] + \
            cls.rob_lookup(nums[3:], skip_endless, cached_max_values)

        max_value: int = max(a, b)
        # if cached_max_values.get(len(nums)) and cached_max_values.get(len(nums)) != max_value:
        #     print(
        #         f"Cached value: {cached_max_values.get(len(nums))}, real value: {max_value}")

        cached_max_values.update({
            len(nums): max_value
        })

        return max_value

    def rob(self, nums: List[int]) -> int:
        num_of_houses: int = len(nums)

        if num_of_houses == 1:
            return nums[0]
        if num_of_houses == 0:
            return 0
        if sum(nums) == 0:
            return 0

        odd_sum: int = self.rob_lookup(nums[1:], False, {})
        even_sum: int = self.rob_lookup(
            nums, True, {})
        three_sum: int = 0
        if len(nums) > 2:
            three_sum = self.rob_lookup(
                nums[2:], False, {}
            )

        # print(f"Sum even: {even_sum}, odd: {odd_sum}, three: {three_sum}")
        return max(even_sum, odd_sum, three_sum)


# @lc code=end
def run_test(instance: Solution):
    assert instance.rob([2, 3, 2]) == 3, "Wrong case 1"
    assert instance.rob([1, 2, 3, 1]) == 4, "Wrong case 2"
    assert instance.rob([0]) == 0, "Wrong case 3"
    assert instance.rob(
        [1, 3, 1, 3, 100]) == 103, f"Wrong case 4: {instance.rob([1, 3, 1, 3, 100])} != 103"
    assert instance.rob([2, 1, 1, 2]) == 3, "Wrong case 5."
    assert instance.rob([2, 4, 8, 9, 9, 3]) == 19, "Wrong case 6"
    assert instance.rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16, "Wrong case 7"
    assert instance.rob([0, 0]) == 0, "Wrong case 8"
    assert instance.rob([6, 6, 4, 8, 4, 3, 3, 10]) == 27, "Wrong case 9"
    assert instance.rob([82, 217, 170, 215, 153, 55, 185, 55, 185, 232, 69, 131, 130, 102]
                        ) == 1082, "Wrong case 10"


def run_debug(instance: Solution):
    r = instance.rob([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                     )
    print(f"Result: {r}")


if __name__ == "__main__":
    instance: Solution = Solution()

    run_debug(instance)
    # run_test(instance)

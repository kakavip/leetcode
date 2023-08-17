#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#


# @lc code=start
debug = False


class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0

        num_op: int = 0
        copy_temp: int = 0
        real_n: int = 1
        while real_n < n:
            # copy
            if not copy_temp:
                copy_temp = real_n
                num_op += 1
                debug and print(
                    f"ACTION: COPY, REAL N: {real_n}, TEMP: {copy_temp}, NUM_OP: {num_op}"
                )
                continue

            if (
                (2 * copy_temp + real_n < 2 * real_n)
                and (2 * copy_temp + real_n < n)
                and (n - real_n) % real_n == 0
            ):
                copy_temp = real_n
                num_op += 1
                debug and print(
                    f"ACTION: COPY, REAL N: {real_n}, TEMP: {copy_temp}, NUM_OP: {num_op}"
                )

            # patse
            real_n += copy_temp
            num_op += 1
            debug and print(
                f"ACTION: PASTE, REAL N: {real_n}, TEMP: {copy_temp}, NUM_OP: {num_op}"
            )

        debug and print(f"NUMBER OPERATIONS: {num_op}")
        return num_op


# @lc code=end

debug = True
if __name__ == "__main__":
    s = Solution()
    assert s.minSteps(3) == 3, f"Wrong output!!!"
    assert s.minSteps(1) == 0, f"Wrong output!!!"
    assert s.minSteps(2) == 2, f"Wrong output!!!"
    assert s.minSteps(9) == 6, f"Wrong output!!!"
    assert s.minSteps(6) == 5, f"Wrong output!!!"
    assert s.minSteps(4) == 4, f"Wrong output!!!"
    assert s.minSteps(7) == 7, f"Wrong output!!!"

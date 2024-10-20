#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#

# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operators: List[str] = []
        stack: List[int] = []  # index open
        _map: Dict[int, List[int]] = {}

        n: int = len(expression)
        for i in range(n):
            if expression[i] in ["!", "|", "&"]:
                operators.append(expression[i])

            if expression[i] == "(":
                stack.append(i)
                _map[i] = []

            if expression[i] == ")":
                r: int = -1
                _sum: int = sum(_map[stack[-1]])
                if operators[-1] == "|":
                    r = min(1, _sum)
                elif operators[-1] == "&":
                    r = int(_sum == len(_map[stack[-1]]))
                elif operators[-1] == "!":
                    r = 1 - _map[stack[-1]][0]

                if stack[-1] == 1:
                    return bool(r)

                _map[stack[-2]].append(r)
                _map[stack[-1]].clear()

                # print(stack, _map)
                stack.pop()
                operators.pop()

            if expression[i] in ["t", "f"]:
                _map[stack[-1]].append(
                    1 if expression[i] == "t" else 0,
                )

        # print(_map)

        return False


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.parseBoolExpr(expression="&(|(f))") == False)
    print(s.parseBoolExpr(expression="|(f,f,f,t)") == True)
    print(s.parseBoolExpr(expression="!(&(f,t))") == True)

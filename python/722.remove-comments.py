#
# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#


# @lc code=start
import re
from typing import List

debug = False


bracket_pattern = r"\/\*.*\*\/"
bracket_regex = re.compile(bracket_pattern)


def remove_cmt_inline2(
    n_line: str, bracket_stack: List[str], check_empty_stack: List[bool]
) -> str:
    in_line: int = ""

    mark_idx: int = 0
    while ("/*" in n_line or "//" in n_line) and not bracket_stack:
        dup_idx: int = (
            -1 if "//" not in n_line[mark_idx:] else n_line[mark_idx:].index("//")
        )
        bracket_idx: int = (
            -1 if "/*" not in n_line[mark_idx:] else n_line[mark_idx:].index("/*")
        )

        if dup_idx >= 0:
            dup_idx += mark_idx
        if bracket_idx >= 0:
            bracket_idx += mark_idx

        if dup_idx >= 0 or bracket_idx >= 0:
            if dup_idx >= 0 and bracket_idx >= 0:
                if bracket_idx < dup_idx:
                    debug and print(f"BRACKET LINE: {n_line[mark_idx:]}")

                    if "*/" in n_line[bracket_idx + 2 :]:
                        close_bracket_idx: int = (
                            n_line[bracket_idx + 2 :].index("*/") + bracket_idx + 2
                        )
                        in_line += n_line[mark_idx:bracket_idx]
                        mark_idx = close_bracket_idx + 2
                    else:
                        bracket_stack.append("/*")
                        if not n_line[mark_idx:bracket_idx]:
                            check_empty_stack.append(True)

                        in_line += n_line[mark_idx:bracket_idx]
                        break
                else:
                    in_line += n_line[mark_idx:dup_idx]
                    break

            elif bracket_idx >= 0:
                debug and print(f"BRACKET LINE: {n_line[mark_idx:]}")
                if "*/" in n_line[bracket_idx + 2 :]:
                    close_bracket_idx: int = (
                        n_line[bracket_idx + 2 :].index("*/") + bracket_idx + 2
                    )
                    in_line += n_line[mark_idx:bracket_idx]
                    mark_idx = close_bracket_idx + 2
                else:
                    bracket_stack.append("/*")
                    if not n_line[mark_idx:bracket_idx]:
                        check_empty_stack.append(True)
                    in_line += n_line[mark_idx:bracket_idx]
                    break
            elif dup_idx >= 0:
                in_line += n_line[mark_idx:dup_idx]
                break
        else:
            in_line += n_line[mark_idx:]
            break

        debug and print(f"INLINE: {in_line}")

    else:
        in_line += n_line[mark_idx:]

    debug and print(f'RESULT INLINE: "{in_line}"')
    return in_line


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        bracket_stack = []
        check_empty_stack: List[bool] = []

        new_source: List[str] = []
        for idx, line in enumerate(source):
            is_in_cmt: bool = bool(bracket_stack)

            if is_in_cmt:
                bracket_idx = -1 if "*/" not in line else line.index("*/")
                if bracket_idx < 0:
                    source[idx] = ""
                else:
                    debug and print(f"APPEND: {source[idx][bracket_idx + 2 :]}")
                    bracket_stack.pop()
                    debug and print(f"CHECK EMPTY: {check_empty_stack}")
                    if check_empty_stack:
                        _inline = remove_cmt_inline2(
                            source[idx][bracket_idx + 2 :], bracket_stack, []
                        )
                        if _inline:
                            new_source.append(_inline)
                        check_empty_stack.pop()
                    else:
                        new_source[-1] += remove_cmt_inline2(
                            source[idx][bracket_idx + 2 :], bracket_stack, []
                        )
                    source[idx] = ""
            else:
                # source[idx] = re.sub(bracket_pattern, "", source[idx])
                source[idx] = remove_cmt_inline2(
                    source[idx], bracket_stack, check_empty_stack
                )

            if len(source[idx]) > 0:
                new_source.append(source[idx])

        debug and print(f"OUTPUT: {new_source}")
        return new_source


# @lc code=end

debug = True

if __name__ == "__main__":
    s = Solution()
    assert s.removeComments(
        [
            "/*Test program */",
            "int main()",
            "{ ",
            "  // variable declaration ",
            "int a, b, c;",
            "/* This is a test",
            "   multiline  ",
            "   comment for ",
            "   testing */",
            "a = b + c;",
            "}",
        ]
    ) == ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"]
    assert s.removeComments(["a/*comment", "line", "more_comment*/b"]) == ["ab"]
    assert s.removeComments(
        [
            "class test{",
            "public: ",
            "   int x = 1;",
            "   /*double y = 1;*/",
            "   char c;",
            "};",
        ]
    ) == ["class test{", "public: ", "   int x = 1;", "   ", "   char c;", "};"]
    assert s.removeComments(
        [
            "main() {",
            "  Node* p;",
            "  /* declare a Node",
            "  /*float f = 2.0",
            "   p->val = f;",
            "   /**/",
            "   p->val = 1;",
            "   //*/ cout << success;*/",
            "}",
            " ",
        ]
    ) == ["main() {", "  Node* p;", "  ", "   p->val = 1;", "   ", "}", " "]
    assert s.removeComments(["a//*b//*c", "blank", "d/*/e*//f"]) == [
        "a",
        "blank",
        "d/f",
    ]
    assert s.removeComments(["a/*/b//*c", "blank", "d/*/e*//f"]) == ["ae*"]
    assert s.removeComments(["a", "/*comment", "line", "more_comment*/b"]) == ["a", "b"]

    # print(
    #     remove_cmt_inline2(
    #         "/*/dadb/*/aec*////*//*ee*//*//b*////*badbda//*bbacdbbd*//ceb//*cdd//**//de*////*",
    #         [],
    #     )
    # )
    # a = []
    # # print(f"{remove_cmt_inline2('d/*/e*//f', a)} -> {a}")
    # print(f"{remove_cmt_inline2('   /*double y = 1;*/', a)} -> {a}")

    # print(o)

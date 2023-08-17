#
# @lc app=leetcode id=591 lang=python3
#
# [591] Tag Validator
#


# @lc code=start
import re
from typing import List, Tuple

debug = False

open_or_close_tag_regex = re.compile(r"<[A-Za-z]*>|<\/[A-Za-z]*>")
open_tag_regex = re.compile(r"<[A-Za-z]*>")
close_tag_regex = re.compile(r"<\/[A-Za-z]*>")
tag_regex = re.compile(r"(<[A-Z]*>)(.*)(<\/[A-Z]*>)")

u_open_tag_regex = re.compile(r"<[A-Z]*>")
u_close_tag_regex = re.compile(r"<\/[A-Z]*>")


def check_tag_name(tag: str):
    tag_name: str = tag.replace("<", "").replace(">", "").replace("/", "")
    if not tag_name.isupper():
        return False
    if len(tag_name) > 9 or len(tag_name) < 1:
        return False

    return True
    # return u_close_tag_regex.match(tag) or u_open_tag_regex.match(tag)


def check_tag_content(tag_content: str) -> bool:
    str_output = re.sub(r"<!\[CDATA\[.*\]\]>", "", tag_content)
    debug and print(f"NORMALIZE TAG CONTENT: {str_output}")

    if bool(tag_regex.findall(tag_content)):
        return True

    if "<" in str_output:
        return False

    return True


def normalize_cdata(code: str) -> str:
    code = code.strip()
    if "<![CDATA" in code:
        cdata_idxes: List[int] = [m.start() for m in re.finditer(r"<!\[CDATA", code)]
        cdata_idxes.reverse()
        debug and print(f"CDATA INDEXES: {cdata_idxes}")
        cdata_parts: List[str] = []
        for idx, cdata_idx in enumerate(cdata_idxes):
            part_cdata = code[cdata_idx:]
            if idx >= 1:
                part_cdata = code[cdata_idx : cdata_idxes[idx - 1]]
            n_cdata: str = re.sub(r"<!\[CDATA\[.*\]\]>", "<![CDATA[abc]]>", part_cdata)

            debug and print(f'PART DATA: "{part_cdata}" to "{n_cdata}"')

            cdata_parts.append(n_cdata)

        cdata_parts.reverse()
        debug and print(f"CDATA PARTS: {cdata_parts}")

        code = code[: cdata_idxes[-1]] + "".join(cdata_parts)

    return code


def check_code(code: str) -> bool:
    code = normalize_cdata(code)

    debug and print(f"CHECK CODE: {code}")
    tags: List[str] = open_or_close_tag_regex.findall(code)
    index_tags: List[Tuple[int, int]] = [
        (m.start(0), m.end(0)) for m in re.finditer(open_or_close_tag_regex, code)
    ]

    debug and print(f"TAGS: {tags}")
    debug and print(f"INDEX TAGS: {index_tags}")

    if code and not tags:
        return False

    if index_tags[0][0] != 0 or index_tags[-1][-1] != len(code):
        return False
    # NOTE: None data
    # if index_tags[0][1] == index_tags[-1][0]:
    #     return False

    tag_stack = []
    tag_index_stack = []
    for idx, tag in enumerate(tags):
        if not check_tag_name(tag):
            return False

        if close_tag_regex.match(tag):
            if not tag_stack or tag.replace("/", "") != tag_stack[-1]:
                debug and print("ONE")
                return False

            c_tag: str = code[tag_index_stack[-1][1] : index_tags[idx][0]]
            debug and print(f'CONTENT BETWEEN "{tag}" - "{tag_stack[-1]}": "{c_tag}"')
            if not check_tag_content(c_tag.strip()):
                debug and print(f"TWO: {c_tag}")
                return False

            tag_stack.pop()
            tag_index_stack.pop()

            if not tag_stack and idx < len(tags) - 1:
                debug and print("THREE")
                return False

        elif open_tag_regex.match(tag):
            tag_stack.append(tag)
            tag_index_stack.append(index_tags[idx])

    return not tag_stack


class Solution:
    def isValid(self, code: str) -> bool:
        return check_code(code)

        # tag_stack = []
        # tags = tag_regex.findall(code)
        # for tag in tags:
        #     print(f"TAG: {tag}")
        # if close_tag_regex.match(tag):
        #     # CLOSE TAG
        #     if not tag_stack or tag.replace("/", "") != tag_stack[-1]:
        #         return False

        #     tag_stack.pop()
        # elif open_tag_regex.match(tag):
        #     # OPENT TAG
        #     tag_stack.append(tag)

        # return not tag_stack


# @lc code=end

debug = False

if __name__ == "__main__":
    code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"  # true
    code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"  # true
    # code = "<A>  <B> </A>   </B>"  # false
    # code = "<DIV>  unmatched <  </DIV>"  # false
    # code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"  # true
    # code = "<DIV>This is the first line <![CDATA[<div>]]><DIV>"  # false
    # code = "<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>"  # false
    # code = "<A></A><B></B>"  # false
    # code = "<A><A>/A></A></A>"  # false
    # # code = "<A><A></A></A></A>"  # false
    # # code = "<A><A>456</A>  <A> 123  !!  <![CDATA[<![cdata]>]]>  123 </A>   <A><![CDATA[</A>]]>  </A>  <A>123</A></A>" # false
    # code = "<A><A>456</A>  <A> 123  !!  <![CDATA[<![cdata]>]]>  123 </A>   <A><![CDATA[</A>]]>  </A>  <A>123</A></A>"  # true
    # code = "<Aa><B><![CDATA[<B></Aa>]]></B></Aa>"  # false
    # code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"  # false
    code = "<DIV><A></A></DIV>"  # false
    # code = "<<A></A>"  # false
    # code = "<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>"  # false
    # code = "<A></A>>"  # false
    # code = "<AAAAAAAAAA></AAAAAAAAAA>"  # false
    code = "<DIV>This is the first line <![CDATA[<div> <![cdata]> [[]]</div>   ]]>  <DIV> <A>  <![CDATA[<b>]]>  </A>  <A> <C></C></A></DIV>    </DIV>"  # false

    s = Solution()
    print(s.isValid(code))

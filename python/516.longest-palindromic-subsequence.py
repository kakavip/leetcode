#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#


# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def dp(min_idx, max_idx) -> int:
            if (min_idx, max_idx) in cache:
                return cache[(min_idx, max_idx)]

            if min_idx > max_idx:
                return 0
            if s[min_idx] == s[max_idx]:
                if min_idx == max_idx:
                    return 1
                return 2 + dp(min_idx + 1, max_idx - 1)
            else:
                cache[(min_idx, max_idx)] = max(
                    dp(min_idx + 1, max_idx), dp(min_idx, max_idx - 1)
                )
                return cache[(min_idx, max_idx)]

        return dp(0, len(s) - 1)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq("bbbab"))
    print(s.longestPalindromeSubseq("cbbd"))
    print(s.longestPalindromeSubseq("c"))
    print(
        s.longestPalindromeSubseq(
            "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
        )
    )

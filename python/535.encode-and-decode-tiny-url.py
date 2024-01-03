#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHAR_MAP = {}
for idx, c in enumerate(BASE62):
    CHAR_MAP[c] = idx


def string_to_base62(string):
    # Convert the string to a number using UTF-8 encoding
    num = int.from_bytes(string.encode("utf-8"), "big")

    # Use the same logic as the encode function in the answer
    if num == 0:
        return BASE62[0]
    arr = []
    while num > 0:
        num, rem = divmod(num, 62)
        arr.append(BASE62[rem])
    arr.reverse()
    return "".join(arr)


def base62_to_string(string):
    # Use the same logic as the decode function in the answer
    num = 0
    for char in string:
        num = num * 62 + CHAR_MAP[char]

    # Convert the number back to a string using UTF-8 encoding
    return num.to_bytes((num.bit_length() + 7) // 8, "big").decode("utf-8")


class Codec:
    base_url: str = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        return self.base_url + string_to_base62(longUrl)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""

        return base62_to_string(shortUrl.replace(self.base_url, ""))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
if __name__ == "__main__":
    s = Codec()
    print(s.encode("https://leetcode.com/problems/design-tinyurl"))
    print(
        s.decode(
            "http://tinyurl.com/FaeHJK15AUBPXt3eDd7OKW7GHdI0ZcSwi8p1gtop4cPjCObPgmsojQgSQFu"
        )
    )

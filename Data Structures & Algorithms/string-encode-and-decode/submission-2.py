class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s

        return ret

    # [hi, bye] -> "2#hi3#bye"

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            "2#hi"
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            res.append(word)
            i = j + 1 + length

        return res


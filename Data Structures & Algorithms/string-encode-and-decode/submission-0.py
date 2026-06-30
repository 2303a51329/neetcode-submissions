class Solution:
    def encode(self, strs: list[str]) -> str:
        # Encode each string as: length + '#' + string
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the separator '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])   # length of the next string
            j += 1                 # move past '#'
            res.append(s[j:j+length])
            i = j + length         # move to next encoded part
        return res

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = self.encode_length(len(strs)) + "".join([self.encode_length(len(s)) for s in strs]) + "".join(strs)
        return s

    def encode_length(self, l: int) -> str:
        if l < 10:
            return "00" + str(l)
        elif l < 100:
            return "0" + str(l)
        else:
            return str(l)

    def decode(self, s: str) -> List[str]:
        arr_len = int(s[:3])
        lengths = [self.decode_length(s[i:i+3]) for i in range(3, 3 + arr_len * 3, 3)]

        strs = []
        i = 3 + arr_len * 3

        for l in lengths:
            strs.append(s[i:i+l])
            i += l

        return strs

    def decode_length(self, s: str) -> int:
        if s == "-1":
            return 100
        else:
            return int(s)
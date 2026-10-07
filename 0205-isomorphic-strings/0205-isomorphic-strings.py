class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_st = {}
        map_ts = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in map_st and map_st[char_s] != char_t:
                return False

            if char_t in map_ts and map_ts[char_t] != char_s:
                return False

            map_st[char_s] = char_t
            map_ts[char_t] = char_s

        return True
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_ptr, s_ptr = 0, 0
        while t_ptr < len(t) and s_ptr < len(s):
            if t[t_ptr] == s[s_ptr]:
                t_ptr += 1
                s_ptr += 1
            else:
                t_ptr += 1

        return s_ptr == len(s)

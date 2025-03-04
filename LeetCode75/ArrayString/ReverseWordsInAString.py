class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.strip().split(" ")
        s_split = [x for x in s_split if x != ""]
        s_split.reverse()
        return " ".join(s_split)

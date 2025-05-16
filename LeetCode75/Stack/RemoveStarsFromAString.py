class Solution:
    def removeStars(self, s: str) -> str:
        left = s[0 : s.find("*")]
        right = s[s.find("*") :]

        while "*" in right:
            if "*" == right[0]:
                left = left[0:-1]
            else:
                left = left + right[0]
            right = right[1:]

        return "".join(left + right)

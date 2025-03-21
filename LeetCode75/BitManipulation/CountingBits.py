class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        ans, prev = [0, 1], [1]
        while len(ans) < (n + 1):
            prev2 = [x + 1 for x in prev]
            ans.extend(prev)
            ans.extend(prev2)
            prev = prev + prev2

        return ans[0 : n + 1]

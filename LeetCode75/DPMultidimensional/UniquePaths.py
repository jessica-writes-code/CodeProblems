class Solution:
    def __init__(self):
        self._memo = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if (m, n) in self._memo:
            return self._memo[(m, n)]

        if m == 1 or n == 1:
            return 1

        ans = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        self._memo[(m, n)] = ans

        return ans

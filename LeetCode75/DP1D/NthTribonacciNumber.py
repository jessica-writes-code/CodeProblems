class Solution:
    def __init__(self):
        self.MEMO = {}

    def tribonacci(self, n: int) -> int:

        if n in self.MEMO:
            return self.MEMO[n]

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            t_n = self.tribonacci(n - 3)
            t_n1 = self.tribonacci(n - 2)
            t_n2 = self.tribonacci(n - 1)

            sol = t_n + t_n1 + t_n2
            self.MEMO[n] = sol

            return sol

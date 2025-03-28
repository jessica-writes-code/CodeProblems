class Solution:
    def guessNumber(self, n: int) -> int:
        g, lower_bound, upper_bound = int(n / 2), 1, n
        guess_result = guess(g)
        while guess_result != 0:
            if guess_result == 1:
                lower_bound = g + 1
            else:
                upper_bound = g - 1
            g = int((lower_bound + upper_bound) / 2)
            guess_result = guess(g)

        return g

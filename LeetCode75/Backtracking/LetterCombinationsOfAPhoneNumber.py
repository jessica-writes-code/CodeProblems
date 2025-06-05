class Solution:

    LOOKUP = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit0_options = self.LOOKUP[digits[0]]
        subsequent_digits_combinations = self.letterCombinations(digits[1:])

        combinations = []
        for letter in digit0_options:
            if len(subsequent_digits_combinations) == 0:
                combinations.append(letter)
            else:
                for sdc in subsequent_digits_combinations:
                    combinations.append(letter + sdc)

        return combinations

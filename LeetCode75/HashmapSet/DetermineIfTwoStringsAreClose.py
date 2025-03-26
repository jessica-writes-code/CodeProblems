class Solution:
    def getLetterCounts(self, word: str) -> dict:
        word_dict = {}
        for l in word:
            if l in word_dict:
                word_dict[l] += 1
            else:
                word_dict[l] = 1
        word_counts = sorted([v for k, v in word_dict.items()])
        return word_counts

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        return self.getLetterCounts(word1) == self.getLetterCounts(word2)

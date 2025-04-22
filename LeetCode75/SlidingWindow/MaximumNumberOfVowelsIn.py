class Solution:
    @staticmethod
    def isVowel(a: str):
        return int(a in "aeiou")

    def maxVowels(self, s: str, k: int) -> int:
        subs = s[0:k]
        is_vowel = [self.isVowel(letter) for letter in subs]
        total_vowels = sum(is_vowel)
        max_total_vowels = total_vowels

        for letter in s[k:]:
            letter_is_vowel = self.isVowel(letter)

            subs += letter
            is_vowel.append(letter_is_vowel)
            total_vowels += letter_is_vowel

            if len(subs) > k:
                total_vowels -= is_vowel[0]
                is_vowel = is_vowel[1:]
                subs = subs[1:]

            if total_vowels > max_total_vowels:
                max_total_vowels = total_vowels
                if max_total_vowels == k:
                    return k

        return max_total_vowels

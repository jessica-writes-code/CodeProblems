class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels, locations, s_list = [], [], [l for l in s]
        for i in range(len(s)):
            if s_list[i].lower() in ["a", "e", "i", "o", "u"]:
                vowels.append((s_list[i]))
                locations.append(i)

        locations.reverse()
        for v, l in zip(vowels, locations):
            s_list[l] = v

        return "".join(s_list)

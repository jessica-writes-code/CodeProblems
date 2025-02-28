class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (
                    (len(flowerbed) == 1)
                    or ((i == 0) and (flowerbed[i + 1] == 0))
                    or ((i == len(flowerbed) - 1) and (flowerbed[i - 1] == 0))
                    or ((flowerbed[i - 1] == 0) and (flowerbed[i + 1] == 0))
                ):
                    n -= 1
                    flowerbed[i] = 1

        return n <= 0

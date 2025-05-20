class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right, right_running = [], 1
        for n in nums:
            right.append(right_running)
            right_running = right_running * n

        left, left_running = [], 1
        for n in nums[::-1]:
            left.append(left_running)
            left_running = left_running * n
        left.reverse()

        return [r * l for r, l in zip(right, left)]

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = k
        interval_sum = sum(nums[0:k])
        max_value = interval_sum
        while i < len(nums):
            interval_sum = interval_sum - nums[i - k]
            interval_sum = interval_sum + nums[i]

            if interval_sum > max_value:
                max_value = interval_sum
            i += 1

        return max_value / k

class Solution:

    MAP = {}

    def rob_recursively(self, nums: Tuple[int]) -> int:
        if nums in self.MAP:
            return self.MAP[nums]

        if len(nums) == 0:
            max_money = 0
        elif len(nums) == 1:
            max_money = nums[0]
        else:
            max_money = None
            for i, num in enumerate(nums):
                money = num + self.rob(nums[i + 2 :])
                if max_money is None or money > max_money:
                    max_money = money

        self.MAP[nums] = max_money

        return max_money

    def rob(self, nums: List[int]) -> int:
        return self.rob_recursively(tuple(nums))

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        temp_inventory = {}
        temperatures.reverse()
        for i, t in enumerate(temperatures):
            # Check inventory
            min_diff = None
            for k, v in temp_inventory.items():
                if k > t:
                    diff = i - temp_inventory[k]
                    if min_diff is None or diff < min_diff:
                        min_diff = diff

            if min_diff is not None:
                answer[i] = min_diff

            # Add to inventory
            temp_inventory[t] = i

        answer.reverse()
        return answer

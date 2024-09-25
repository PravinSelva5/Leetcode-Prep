class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_tracker = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in sum_tracker:
                return [sum_tracker[complement], i]
            else:
                sum_tracker[nums[i]] = i
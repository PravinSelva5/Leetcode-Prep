class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        cur_sum = 0
        min_len = float('inf')
        i = 0

        for num in range(len(nums)):

            cur_sum += nums[num]

            while cur_sum >= target:

                min_len = min(min_len, num - i + 1)
                cur_sum -= nums[i]
                i += 1
        

        return min_len if min_len != float('inf') else 0
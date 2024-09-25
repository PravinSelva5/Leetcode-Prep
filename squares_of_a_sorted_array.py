#Solution 1


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0 
        end = len(nums) - 1
        count = len(nums) - 1
        res = [0] * len(nums)

        # Square the integers
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        
        while start <= end:
            
            if nums[start] > nums[end]:
                res[count] = nums[start]
                start += 1
            else:
                res[count] = nums[end]
                end -= 1
            count -= 1

        return res


#Solution 2

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0 
        end = len(nums) - 1
        count = len(nums) - 1
        res = [0] * len(nums)        

        while start <= end:
            start_squared = nums[start] ** 2
            end_squared = nums[end] ** 2
            
            if start_squared > end_squared:
                res[count] = start_squared
                start += 1
            else:
                res[count] = end_squared
                end -= 1
            count -= 1

        return res
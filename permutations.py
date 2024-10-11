class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]
        
        # subproblem calls
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
    

    ## Solution 2: Using backtracking and recursion
    class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        used = [False] * len(nums)

        def backtrack(current_permutation):
            # Base Case: if current permutation is complete
            if len(current_permutation) == len(nums):
                result.append(current_permutation.copy())
                return
            
            # Recursive case: try all unused elements
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current_permutation.append(nums[i])
                    # Recurse
                    backtrack(current_permutation)
                    # Backtrack
                    current_permutation.pop()
                    used[i] = False
        
        backtrack([])
        return result
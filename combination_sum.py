class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current_combination, current_sum):
            # Base Case
            if current_sum == target:
                result.append(current_combination.copy())
                return
            
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # include the candidate
                current_combination.append(candidates[i])

                # 'i' is passed and not 'i+1' because the same number can be chosen an unlimited # of times
                backtrack(i, current_combination, current_sum + candidates[i])

                # Backtrack
                current_combination.pop()
        
        # backtrack call
        backtrack(0, [], 0)

        return result
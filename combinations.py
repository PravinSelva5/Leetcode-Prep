class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(1, [])

        return res
    

    # Solution 2

    class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, current_combination):
            # Base Case
            if len(current_combination) == k:
                result.append(current_combination.copy())
                return
            
            # Loop through the numbers from start -> n
            for i in range(start, n + 1):
                current_combination.append(i)

                backtrack(i + 1, current_combination)

                current_combination.pop()
        
        backtrack(1, [])

        return result
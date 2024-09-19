class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            # process backspaces for s
            skip_s = 0
            while i >= 0:
                if s[i] == "#":
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break
            
            # process backspaces for t
            skip_t = 0
            while j >= 0:
                if t[j] == "#":
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break
            
            # compare characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
                
            # One string has characters, the other doesn't
            elif i >= 0 or j >= 0:
                return False
                
            # Move to the next character
            i -= 1
            j -= 1
        
        return True
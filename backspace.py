class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.applyBackSpace(S) == self.applyBackSpace(T)
        
        

    def applyBackSpace(self, S):
        i = 0
        while i < len(S):
            print(S)
            if S[i] != "#":
                i += 1
            else:
                if i == 0:
                    S = S[1:]
                else:
                    S = S[:i - 1]  + S[i + 1:]
                    i -= 1
        return S
                    
                    
sol = Solution()
print(sol.backspaceCompare("ab##", "c#d#"))
        
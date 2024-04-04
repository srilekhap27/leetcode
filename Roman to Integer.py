class Solution:
    def romanToInt(self, s: str) -> int:
        X = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total=0
        
        for i in range(len(s)):
            if i+1 < len(s) and X[s[i]] < X[s[i+1]]:
                total=total-X[s[i]]
            else:   
                total=total+X[s[i]]
            
        return total
        
   
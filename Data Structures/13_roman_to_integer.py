class Solution:
    def __init__(self):
        self.roman = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000, 
            'IV': 4, 
            'IX': 9, 
            'XL': 40, 
            'XC': 90, 
            'CD': 400, 
            'CM': 900
        }

    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i + 2] in self.roman:
                total += self.roman[s[i:i + 2]]
                i += 2 
            else:
                total += self.roman[s[i]]
                i += 1
        return total
class Solution:
    def romanToInt(self, s: str) -> int:
        roma_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        special_dict = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        i = 0
        n = len(s)
        res = 0
        
        while i < n:
            if i+1 < n and s[i:i+2] in special_dict:
                res += special_dict[s[i:i+2]]
                i += 2
            else:
                res += roma_dict[s[i]]
                i += 1
        
        return res

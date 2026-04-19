class Solution(object):
    def isPalindrome(self, s):
        filtered = ""
    
        for c in s:
            if c.isalnum():        # chỉ lấy chữ + số
                filtered += c.lower()
        
        return filtered == filtered[::-1]
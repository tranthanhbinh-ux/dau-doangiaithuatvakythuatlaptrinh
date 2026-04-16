class Solution(object):
    def checkString(self, s):
        thay_b = False
    
        for ch in s:
            if ch == 'b':
                thay_b = True
            elif ch == 'a' and thay_b:  #Gặp b → đánh dấu  Nếu sau đó gặp lại a → sai
                return False
        
        return True
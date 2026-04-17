class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
    
        for word in words:
            if word.startswith(pref):    #Nếu từ đó bắt đầu bằng pref → tăng biến đếm
                count += 1
        
        return count
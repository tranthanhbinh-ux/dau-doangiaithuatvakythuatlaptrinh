class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        i = 0  # trẻ
        j = 0  # bánh
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1  # thỏa mãn 1 đứa
            j += 1      # dùng bánh này rồi
        
        return i
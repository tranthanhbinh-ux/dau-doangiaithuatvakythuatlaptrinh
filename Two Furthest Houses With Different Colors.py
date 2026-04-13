class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        res = 0
        # so với đầu
        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                res = max(res, i)
                break
        
        # so với cuối
        for i in range(n):
            if colors[i] != colors[n-1]:
                res = max(res, n-1 - i)
                break
        
        return res
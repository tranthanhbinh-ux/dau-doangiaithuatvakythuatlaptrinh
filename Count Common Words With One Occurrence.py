class Solution(object):
    def countWords(self, words1, words2):
        dem1={}
        dem2={} 
        res=0       
          # đếm words1
        for w in words1:
            dem1[w] = dem1.get(w, 0) + 1
        
        # đếm words2
        for w in words2:
            dem2[w] = dem2.get(w, 0) + 1

        # kiểm tra
        for w in dem1:
            if dem1[w] == 1 and dem2.get(w, 0) == 1:
                res += 1 
        return res
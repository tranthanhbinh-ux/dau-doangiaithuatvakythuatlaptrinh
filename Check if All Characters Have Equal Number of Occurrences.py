class Solution(object):
    def areOccurrencesEqual(self, s):
        dem={}
        for ch in s:
            if ch in dem:
                dem[ch] += 1  #Nếu đã có → tăng thêm 1 lần
            else:
                dem[ch] = 1 #Nếu chưa có → lần đầu tiên xuất hiện → gán = 1
        
        # lấy giá trị đầu tiên
        values = dem.values()
        first = values[0]
        # so sánh tất cả
        for v in values:
            if v != first:
                return False
        
        return True
class Solution(object):
    def largestAltitude(self, gain):
        hientai = 0   # độ cao hiện tại
        max1 = 0   # độ cao lớn nhất
        for g in gain:
            hientai += g # cong độ cao từng bước
            if hientai > max1:
                max1 = hientai
        return max1
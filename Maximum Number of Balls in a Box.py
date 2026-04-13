class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        hop={} #luu số bóng
        for num in range(lowLimit,highLimit +1):
            s =0
            vitri=num
            while vitri > 0:
                s += vitri % 10 #tinh tổng chữ số 10 = 1+0=1
                vitri /= 10
            if s in hop:
                hop[s] += 1 #đếm số bóng trong hộp
            else:
                hop[s] = 1
        return max(hop.values())
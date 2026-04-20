class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max1 = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            gia = price - min_price
            
            if gia > max1:
                max1 = gia
        
        return max1

        #Tại mỗi ngày:
        #thử bán → tính lợi nhuận
        #cập nhật max
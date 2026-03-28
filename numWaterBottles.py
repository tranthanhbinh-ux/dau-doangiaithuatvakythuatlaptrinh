class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = 0
        empty = 0
        full = numBottles

        while full > 0:
            # uống hết chai đầy
            total += full
            
            # chuyển sang chai rỗng
            empty += full
            
            # đổi chai mới
            full = empty // numExchange
            
            # chai rỗng còn dư
            empty = empty % numExchange

        return total
            
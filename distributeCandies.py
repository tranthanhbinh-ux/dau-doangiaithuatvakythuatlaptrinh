class Solution(object):
    def distributeCandies(self, candyType):
        demkeokhacloai = len(set(candyType))  # đếm loại khác nhau
        return min(demkeokhacloai, len(candyType) // 2)
        
class Solution(object):
    def minimumSum(self, num):
        digits = list(map(int, str(num))) #str(num) Chuyển số thành chuỗi , map(int, str(num)) Ép từng ký tự thành số nguyên,Chuyển kết quả trên thành list
        digits.sort()
    
        return digits[0]*10 + digits[2] + digits[1]*10 + digits[3]
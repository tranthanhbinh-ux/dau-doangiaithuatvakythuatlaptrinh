class Solution(object):
    def divideArray(self, nums):
        count = Counter(nums) #đếm số lần xuất hiện
    
        for value in count.values():
            if value % 2 != 0: #Nếu có bất kỳ số nào lẻ → return False
                return False
        
        return True
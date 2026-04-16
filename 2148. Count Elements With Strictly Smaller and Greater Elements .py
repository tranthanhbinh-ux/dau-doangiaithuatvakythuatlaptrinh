class Solution(object):
    def countElements(self, nums):
        mn = min(nums) 
        mx = max(nums)
        
        count = 0
        for x in nums:
            if x > mn and x < mx:   #đếm số phần tử khác min và khác max
                count += 1
                
        return count
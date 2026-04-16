class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort() # sap xep
        res=[] 
        
        for i in range(len(nums)): #duyet tung nums
            if nums[i] == target: #nếu bằng target → lưu lại
                res.append(i)
    
        return res
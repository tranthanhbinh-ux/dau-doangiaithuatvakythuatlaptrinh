class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        n = len(nums)
    
        for i in range(n):
            for j in range(i + 1, n): #Duyệt tất cả cặp (i, j) với i < j
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        
        return count
        
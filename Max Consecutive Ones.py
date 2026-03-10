class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        dem =0
        maxdem = 0
        for num in nums:
            if num ==1:
                dem +=1
                maxdem = max(maxdem,dem)
            else:
                dem =0
        return maxdem

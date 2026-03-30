class Solution(object):
    def findNumbers(self, nums):
        dem =0
        for num in nums:
            if len(str(num)) % 2 ==0:
                dem+=1
        return dem
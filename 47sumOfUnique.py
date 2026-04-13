class Solution(object):
    def sumOfUnique(self, nums):
        count = {}
        # đếm số lần xuất hiện
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # cộng các số xuất hiện đúng 1 lần
        total = 0
        for num in count:
            if count[num] == 1:
                total += num
        return total
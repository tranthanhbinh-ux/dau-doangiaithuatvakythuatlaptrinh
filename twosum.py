class Solution(object):
    def twoSum(self, nums, target):
        ktra = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in ktra:
                return [ktra[complement], i]
            ktra[num] = i
                
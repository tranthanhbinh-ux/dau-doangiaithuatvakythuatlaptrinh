class Solution(object):
    def countHillValley(self, nums):
        # Bước 1: loại bỏ phần tử trùng liên tiếp
        arr = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                arr.append(nums[i])
        
        # Bước 2: đếm hill và valley
        count = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                count += 1  # hill
            elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                count += 1  # valley
        
        return count
class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
            original *= 2 #tìm số original trong mảng, nếu có thì nhân đôi, rồi lặp lại cho đến khi không còn tìm thấy nữa.
        return original
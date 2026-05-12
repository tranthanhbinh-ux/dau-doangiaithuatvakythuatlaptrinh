class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) -1 #tạo con trỏ đầu và cuối

        while left < right:
            s[left], s[right] = s[right], s[left]  # đổi chỗ
            left += 1
            right -= 1
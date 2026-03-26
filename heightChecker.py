class Solution(object):
    def heightChecker(self, heights):
        kiemtra = sorted(heights)  # mảng đúng thứ tự
        count = 0

        for i in range(len(heights)):
            if heights[i] != kiemtra[i]:
                count += 1

        return count
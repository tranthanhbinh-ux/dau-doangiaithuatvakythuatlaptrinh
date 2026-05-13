class Solution(object):
    def dailyTemperatures(self, temperatures): #Phần tử lớn hơn gần nhất bên phải
        n = len(temperatures)
        ans = [0] * n  #Mặc định không có ngày nóng hơn → 0.
        stack = []

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:  #Nếu nhiệt độ hiện tại lớn hơn đỉnh stack
                prev = stack.pop()
                ans[prev] = i - prev

            stack.append(i)

        return ans
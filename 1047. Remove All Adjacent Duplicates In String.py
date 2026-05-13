class Solution(object):
    def removeDuplicates(self, s):
        stack = [] #tao stack

        for ch in s:
            if stack and stack[-1] == ch:  #Nếu giống đỉnh stack
                stack.pop() #Xóa phần tử trên cùng
            else:
                stack.append(ch) #Thêm vào stack.

        return "".join(stack)
        
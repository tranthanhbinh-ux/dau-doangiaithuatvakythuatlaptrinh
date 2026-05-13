class MinStack(object):

    def __init__(self):  #tao 2 stack
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val) #Thêm vào stack chính.

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))  #Cập nhật minStack

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
        

    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.minStack[-1]
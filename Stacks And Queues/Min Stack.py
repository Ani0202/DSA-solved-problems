'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1] >= x:
            self.minStack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack):
            m = self.stack.pop()
            if m == self.minStack[-1]:
                self.minStack.pop()
                
    # @return an integer
    def top(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            return -1


    # @return an integer
    def getMin(self):
        if len(self.stack):
            return self.minStack[-1]
        else:
            return -1


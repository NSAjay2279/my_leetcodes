class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value: any):
        self.stack.append(value)

    def pop(self):
        try:
            if len(self.stack) < 1:
                return
            else:
                temp = []
                for i in range(len(self.stack)-1):
                    temp.append(self.stack[i])
                self.stack = temp
        except:
            pass
            
    def __str__(self):
        return str(self.stack)


myStack = Stack()
myStack.pop()
myStack.push(1)
myStack.push(2)
myStack.push("3")
myStack.push("4")
myStack.pop()
print(myStack)

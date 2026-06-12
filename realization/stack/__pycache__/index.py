from stack import ArrayStack

stack = ArrayStack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.pop()

print(stack)
print(stack.peek())
print(stack.size())
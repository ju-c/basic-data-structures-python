class Stack:

    def __init__(self):
        self.stack = []

    def check_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if (self.check_empty()):
            return "stack is empty"

        return self.stack.pop()

    def __str__(self):
        return str(self.stack)


s = Stack()

s.push('1')
s.push('2')
s.push('3')
s.push('4')

print("Stack before popping an item: ", s)

print("Popped item: " + s.pop())

print("Stack after popping an item: ", s)

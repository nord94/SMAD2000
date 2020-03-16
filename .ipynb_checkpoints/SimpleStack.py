import sys

class SimpleStack(object):
    def __init__(self):
        self.Size = 100
        self.array = self.Size * [0]
        self.end = 0

    def push(self, n):
        self.array[self.end] = n
        self.end += 1
        print("ok")

    def pop(self):
        self.end -= 1
        print(self.array[self.end])

    def back(self):
        print(self.array[(self.end - 1)])

    def size(self):
        print(self.end)

    def clear(self):
        self.end = 0
        print("ok")

    def exit(self):
        print("bye")
        sys.exit(0)


stack = SimpleStack()
while (True):
    command = input()
    if ("pop" in command):
        stack.pop()
    elif ("push" in command):
        number = [int(s) for s in command.split() if s.isdigit()][0]
        stack.push(number)
    elif ("back" in command):
        stack.back()
    elif ("size" in command):
        stack.size()
    elif ("clear" in command):
        stack.clear()
    elif ("exit" in command):
        stack.exit()
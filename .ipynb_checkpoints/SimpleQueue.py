import sys


class SimpleQueue(object):
    def __init__(self):
        self.Size = 100
        self.array = self.Size * [0]
        self.start = 0
        self.end = 0

    def push(self, n):
        self.array[self.end] = n
        self.end += 1
        print("ok")

    def pop(self):
        print(self.array[self.start])
        self.start += 1

    def front(self):
        print(self.array[self.start])

    def size(self):
        print((self.end - self.start))

    def clear(self):
        self.end = 0
        self.start = 0
        self.array = self.Size*[0]
        print("ok")

    def exit(self):
        print("bye")
        sys.exit(0)


queue = SimpleQueue()
while (True):
    command = input()
    if ("pop" in command):
        queue.pop()
    elif ("push" in command):
        queue.push([int(s) for s in command.split() if s.isdigit()][0])
    elif ("front" in command):
        queue.front()
    elif ("size" in command):
        queue.size()
    elif ("clear" in command):
        queue.clear()
    elif ("exit" in command):
        queue.exit()

import sys


class Deque(object):
    def __init__(self):
        self.Size = 100
        self.array = [0] * 100
        self.Front = 0
        self.end = 0
        self.actualSize = 0

    def push_front(self, n):
        self.Front -= 1
        self.array[self.Front] = n
        self.actualSize += 1
        print("ok")

    def push_back(self, n):
        if (self.actualSize != 0):
            self.end += 1
        self.array[self.end] = n
        self.actualSize += 1
        print("ok")

    def pop_front(self):
        print(self.array[self.Front])
        self.array[self.Front] = 0
        if (self.Front != self.end):
            self.Front += 1
        self.actualSize -= 1

    def pop_back(self):
        print(self.array[self.end])
        self.array[self.end] = 0
        if (self.Front != self.end):
            self.end -= 1
        self.actualSize -= 1


    def front(self):
        print(self.array[self.Front])

    def back(self):
        print(self.array[self.end])

    def size(self):
        print(self.actualSize)

    def clear(self):
        self.array = [0] * self.Size
        self.Front = 0
        self.end = 0
        print("ok")

    def exit(self):
        print("bye")
        sys.exit()


deque = Deque()
while (True):
    command = input()
    if ("push_front" in command):
        deque.push_front([int(s) for s in command.split() if s.isdigit()][0])
    elif ("push_back" in command):
        deque.push_back([int(s) for s in command.split() if s.isdigit()][0])
    elif ("pop_front" in command):
        deque.pop_front()
    elif ("pop_back" in command):
        deque.pop_back()
    elif (("front" in command)):
        deque.front()
    elif (("back" in command)):
        deque.back()
    elif ("size" in command):
        deque.size()
    elif ("clear" in command):
        deque.clear()
    elif ("exit" in command):
        deque.exit()

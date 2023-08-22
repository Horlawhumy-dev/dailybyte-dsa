

class Stack:

    def __init__(self):

        self.items = list()
        self.count = 0


    def push(self, data):
        self.items.append(data)
        self.count += 1

    def pop(self):
        popped_off = self.items.pop()
        self.count -= 1
        return popped_off
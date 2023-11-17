class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        # return not (self.items)
        return self.items == []

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()
        
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    # must reverse the stack to count from top down
    def search(self, target):
        reversed_list = list(reversed(self.items))
        for index in range(len(self.items)- 1, -1, -1):
            if reversed_list[index] == target:
                return index
        return -1

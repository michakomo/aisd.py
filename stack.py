class Stack:

    def __init__(self):
        self.items = []
    
    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def top(self):
        if not self.empty:
            return self.items[-1]
        else:
            return "stack is empty"
    
    def size(self):
        return len(self.items)

    def __repr__(self):
    #   return str(self.items.reverse())
        return str(self.items)


def main():
    s = Stack()
    s.push(2)
    s.push(3)
    s.push(6)
    s.push(1)
    s.push(4)

    print(s)


if __name__ == "__main__":
    main()
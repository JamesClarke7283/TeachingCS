"""Stack is a FILO data structure.
1. Push: Add an item to the top of the stack
2. Pop: Remove an item from the top of the stack
3. Peek: Return the top item of the stack
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        try:
            item = self.items.pop()
            return item
        except IndexError:
            return None
        
    
    def peek(self):
        return self.items[-1]

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    # Peek gets the item at the top of the Stack
    print(s.peek())

    lst = []
    lst.append(s.pop())
    lst.append(s.pop())
    lst.append(s.pop())
    print(lst)
    

if __name__ == "__main__":
    main()
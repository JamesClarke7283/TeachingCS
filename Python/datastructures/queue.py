"""A Queue is a FIFO datastructure
1. Enqueue: Add an item to the end of the queue
2. Dequeue: Remove an item from the front of the queue
3. Peek: Return the front item of the queue
"""


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        try:
            item = self.items.pop(0)
            return item
        except IndexError:
            return None

    def peek(self):
        try:
            return self.items[0]
        except IndexError:
            return None


def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Peek gets the item at the front of the Queue
    print(q.peek())

    lst = []
    lst.append(q.dequeue())
    lst.append(q.dequeue())
    lst.append(q.dequeue())
    print(lst)


if __name__ == "__main__":
    main()

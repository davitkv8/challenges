class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return '{' + f"'value': {self.value}, 'next': {self.next_node}" + '}'


class Queue:
    def __init__(self, value):
        self.first = Node(value)
        self.last = self.first
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value=value)

        self.last.next_node = new_node
        self.last = new_node
        self.length += 1

        return self

    def dequeue(self):
        self.first = self.first.next_node
        self.length -= 1
        return self

    def peek(self):
        return self.first

    def __repr__(self):
        return f"{self.first}"


my_queue = Queue(10)
my_queue.enqueue(15)
my_queue.enqueue(25)
my_queue.dequeue()
my_queue.enqueue(45)
my_queue.dequeue()

print(my_queue)

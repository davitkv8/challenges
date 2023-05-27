class Node:
    def __init__(self, value, downside=None):
        self.value = value
        self.downside = downside

    def __repr__(self):
        return '{' + f"'value': {self.value}, 'downside': {self.downside}" + '}'


class Stack:
    def __init__(self, value):
        self.top = Node(value)
        self.bottom = self.top
        self.length = 1

    def push(self, value):
        new_node = Node(
            value=value,
            downside=self.top
        )

        self.top = new_node
        self.length += 1

        return new_node

    def pop(self):
        self.top = self.top.downside
        self.length -= 1

        return self

    def peek(self):
        return self.top

    def __repr__(self):
        return f"{self.top}"


my_stack = Stack(10)
my_stack.push(20)
my_stack.push(25)
my_stack.pop()
my_stack.pop()
my_stack.push(40)

print(my_stack)

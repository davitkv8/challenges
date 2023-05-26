class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return '{' + f"'value': {self.value}, 'next': {self.next}" + '}'


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return self

    def prepend(self, value):
        new_node = Node(value, self.head)

        self.head = new_node
        self.length += 1

        return self

    def insert(self, index, value):
        if index > self.length:
            self.append(value)
            return self

        if index == 0:
            self.prepend(value)
            return self

        previous_node = self.traverse_to_previous_node(index)

        new_node = Node(value, previous_node.next)

        previous_node.next = new_node

    def traverse_to_previous_node(self, index):

        current_node = self.head
        current_index = 0

        while current_node.next:
            if index - 1 == current_index:
                return current_node

            current_node = current_node.next
            current_index += 1

    def remove(self, index):
        if index >= self.length:
            raise IndexError("Index Out Of Range")

        if index == 0:
            self.head = self.head.next

            return self

        previous_node = self.traverse_to_previous_node(index)
        node_to_be_deleted = previous_node.next
        previous_node.next = node_to_be_deleted.next

        return self

    def __repr__(self):
        return f"{self.head}"


myLinkedList = LinkedList(10)
myLinkedList.append(20)
myLinkedList.append(30)
myLinkedList.prepend(5)
myLinkedList.remove(2)
myLinkedList.insert(2, 15)
myLinkedList.append(30)
myLinkedList.remove(0)
myLinkedList.remove(0)
myLinkedList.insert(0, 1)
myLinkedList.insert(100, 100)
myLinkedList.prepend(5)
myLinkedList.insert(1, 11)
myLinkedList.insert(20, 80)
myLinkedList.insert(0, 3)
myLinkedList.remove(1)

print(myLinkedList)

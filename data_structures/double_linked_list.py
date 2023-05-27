class Node:
    def __init__(self, value, next_node=None, back_node=None):
        self.value = value
        self.next = next_node
        self.back = back_node

    def __repr__(self):
        return '{' + f"'value': {self.value}, 'next': {self.next}" + '}'


class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)

        self.head = new_node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        new_node.back = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return self

    def prepend(self, value):
        new_node = Node(
            value=value,
            next_node=self.head,
        )

        self.head.back = new_node
        self.head = new_node
        self.length += 1

        return self

    def traverse_to_node(self, index):

        if index < self.length / 2:
            current_node = self.head
            current_index = 0

            while current_node.next:
                if current_index == index:
                    return current_node

                current_node = current_node.next
                current_index += 1

        else:
            current_node = self.tail
            current_index = self.length - 1
            while current_node.back:
                if current_index == index:
                    return current_node

                current_node = current_node.back
                current_index -= 1

    def remove(self, index):

        if index > self.length - 1:
            raise IndexError("Index Out Of Range")

        the_node = self.traverse_to_node(index)

        previous_node = the_node.back
        next_node = the_node.next

        previous_node.next = next_node
        next_node.back = previous_node

        return self

    def insert(self, index, value):
        the_node = self.traverse_to_node(index)
        previous_node = the_node.back

        new_node = Node(
            value=value,
            back_node=previous_node,
            next_node=the_node
        )

        previous_node.next = new_node
        the_node.back = new_node
        self.length += 1

        return self

    def __repr__(self):
        return f"{self.head}"


my_double_linked_list = DoubleLinkedList(10)
my_double_linked_list.append(5)
my_double_linked_list.append(2)
my_double_linked_list.prepend(1)
my_double_linked_list.prepend(6)
my_double_linked_list.prepend(7)
my_double_linked_list.append(13)

my_double_linked_list.insert(2, 50)
my_double_linked_list.remove(4)

print(my_double_linked_list)

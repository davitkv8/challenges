class LinkedList:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }

        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {
            "value": value,
            "next": None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

        return self

    def prepend(self, value):
        new_node = {
            'value': value,
            'next': self.head
        }

        self.head = new_node
        self.length += 1

        return self

    def insert(self, index, value):
        if index > self.length:
            self.append(value)

        previous_node = self.traverse_to_previous_node(index)

        new_node = {
            "value": value,
            "next": previous_node['next']
        }

        previous_node['next'] = new_node

    def traverse_to_previous_node(self, index):

        current_node = self.head
        current_index = 0

        while current_node['next']:
            if index - 1 == current_index:
                return current_node

            current_node = current_node['next']
            current_index += 1

    def remove(self, index):
        if index >= self.length:
            raise IndexError("Index Out Of Range")

        previous_node = self.traverse_to_previous_node(index)
        node_to_be_deleted = previous_node['next']
        previous_node['next'] = node_to_be_deleted['next']

        return self

    def __repr__(self):
        return f"{self.head}"


myLinkedList = LinkedList(10)
myLinkedList.append(20)
myLinkedList.append(30)
myLinkedList.prepend(5)
myLinkedList.remove(2)
myLinkedList.insert(2, 15)

print(myLinkedList)

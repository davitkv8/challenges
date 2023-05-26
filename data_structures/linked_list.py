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

        current_node = self.head
        current_index = 0

        while current_node['next']:
            if index - 1 == current_index:
                new_node = {
                    'value': value,
                    'next': current_node['next']
                }

                current_node['next'] = new_node
                self.length += 1

            current_node = current_node['next']
            current_index += 1

    def remove(self, index):
        if index >= self.length:
            raise IndexError("Index Out Of Range")

        current_node = self.head
        current_index = 0
        while current_node['next']:
            if index - 1 == current_index:
                node_to_be_deleted = current_node['next']
                current_node['next'] = node_to_be_deleted['next']
                self.length += 1

                return self

            current_node = current_node['next']
            current_index += 1

    def __repr__(self):
        return f"{self.head}"


myLinkedList = LinkedList(10)
myLinkedList.append(20)
myLinkedList.append(30)
myLinkedList.prepend(5)
myLinkedList.remove(2)
myLinkedList.insert(2, 15)

print(myLinkedList)

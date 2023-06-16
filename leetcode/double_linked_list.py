class Node:
    def __init__(self, value, next_node=None, back_node=None):
        self.value = value
        self.next = next_node
        self.back = back_node

    def __repr__(self):
        return '{' + f"'value': {self.value}, 'next': {self.next}" + '}'


class DoubleLinkedList:
    def __init__(self, value=None):

        if value:
            new_node = Node(value)

            self.head = new_node
            self.tail = self.head
            self.length = 1

    def append(self, value):

        try:
            self.head
        except AttributeError:
            self.__init__(value)
            return

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

    def reverse_nodes_in_k_group(self, k):

        start_at_index = k - 1
        stop_at_index = 0

        last_element_index = self.length - k // 2 if self.length % 2 else self.length - 1

        for i in range(self.length // k):
            current_node_from_right = self.traverse_to_node(start_at_index)
            current_node_from_left = self.traverse_to_node(stop_at_index)

            for value in range(k // 2):
                current_node_from_left.value, current_node_from_right.value \
                    = current_node_from_right.value, current_node_from_left.value

                current_node_from_right = current_node_from_right.back
                current_node_from_left = current_node_from_left.next

            stop_at_index = start_at_index + 1
            start_at_index = stop_at_index + k - 1

            if start_at_index > last_element_index:
                break

        return self

    def convert_to_list(self):
        result_list = []
        current_node = self.head

        while current_node.next:
            result_list.append(current_node.value)
            current_node = current_node.next

        result_list.append(current_node.value)

        return result_list

    def __repr__(self):
        return f"{self.head}"





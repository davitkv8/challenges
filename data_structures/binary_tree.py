class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '{' + f"'value': {self.value}, 'left': {self.left}, 'right': {self.right}" + '}'


class BST:
    def __init__(self, value):
        self.root = Node(value)
        self.length = 1

    def insert(self, value):
        new_node = Node(value)
        current_node = self.root
        self.length += 1

        while True:
            if new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    return self

            else:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    return self

    def lookup(self, value):
        current_node = self.root

        while True:

            if value == current_node.value:
                return current_node

            if value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    return "Not Found"
            else:
                if current_node.left:
                    current_node = current_node.left
                else:
                    return "Not Found"

    def __repr__(self):
        return f"{self.root}"


my_binary_tree = BST(10)
my_binary_tree.insert(15)
my_binary_tree.insert(8)
my_binary_tree.insert(13)
my_binary_tree.insert(17)

print(my_binary_tree.lookup(15))

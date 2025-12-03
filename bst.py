from Stack import Stack
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)

        if self.root is None:
            self.root = new_node
            return

        parent = None
        current = self.root

        while current:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        # attach new node
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def inorder(self):
        current = self.root
        stack = Stack()

        while True:
            # go left
            while current:
                stack.push(current)
                current = current.left

            # if stack empty → we are done
            if stack.peek() is None:
                return

            current = stack.pop()
            print(current.key, end=" ")

            current = current.right

    def preorder(self):
        current = self.root
        stack = Stack()

        while True:
            # go left
            while current:
                print(current.key, end=" ")
                stack.push(current)
                current = current.left
            # if stack empty → we are done
            if stack.peek() is None:
                return
            current = stack.pop()
            current = current.right

    def postorder(self):
        current = self.root
        stack = Stack()
        last_visited = None
        while True:
            while current:
                stack.push(current)
                current = current.left
            if stack.peek() is None:
                return
            peek_node = stack.peek()
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                print(peek_node.key, end=" ")
                last_visited = stack.pop()


bst = BST()
for x in [50, 20,40, 60,99]:
    bst.insert(x)

bst.inorder()
print()
bst.preorder()
print()
bst.postorder()
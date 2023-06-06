class BinarySearchTree:

    def __init__(self, key=0, value=0):
        self.root = None
        self._size = 0

    class BSTNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.right = None
            self.left = None

 # Return the number of nodes in the BST

    def size(self):
        return self._size
    
    
    # Add a node to the BST

    def add(self, key, value):
        z = self.BSTNode(key, value)
        y = None
        x = self.root

        while (x != None):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right

        if (y == None):
            self.root = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z

        self._size += 1

    # Perform inorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 2, 3, 4].

    def inorder_walk(self):
        stack = []
        list = []
        x = self.root

        while stack or x:
            if x:
                stack.append(x)
                x = x.left
            else:
                x = stack.pop()
                list.append(x.key)
                x = x.right

        return list

    # Perform postorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 4, 3, 2].

    def postorder_walk(self):
        x = self.root
        stack = []
        stack.append(x)
        list = []

        while stack:
            x = stack.pop()
            list.append(x.key)

            if x.left:
                stack.append(x.left)

            if x.right:
                stack.append(x.right)

        list = list[::-1]

        return list

    # Perform preorder traversal. Must return a list of keys visited in inorder way, e.g. [2, 1, 3, 4].
    def preorder_walk(self):
        x = self.root

        stack = []
        stack.append(x)

        list = []
        while stack:
            x = stack.pop()
            list.append(x.key)
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)

        return list

    # Search the BST for the given key. Return False if the key is not found.
    def search(self, key):
        x = self.root
        while x != None:
            if key == x.key:
                return x.value
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return False

    # Remove a key from the BST. Return False if the key is not present in the BST.
    def remove(self, key):
        x = self.search(key)
        if not x:
            return -1

        to_delete = self.root
        parent = None
        while (to_delete.key != key):
            parent = to_delete
            if (key < to_delete.key):
                to_delete = to_delete.left
            else:
                to_delete = to_delete.right

        #  leaf node case
        if (to_delete.right == None and to_delete.left == None):
            if parent.left == to_delete:
                parent.left = None
            else:
                parent.right = None
            self._size -= 1

        # one child case
        if (to_delete.left == None and to_delete.right != None) or (to_delete.right == None and to_delete.left != None):
            if (to_delete.left == None):
                to_replace = to_delete.right
                to_delete.right = None
            else:
                to_replace = to_delete.left
                to_delete.left = None

            to_delete.key = to_replace.key
            to_delete.value = to_replace.value
            self._size -= 1

        #  two children case
        if (to_delete.right != None and to_delete.left != None):
            to_replace = to_delete.left
            to_replace_parent = None

            if to_replace.right == None:
                to_delete.key = to_replace.key
                to_delete.value = to_replace.value
                to_delete.left = None
                self._size -= 1

            else:
                while (to_replace.right != None):
                    to_replace_parent = to_replace
                    to_replace = to_replace.right
                to_replace_parent.right = None
                to_delete.key = to_replace.key
                to_delete.value = to_replace.value
                self._size -= 1

    # Find the smallest key and return the corresponding key-value pair/tuple, i.e. (key, value)

    def smallest(self):
        x = self.root
        while x.left != None:
            x = x.left

        return (x.key, x.value)

    # Find the largest key and return the corresponding key-value pair/tuple, i.e. (key, value)

    def largest(self):
        x = self.root
        while x.right != None:
            x = x.right

        return (x.key, x.value)


tree = BinarySearchTree()


tree.add(10, "ten")
tree.add(52, 'thirtyfive')
tree.add(5, "five")
tree.add(8, "twenty")
tree.add(1, "forty")
tree.add(40, "three")
tree.add(30, "six")
tree.add(45, "fifteen")


print(tree.size())
print(tree.search(13))
print(tree.search(40))
print(tree.smallest())
print(tree.largest())


# print(tree.preorder_walk())
# tree.remove(40)
# print(tree.preorder_walk())

print(tree.inorder_walk())
tree.remove(40)
print(tree.inorder_walk())

# print(tree.postorder_walk())
# tree.remove(40)
# print(tree.postorder_walk())

class Node:
    def __init__(self, v=0):
        self.value = v
        self.left = None
        self.right = None


class Tree(Node):
    def __init__(self, v=0):
        super().__init__(v)

    def centre_walk(self):  # центрированный обход

        if self.left is not None:
            self.left.centre_walk()
        print(self.value, end=" ")
        if self.right is not None:
            self.right.centre_walk()


class AvlNode(Node):
    def __init__(self, k=0,  v=0):
        self.key = k
        self.height = 0
        super().__init__(v)

    def straight_walk(self):
        print(self.value, end=" ")
        if self.left is not None:
            self.left.straight_walk()
        if self.right is not None:
            self.right.straight_walk()

    def centre_walk(self):  # центрированный обход
        if self.left is not None:
            self.left.centre_walk()
        print(self.value, end=" ")
        if self.right is not None:
            self.right.centre_walk()
            
    def reverse_walk(self):
        if self.left is not None:
            self.left.reverse_walk()
        if self.right is not None:
            self.right.reverse_walk()
        print(self.value, end=" ")

    def width_walk(self):

        def print_level(node, level):
            if node is None:
                return
            if level == 0:
                print(node.value, end = ' ')
            if level > 0:
                print_level(node.left, level-1)
                print_level(node.right, level-1)

        h = self.height

        for i in range(h+1):
            print_level(self, i)


def get_height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1


def get_balance(node):
    if node is None:
        return 0
    else:
        return get_height(node.left) - get_height(node.right)


def swap(a, b):
    a.key, b.key = b.key, a.key
    a.value, b.value = b.value, a.value


def right_rotate(node):
    swap(node, node.left)
    buffer = node.right
    node.right = node.left
    node.left = node.right.left
    node.right.left = node.right.right
    node.right.right = buffer

    update_height(node.right)
    update_height(node)


def left_rotate(node):
    swap(node, node.right)
    buffer = node.left
    node.left = node.right
    node.right = node.left.right
    # node.right.left = node.right.right
    node.left.right = node.left.left
    node.left.left = buffer

    update_height(node.left)
    update_height(node)


def balance(node):
    bal = get_balance(node)
    if bal == 2:
        if get_balance(node.left) == -1:
            left_rotate(node.left)
        right_rotate(node)
    elif bal == -2:
        if get_balance(node.right) == 1:
            right_rotate(node.right)
        left_rotate(node)


def insert(node, key, value=0):
    if node.key is None:
        node.key = key
        node.value = value
        return

    if key < node.key:
        if node.left is None:
            node.left = AvlNode(key, value)
        else:
            insert(node.left, key, value)
    elif key > node.key:  #  или >???
        if node.right is None:
            node.right = AvlNode(key, value)
        else:
            insert(node.right, key, value)

    update_height(node)
    balance(node)


def delete_avl(node, key):

    def get_min(n):
        if n is None:
            return None
        if n.left is None:
            return n
        return get_min(n.left)

    def get_max(n):
        if n is None:
            return None
        if n.right is None:
            return n
        return get_max(n.right)

    if node is None:
        return None
    elif key < node.key:
        node.left = delete_avl(node.left, key)
    elif key > node.key:
        node.right = delete_avl(node.right, key)
    else:
        if node.left is None or node.right is None:
            if node.left is None:
                node = node.right
            else:
                node = node.left
        else:
            max_left = get_max(node.left)
            node.key = max_left.key
            node.value = max_left.value
            node.left = delete_avl(node.left, max_left.key)

    if node is not None:
        update_height(node)
        balance(node)

    return node


def search(node, key):
    if node is None:
        return None
    if node.key == key:
        return node

    if key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)
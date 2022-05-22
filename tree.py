class Node:
    def __init__(self, key, value, parent, id_nr):
        self.key = key
        self.value = value
        self.id_nr = id_nr
        self.parent = parent
        self.child_list = []

    def add_child(self, node):
        self.child_list.append(node)


class Tree:
    def __init__(self, key, value):
        self.id_nr = 0
        self.root = Node(key=key, value=value, parent=None, id_nr=self.id_nr)
        self.all_nodes = [self.root]

    def show(self):
        print("key== ", self.root.key, "value = ", self.root.value)
        self.show_2(self.root)

    def show_2(self, start):
        print("----")
        for child in start.child_list:
            print("key== ", child.key, "value = ", child.value)
            self.show_2(child)

    def add(self, key, value, start_node):
        self.id_nr += 1
        node = Node(key, value, parent=self.root, id_nr=self.id_nr)
        start_node.child_list.append(node)
        return node


class GameNode:
    def __init__(self, key, value, parent_list, id_nr):
        self.key = key
        self.value = value
        self.id_nr = id_nr
        self.parent_list = parent_list
        self.child_list = []

    def add_child(self, node):
        self.child_list.append(node)

    def add_parent(self, parent):
        self.parent_list.append(parent)


class GameTree:
    def __init__(self, key, value):
        self.id_nr = 1
        self.root = GameNode(key=key, value=value, parent_list=None, id_nr=self.id_nr)
        self.all_nodes = [self.root]

    def show(self):
        print("key== ", self.root.key, "value = ", self.root.value)
        self.show_2(self.root)

    def show_2(self, start):
        print("----")
        for child in start.child_list:
            print("key== ", child.key, "value = ", child.value)
            self.show_2(child)

    def add(self, key, value, start_node):
        self.id_nr += 1
        node = GameNode(key, value, parent_list=[start_node], id_nr=self.id_nr)
        start_node.child_list.append(node)
        self.all_nodes.append(node)
        return node


class BinaryNode:
    def __init__(self, key, value, parent):
        self.parent = parent
        self.right = None
        self.left = None
        self.key = key
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None


    def add(self, key, value, start_node):
        if self.root is None:
            self.root = BinaryNode(key=key, value=value, parent=start_node)
            return
        if key > start_node.key:
            if start_node.right is None:
                start_node.right = BinaryNode(key=key, value=value, parent=start_node)
            else:
                self.add(key, value, start_node.right)
        else:
            if start_node.left is None:
                start_node.left = BinaryNode(key=key, value=value, parent=start_node)
            else:
                self.add(key, value, start_node.left)

    def in_tree(self, key, start_node):
        if start_node.key == key:
            return True
        if self.root is None:
            return False
        if key > start_node.key:
            if start_node.right is None:
                return False
            else:
                return self.in_tree(key, start_node.right)
        else:
            if start_node.left is None:
                return False
            else:
                return self.in_tree(key, start_node.left)

    def find_in_tree(self, key, start_node):
        if start_node.key == key:
            return start_node
        if self.root is None:
            return False
        if key > start_node.key:
            if start_node.right is None:
                return False
            else:
                return self.find_in_tree(key, start_node.right)
        else:
            if start_node.left is None:
                return False
            else:
                return self.find_in_tree(key, start_node.left)


def test_tree_1():
    tree = Tree(key=1, value="A")
    tree.add(key=1, value="B")
    tree.show()


def test_tree_2():
    binary_tree = BinaryTree()
    binary_tree.add(key=5, value="A", start_node=binary_tree.root)
    binary_tree.add(key=6, value="B", start_node=binary_tree.root)
    binary_tree.add(key=7, value="C", start_node=binary_tree.root)
    binary_tree.add(key=8, value="D", start_node=binary_tree.root)
    binary_tree.add(key=9, value="H", start_node=binary_tree.root)
    check = binary_tree.in_tree(key=5, start_node=binary_tree.root)
    print(check)
    check = binary_tree.in_tree(key=6, start_node=binary_tree.root)
    print(check)


# test_tree_1()
test_tree_2()

class Tree(object):
    def __init__(self, root):
        self.root = root

    def printTree(self, root, i):
        i += 1
        print(i, root.name)
        if root == None:
            return
        cur = root
        children = cur.get_children()
        for child in children:
            self.printTree(child, i)


class Node(object):
    def __init__(self, name, size, parent, file):
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent
        self.file = file

    def add_child(self, obj):
        self.children.append(obj)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

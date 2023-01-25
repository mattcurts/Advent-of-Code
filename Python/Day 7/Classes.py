class Tree(object):
    def __init__(self, root):
        """Initialize this tree with the given root node
        input: root node
        output: None"""
        self.root = root

class Node(object):
    def __init__(self, name:str, size:int, parent, file:bool):
        """Initialize this node with the given data
        input: name, size, parent, file
        output: None"""
        self.name:str = name
        self.size:int = size
        self.children:list = []
        self.parent:Node = parent
        self.file:bool = file

    def add_child(self, child):
        """Add a child node to this node
        input: child node
        output: None"""
        self.children.append(child)

    def get_children(self):
        """Return the children of this node
        input: None
        output: list of children"""
        return self.children

    def get_parent(self):
        """Return the parent of this node
        input: None
        output: parent"""
        return self.parent

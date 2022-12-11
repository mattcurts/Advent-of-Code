monkeys = []


class Monkey:
    items = []
    operations = lambda x: (x * 13)
    mod = 1
    test = lambda x: True if x % 19 == 0 else False
    inspections = 0

    def __init__(self, items, operations, test, mod):
        self.items = items
        self.operations = operations
        self.test = test
        self.mod = mod

    def __repr__(self):
        return f"Monkey({self.items,self.inspections,self.mod})"

    def __str__(self):
        return f"Monkey({self.items,self.inspections,self.mod})"

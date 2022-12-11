class Monkey:
    items = []
    operations = lambda x: (x * 13)
    test = lambda x: True if x % 19 == 0 else False
    inspections = 0

    def __init__(self, items, operations, test):
        self.items = items
        self.operations = operations
        self.test = test

    def __repr__(self):
        return f"Monkey({self.items,self.inspections})"

    def __str__(self):
        return f"Monkey({self.items,self.inspections})"


def main():
    with open("Python/Day 11/test01.txt", "r") as f:
        data = list(f.readlines())
        data = [string.strip() for string in data]
        monkeys = []
        monkeys.append(  # 0
            Monkey(
                [75, 75, 98, 97, 79, 97, 64],
                lambda x: (x * 13),
                lambda x: 2 if x % 19 == 0 else 7,
            )
        )
        monkeys.append(  # 1
            Monkey(
                [50, 99, 80, 84, 65, 95],
                lambda x: (x + 2),
                lambda x: 4 if x % 3 == 0 else 5,
            )
        )
        monkeys.append(  # 2
            Monkey(
                [96, 74, 68, 96, 56, 71, 75, 53],
                lambda x: (x + 1),
                lambda x: 7 if x % 11 == 0 else 3,
            )
        )
        monkeys.append(  # 3
            Monkey(
                [83, 96, 86, 58, 92],
                lambda x: (x + 8),
                lambda x: 6 if x % 17 == 0 else 1,
            )
        )

        monkeys.append(  # 4
            Monkey([99], lambda x: (x * x), lambda x: 0 if x % 5 == 0 else 5)
        )
        monkeys.append(  # 5
            Monkey([60, 54, 83], lambda x: (x + 4), lambda x: 2 if x % 2 == 0 else 0)
        )
        monkeys.append(  # 6
            Monkey([77, 67], lambda x: (x * 17), lambda x: 4 if x % 13 == 0 else 1)
        )
        monkeys.append(  # 7
            Monkey(
                [95, 65, 58, 76], lambda x: (x + 5), lambda x: 3 if x % 7 == 0 else 6
            )
        )
    for index in range(10000):  # change to 20 for part 1
        for i in range(len(monkeys)):
            while len(monkeys[i].items) > 0:
                item = monkeys[i].items.pop(0)
                item = monkeys[i].operations(item)
                monkeys[i].inspections += 1
                item = item % 9699690  # change to item = item // 3 for part 1
                # 9,699,690 is the product of the all of the test values
                throwindex = monkeys[i].test(item)
                monkeys[throwindex].items.append(item)
        print("Index at", index)
    i = 0
    for monkey in monkeys:
        print(i, monkey)
        i += 1
    monkeys.sort(key=lambda x: x.inspections, reverse=True)
    part1 = monkeys[0].inspections * monkeys[1].inspections
    print(part1)


if __name__ == "__main__":
    main()

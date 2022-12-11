from input import *

# hardcoded input into a python file called input.py
# input.py contains a list called monkeys contain Monkey objects
# for each monkey in the input file


def superModulo(monkeys):
    superMod = 1
    for monkey in monkeys:
        superMod *= monkey.mod
    return superMod


def solve(monkeys, rounds, worryLevelControl, part):
    for index in range(rounds):  # change to 20 for part 1
        for i in range(len(monkeys)):
            while len(monkeys[i].items) > 0:
                item = monkeys[i].items.pop(0)
                item = monkeys[i].operations(item)
                monkeys[i].inspections += 1
                item = worryLevelControl(item)
                throwIndex = monkeys[i].test(item)
                monkeys[throwIndex].items.append(item)
    monkeys.sort(key=lambda x: x.inspections, reverse=True)
    print(part, monkeys[0].inspections * monkeys[1].inspections)


def main():
    monkeys2 = monkeys.copy()
    superMod = superModulo(monkeys)
    solve(monkeys, 20, lambda x: x // 3, "Part 1: ")
    solve(monkeys2, 10000, lambda x: x % superMod, "Part 2: ")


if __name__ == "__main__":
    main()

import re


def clean(lst):
    lst.append(pop(lst))
    return lst


def pop(cargo):
    x = cargo.pop()
    match = re.search(r"\[[A-Z]\]", x)
    if match:
        return x
    else:
        return pop(cargo)


def move(num, frm, to, cargo):
    # print("move", num, "from", frm, "to", to)
    lst = []
    for i in range(num):
        lst.append(cargo[frm - 1].pop())

    for i in range(num):
        cargo[to - 1].append(lst.pop())


def main():
    f = open("Python/Day 5/input.txt", "r")
    lines = f.readlines()
    part1Solution = 0
    part2Solution = 0
    i = 0
    stacks = []
    cargo = []
    drawingFlag = False
    for line in lines:
        match = re.findall(r"\[[A-Z]\]|\s\d\d?\s\s?|\s{3}[\s]", line)
        if match and not drawingFlag:
            # print("unchanged", line)
            match = re.findall(r"\[[A-Z]\]|\s\d\d?\s\s?|\s{3}[\s]", line)
            stacks.append(match)
        # print("changed", match)

        if match == []:
            numberOfStacks = len(stacks.pop())
            stacks.reverse()
            drawingFlag = True
            for i in range(numberOfStacks):
                x = list(list(zip(*stacks))[0])
                for stack in stacks:
                    if stack != []:
                        stack.remove(stack[0])
                    if stack == []:
                        stack.append(" ")
                cargo.append(x)
            for x in cargo:
                x = clean(x)
                print("before", x)
            continue
        if drawingFlag:
            match = [int(x.strip()) for x in match]
            # print(match)
            move(match[0], match[1], match[2], cargo)
    for x in cargo:
        print(x.pop())
    f.close()


if __name__ == "__main__":
    main()

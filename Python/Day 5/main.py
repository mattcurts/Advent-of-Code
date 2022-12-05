import re


def pop(cargo):
    x = cargo.pop()
    match = re.search(r"[A-Z]", x)
    if match:
        return x
    else:
        return pop(cargo)


def parseCrates(crates):
    crates.reverse()
    cargo = []
    for i in range(len(crates) + 1):
        x = list(list(zip(*crates))[0])
        for stack in crates:
            if stack != []:
                stack.remove(stack[0])
            if stack == []:
                stack.append(" ")
        cargo.append(x)
        for x in cargo:
            x.append(pop(x))
    return cargo


def move(num, frm, to, crates, part):

    if part == 1:
        for i in range(num):
            crates[to - 1].append(crates[frm - 1].pop())
    if part == 2:
        lst = []
        for i in range(num):
            lst.append(crates[frm - 1].pop())
        for i in range(num):
            crates[to - 1].append(lst.pop())


def printTop(crates):
    for crate in crates:
        print(crate[-1], end="")


def main():
    f = open("Python/Day 5/input.txt", "r")
    lines = f.readlines()
    instructionsFlag = False
    startingCrates = re.compile(r"\[[(A-Z)]\]|\s{4}")
    instructions = re.compile(r"move (\d+) from (\d+) to (\d+)")
    crates = []
    for line in lines:
        if line[0] == " ":
            instructionsFlag = True
            crates = parseCrates(crates)

        if not instructionsFlag:
            match = startingCrates.findall(line)
            if match:
                crates.append(match)

        if instructionsFlag:
            match = instructions.match(line)
            if match:
                match = (int(match[1]), int(match[2]), int(match[3]))
                move(*match, crates, 1)
    printTop(crates)
    f.close()


if __name__ == "__main__":
    main()

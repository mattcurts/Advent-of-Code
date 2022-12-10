def checkTargets(cycles, targets, strength):
    for target in targets:
        if cycles == target:
            temp = targets.pop(targets.index(target))
            return True
    return False


def check(strength, columns, rows, display):
    if strength == columns or strength == columns + 1 or strength == columns - 1:
        display[rows][columns] = "#"
    else:
        display[rows][columns] = "."


def main():
    strength = 1
    targets = [20, 60, 100, 140, 180, 220]
    signals = []
    display = [["." for j in range(40)] for i in range(6)]
    i, rows, columns, index, cycles = 0, 0, 0, 0, 0
    addFlag = False
    with open("Python/Day 10/input.txt", "r") as f:
        data = list(f.readlines())
        data = [string.strip() for string in data]
        while index < len(data):
            rows = i // 40
            columns = i % 40
            check(strength, columns, rows, display)
            cycles += 1
            if data[index].startswith("noop"):
                index += 1
            elif addFlag:
                if checkTargets(cycles, targets, strength):
                    signals.append(strength * cycles)
                strength += int(list(data[index].split(" "))[1])
                addFlag = False
                index += 1
            elif data[index].startswith("addx"):
                addFlag = True
            if checkTargets(cycles, targets, strength):
                signals.append(strength * cycles)
            i += 1
    part1 = sum(signals)
    print(part1)
    for part2 in display:
        print(*part2)


if __name__ == "__main__":
    main()

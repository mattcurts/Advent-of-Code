with open("Python/Day 1/test.txt", "r") as f:
    lines:list = f.read().split("\n")

def sumElf(lines:list)->list:
    """Sum the calories per elf
        input: list of calories
        output: list of total calories per elf

    """
    elves:list = []
    sum:int = 0
    for line in lines:
        if line == "":
            elves.append(sum)
            sum = 0
        else:
            sum = sum + int(line)
    elves.append(sum)
    return elves
def main():
    print(lines)
    Elves:list = sumElf(lines)
    Elves.sort(reverse=True)
    print(Elves)
    part1:int = Elves[0]
    part2:int = Elves[0] + Elves[1] + Elves[2]
    print("Part 1:",part1)
    print("Part 2:",part2)

if __name__ == "__main__":
    main()

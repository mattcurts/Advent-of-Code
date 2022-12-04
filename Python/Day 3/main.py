def pointScore(ch):  # scores the points based on the priority
    if ch.isupper():
        return (ord(ch) - ord("A")) + 27
    else:
        return ord(ch) - ord("a") + 1


def part1(lines):
    totalPriority = 0
    for line in lines:
        mid = len(line) // 2
        rucksack1 = line[:mid]
        rucksack2 = line[mid:]  # splits the line into 2 even parts
        totalPriority += pointScore(*(set(rucksack1) & set(rucksack2)))
    print(totalPriority)


def part2(lines):
    totalPriority = 0
    i = 0
    for line in lines[::3]:
        # skipping by 3 so we gather lines in groups of 3
        seen = []
        elf1 = lines[i]
        elf2 = lines[i + 1]
        elf3 = lines[i + 2]
        totalPriority += pointScore(*(set(elf1) & set(elf2) & set(elf3)))
        i += 3
    print("Total priority", totalPriority)


def main():
    f = open("Python/Day 3/input.txt", "r")
    lines = f.read().splitlines()
    part1(lines)
    part2(lines)
    f.close()


if __name__ == "__main__":
    main()

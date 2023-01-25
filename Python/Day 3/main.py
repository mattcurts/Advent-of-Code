with open("Python/Day 3/input.txt", "r") as f:
        lines = f.read().splitlines()

def pointScore(ch: str)-> int:
    """Returns the point value of a character
    based on the priority of the character
    input: ch (str)
    output: int"""
    if ch.isupper():
        return (ord(ch) - ord("A")) + 27
    else:
        return ord(ch) - ord("a") + 1


def part1()-> int:
    """Returns the total priority of all the rucksacks
    where there is one item in common in the first part and the second part
    input: None
    output: int"""
    totalPriority = 0
    for line in lines:
        mid = len(line) // 2
        rucksack1 = line[:mid]
        rucksack2 = line[mid:]  # splits the line into 2 even parts
        totalPriority += pointScore(*(set(rucksack1) & set(rucksack2)))
    return totalPriority


def part2()-> int:
    """Returns the total priority of all the rucksacks where
    there is one item in common in the first line, second line, and third line
    input: None
    output: int"""
    totalPriority = 0
    i = 0
    for line in lines[::3]:
        # skipping by 3 so we gather lines in groups of 3
        elf1 = lines[i]
        elf2 = lines[i + 1]
        elf3 = lines[i + 2]
        totalPriority += pointScore(*(set(elf1) & set(elf2) & set(elf3)))
        i += 3
    return totalPriority


def main():
    print("Part 1:", part1())
    print("Part 2:",part2())

if __name__ == "__main__":
    main()

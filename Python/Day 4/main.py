import re
with open("Python/Day 4/input.txt", "r") as f:
        lines = f.readlines()

def part1()-> int:
    """Returns the number of pairs of elves where one range is completely within the other
    input: None
    output: int"""
    pairs = 0
    for line in lines:
        elf1Start, elf1End, elf2Start, elf2End = map(int, re.split(",|-", line.strip()))
        if elf1Start <= elf2Start and elf1End >= elf2End:
            # elf 2 is completely within elf 1
            pairs = pairs + 1
        elif elf2Start <= elf1Start and elf2End >= elf1End:
            # elf 1 is completely within elf 2
            pairs = pairs + 1

    return pairs


def part2()-> int:
    """Returns the number of pairs of elves where there is any overlap
    input: None
    output: int"""
    pairs = 0
    for line in lines:
        elf1Start, elf1End, elf2Start, elf2End = map(int, re.split(",|-", line.strip()))
        if elf2Start <= elf1End and elf1Start <= elf2End:
            pairs = pairs + 1

    return pairs


def main():
    print("Part 1:",part1())
    print("Part 2:",part2())

if __name__ == "__main__":
    main()

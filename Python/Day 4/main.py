import re


def part1(lines):
    pairs = 0
    for line in lines:
        elf1Start, elf1End, elf2Start, elf2End = map(int, re.split(",|-", line.strip()))
        if elf1Start <= elf2Start and elf1End >= elf2End:
            # elf 2 starts after elf 1 and elf 1 ends before elf 2
            pairs = pairs + 1
        elif elf2Start <= elf1Start and elf2End >= elf1End:
            # elf 1 starts after elf 2 and elf 2 ends after elf 1
            pairs = pairs + 1

    print("Pairs =", pairs)


def part2(lines):
    pairs = 0
    for line in lines:
        elf1Start, elf1End, elf2Start, elf2End = map(int, re.split(",|-", line.strip()))
        if elf1Start <= elf2Start and elf1End >= elf2End:
            # elf 2 starts after elf 1 and elf 1 ends before elf 2
            # elf 2 is a subset of elf 1
            pairs = pairs + 1
        elif elf2Start <= elf1Start and elf2End >= elf1End:
            # elf 1 starts after elf 2 and elf 2 ends after elf 1
            # elf 1 is a subset of elf 2
            pairs = pairs + 1
        elif elf2Start <= elf1End and elf1Start <= elf2End:
            pairs = pairs + 1

    print("Pairs =", pairs)


def main():
    f = open("Python/Day 4/test.txt", "r")
    lines = f.readlines()
    part1(lines)
    part2(lines)
    f.close()


if __name__ == "__main__":
    main()

def solution(data, part):
    if part == 1:
        window = 4
    else:
        window = 14
    for i in range(len(data) - window + 1):
        string = data[i : i + window]
        seen = set([])
        for ch in string:
            seen.add(ch)
        if len(seen) == window:
            print(string)
            print(i + window)
            break


def main():
    f = open("Python/Day 6/input.txt", "r")
    data = f.read()
    solution(data, 1)
    solution(data, 2)
    f.close()


if __name__ == "__main__":
    main()

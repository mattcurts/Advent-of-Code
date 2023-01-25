def solution(data:str, part:int)->None:
    """Solves the problem for part 1 or 2 using
    a sliding window of 4 or 14 characters respectively.
    input: data - string of data
           part - 1 or 2
    output: None """
    if part == 1:
        window = 4
    else:
        window = 14
    for i in range(len(data) - window + 1):
        string = data[i : i + window]
        if len(set(string)) == window:
            print(i + window)
            break


def main():
    f = open("Python/Day 6/input.txt", "r")
    data:str = f.read()
    solution(data, 1)
    solution(data, 2)
    f.close()


if __name__ == "__main__":
    main()

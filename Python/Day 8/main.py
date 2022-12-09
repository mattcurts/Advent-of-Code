# Assisted by: Reddit comments
def count_visible(slice, tree):
    for i in range(len(slice)):
        if slice[i] >= tree:
            return i + 1
    return len(slice)


def main():
    f = open("Python/Day 8/test.txt", "r")
    data = list(f.readlines())
    lst = []
    for string in data:

        letters = [int(ch) for ch in string if ch != "\n"]
        lst.append(letters)
    height = len(lst)
    width = len(lst[0])
    maxScore = 0
    visible = (2 * height) + (2 * (width - 2))
    for i in range(1, len(lst) - 1):  # going down the rows
        for j in range(1, len(lst[i]) - 1):  # going across the columns
            tree = lst[i][j]
            print(lst[i][j])
            if (
                max(lst[i][:j]) < tree  # left
                or max(lst[i][j + 1 :]) < tree  # right
                or max(lst[k][j] for k in range(0, i)) < tree  # above
                or max(lst[k][j] for k in range(i + 1, len(lst))) < tree  # below
            ):
                visible += 1
            score = count_visible(
                lst[i][j - 1 :: -1], tree
            )  # counting visible trees to the left
            score *= count_visible(
                lst[i][j + 1 :], tree
            )  # counting visible trees to the right
            score *= count_visible(
                [lst[k][j] for k in reversed(range(0, i))], tree
            )  # counting visible trees above
            score *= count_visible(
                [lst[k][j] for k in range(i + 1, len(lst))], tree
            )  # counting visible trees below
            maxScore = score if maxScore < score else maxScore

    print(visible, maxScore)
    f.close()


if __name__ == "__main__":
    main()

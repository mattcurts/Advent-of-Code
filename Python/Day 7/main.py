from Classes import Node, Tree


def solution(cur, part, goodSums):
    if cur == None:
        return
    sum = 0
    children = cur.get_children()
    for child in children:
        if child.file == False:
            tempSum, tempGoodSum = solution(child, part, goodSums)
            sum += tempSum
        if child.file == True:
            sum += child.size

    goodSums.append(sum)
    return sum, goodSums


def part1(root, part, goodSums):
    junk, totalSum = solution(root, part, goodSums)
    print(sum([x for x in totalSum if x <= 100000]))


def part2(root, part, goodSums):
    junk, totalSum = solution(root, part, goodSums)
    totalSum.sort()
    required = 30000000 - (70000000 - totalSum[-1])
    print(min([x for x in totalSum if x >= required]))


def strip(s):
    return s.strip()


def File(string, cur):
    file = string.split(" ")
    if file[0] == "dir":
        cur.add_child(Node(file[1], 0, cur, False))
    else:
        cur.add_child(Node(file[1], int(file[0]), cur, True))


def cd(string, root, cur, currentDir):
    if string[5:] == "..":
        return cur.get_parent(), cur.get_parent().name
    elif string[5:] == "/":
        return root, "/"
    else:
        child = [child for child in cur.children if child.name == string[5:]].pop()
        return child, child.name


def main():
    f = open("Python/Day 7/input.txt", "r")
    data = f.readlines()
    data = list(map(strip, data))
    Files = Tree(Node("/", 0, None, False))
    cur = Files.root
    currentDir = "/"
    for string in data:
        if string.startswith("$ ls"):
            pass
        elif string.startswith("$ cd"):
            cur, currentDir = cd(string, Files.root, cur, currentDir)
        else:
            File(string, cur)

    part1(Files.root, 1, [])
    part2(Files.root, 2, [])
    f.close()


if __name__ == "__main__":
    main()

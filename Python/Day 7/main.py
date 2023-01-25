from Classes import Node, Tree
with open("Python/Day 7/input.txt", "r") as f:
        data:list[str] = f.readlines()
        data:list[str] = [x.strip() for x in data]

def solution(cur:Node,  goodSums:int):
    """Find the sum of all the directories in the tree recursively
    input: cur, goodSums
    output: sum, goodSums"""
    if cur == None:
        return
    sum:int = 0
    children:list[Node] = cur.get_children()
    for child in children:
        if child.file == False:
            tempSum:int = solution(child, goodSums)[0]
            sum += tempSum
        else:
            sum += child.size

    goodSums.append(sum)
    return sum, goodSums


def part1(root:Node, goodSums:list[int]):
    """Find the sum of all the files in the tree
     that are at most 100_000 bytes
     input: root, goodSums
     output: sum"""
    totalSum:list[int] = solution(root, goodSums)[1]
    return sum([x for x in totalSum if x <= 100000])


def part2(root, goodSums):
    """find the smallest directory to delete
    that leaves 30_000_000 bytes left of 70_000_000
    input: root, goodSums
    output: smallest directory to delete"""
    totalSum:list[int] = solution(root, goodSums)[1]
    totalSum.sort()
    required = 30_000_000 - (70_000_000 - totalSum[-1])
    return min([x for x in totalSum if x >= required])

def File(cmd:str, cur:Node):
    """Create a file node and add it to the current directory
    input: cmd, cur
    output: None"""
    file:list[str] = cmd.split(" ")
    if file[0] == "dir":
        cur.add_child(Node(file[1], 0, cur, False))
    else:
        cur.add_child(Node(file[1], int(file[0]), cur, True))


def cd(cmd:str, root:Node, cur:Node, currentDir:str):
    """Change the current directory to the given directory
    input: cmd, root, cur, currentDir
    output: cur, currentDir"""
    if cmd[5:] == "..":
        return cur.get_parent(), cur.get_parent().name
    elif cmd[5:] == "/":
        return root, "/"
    else:
        child = [child for child in cur.children if child.name == cmd[5:]].pop()
        return child, child.name

def buildTree(Files, data,):
    """Build the tree from the given data
    input: Files, data
    output: None"""
    cur:Node = Files.root
    currentDir:str = cur.name
    for cmd in data:
        if cmd.startswith("$ ls"):
            pass
        elif cmd.startswith("$ cd"):
            cur, currentDir = cd(cmd, Files.root, cur, currentDir)
        else:
            File(cmd, cur)


def main():
    currentDir:str = "/"
    cur:Node = Node(currentDir, 0, None, False)
    Files:Tree = Tree(cur)
    buildTree(Files, data)
    print("Part 1:",part1(Files.root, []))
    print("Part 2:",part2(Files.root, []))


if __name__ == "__main__":
    main()

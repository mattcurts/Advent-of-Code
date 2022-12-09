def distance(head, tail):
    return (head[0] - tail[0], head[1] - tail[1])


def move(cur, distance):
    return (cur[0] + distance[0], cur[1] + distance[1])


def follow(head, tail):
    distanceX, distanceY = distance(head, tail)
    if abs(distanceX) > 1 or abs(distanceY) > 1:
        if distanceX > 0 and distanceY > 0:  # moving up and right
            newtail = move(tail, (1, 1))
        elif distanceX > 0 and distanceY < 0:  # moving down and right
            newtail = move(tail, (1, -1))
        elif distanceX < 0 and distanceY > 0:  # moving up and left
            newtail = move(tail, (-1, 1))
        elif distanceX < 0 and distanceY < 0:  # moving down and left
            newtail = move(tail, (-1, -1))
        elif distanceX > 0 and distanceY == 0:  # moving right
            newtail = move(tail, (1, 0))
        elif distanceX < 0 and distanceY == 0:  # moving left
            newtail = move(tail, (-1, 0))
        elif distanceX == 0 and distanceY > 0:  # moving up
            newtail = move(tail, (0, 1))
        elif distanceX == 0 and distanceY < 0:  # moving down
            newtail = move(tail, (0, -1))
        return newtail
    return tail


def main():
    f = open("Python/Day 9/input.txt", "r")
    data = f.read().splitlines()
    direction = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    seen1 = set()
    seen2 = set()
    part1 = [(0, 0)] * 2
    part2 = [(0, 0)] * 10
    for line in [line.split(" ") for line in data]:
        line[1] = int(line[1])
        for i in range(int(line[1])):
            part1[0] = move(part1[0], direction[line[0]])
            part1[1] = follow(part1[0], part1[1])
            seen1.add(part1[-1])
            part2[0] = move(part2[0], direction[line[0]])
            for i in range(1, len(part2)):
                part2[i] = follow(part2[i - 1], part2[i])
            seen2.add(part2[-1])

    print(len(seen1))
    print(len(seen2))
    f.close()


if __name__ == "__main__":
    main()

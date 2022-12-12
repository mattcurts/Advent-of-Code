# I know this code can be improved using dynamic programming, but I'm not sure how to do it.
def findStart(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                data[i][j] = "a"
                return i, j
    return None


def findEnd(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "E":
                data[i][j] = "z"
                return i, j
    return None


def getNeighbors(data, x, y, distanceFromStart):
    neighbors = []
    ch = data[x][y]
    if x > 0 and checkNeighbor(data, x - 1, y, ch):
        neighbors.append({"x": x - 1, "y": y, "distanceFromStart": distanceFromStart})
    if x < len(data) - 1 and checkNeighbor(data, x + 1, y, ch):
        neighbors.append({"x": x + 1, "y": y, "distanceFromStart": distanceFromStart})
    if y > 0 and checkNeighbor(data, x, y - 1, ch):
        neighbors.append({"x": x, "y": y - 1, "distanceFromStart": distanceFromStart})
    if y < len(data[x]) - 1 and checkNeighbor(data, x, y + 1, ch):
        neighbors.append({"x": x, "y": y + 1, "distanceFromStart": distanceFromStart})
    return neighbors


def checkNeighbor(data, xx, yy, ch):
    if ord(data[xx][yy]) <= ord(ch) + 1:
        return True
    return False


def findAllStarts(data, part):
    starts = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "a" or data[i][j] == "S":
                starts.append((i, j))
    return starts


def bfs(data, start, goalX, goalY):
    distance = 1000
    toVisit = []
    visited = []
    toVisit.append({"x": start[0], "y": start[1], "distanceFromStart": 0})
    while len(toVisit) > 0:
        node = toVisit.pop(0)
        x = node["x"]
        y = node["y"]
        distanceFromStart = node["distanceFromStart"]
        if (x, y) == (goalX, goalY):
            print("Found it!", distanceFromStart)
            distance = distanceFromStart
            break
        if (x, y) not in visited:
            visited.append((x, y))
            toVisit.extend(getNeighbors(data, x, y, distanceFromStart + 1))
    return distance


def main():
    with open("Python/Day 12/input.txt", "r") as f:
        data = list(f.readlines())
        data = [string.strip() for string in data]
        data = [list(string) for string in data]
    goalX, goalY = findEnd(data)
    fromS = findStart(data)
    starts = findAllStarts(data, 2)
    shortestStart = bfs(data, fromS, goalX, goalY)
    print("Part 1 shortest start:", shortestStart)
    # print(starts)
    for start in starts:
        distance = bfs(data, start, goalX, goalY)
        if shortestStart > distance:
            print("New shortest start:", distance)
            shortestStart = distance
    print("Shortest start:", shortestStart)


if __name__ == "__main__":
    main()

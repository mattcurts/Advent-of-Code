def createBoard(rows,cols):
    board = [["." for i in range(cols)] for j in range(rows)]
    with open("Python/Day 14/input.txt", "r") as f:
        data = f.read().splitlines()
        for string in data:
            substring = string.split("->")
            print(substring)
            for i in range(len(substring)-1):
                startCord = substring[i].strip().split(",")
                endCord = substring[i+1].strip().split(",")
                board = drawRocks(board, startCord, endCord)
    return board

def drawRocks(board, start,end):
    startcol, startrow = int(start[0]), int(start[1])
    endcol, endrow = int(end[0]), int(end[1])
    if startcol == endcol: #vertical
        print("Times looping",max(startrow,endrow)+1 - min(startrow,endrow))
        for i in range(min(startrow,endrow), max(startrow,endrow)+1):
            board[i][startcol] = "#"
    elif startrow == endrow:
        for i in range(min(startcol,endcol), max(startcol,endcol)+1):
            board[startrow][i] = "#"
    return board

def getMaxRow(board):
    maxRow = 0
    for i in range(len(board[::])):
        for j in range(len(board[i])):
            if board[i][j] == "#":
                maxRow = max(maxRow,i)
    return maxRow + 2

def drawBottom(board, maxRow):
    for i in range(len(board[maxRow])):
        board[maxRow][i] = "#"
    return board

def dropSand(board, sandSpawn):
    col, row = sandSpawn
    if board[row][col] == "o":
        return board,True
    while True:#while sand is falling
        if row+1 > len(board)-1:
            return board,True
        if board[row+1][col] == "o" or board[row+1][col] == "#":
            if board[row+1][col-1] == ".":#if sand can move left
                col -=1
            elif board[row+1][col+1] == ".":#if sand can move right
                col +=1
            else:#if sand can't move
                board[row][col] = "o"
                break
        row +=1
    return board,False
def main():
    rows, cols = 200, 600 #arbitrary values
    part1Board = createBoard(rows,cols)
    part2Board = createBoard(rows,2*cols)#doubled cols to account for sand overflow
    maxRow = getMaxRow(part2Board)
    part2Board = drawBottom(part2Board,maxRow)
    sandSpawn =(500,0)
    index,part1Index,part2Index = 0,0,0
    part1Stop,part2Stop = False,False
    while index < 100000:
        print("Iteration",index)
        if part1Stop:#if part 1 is done
            part2Board,part2Stop = dropSand(part2Board,sandSpawn)
            if part2Stop:
                part2Index = index
                break
            index+=1
        elif not part2Stop and not part1Stop: #if both are not done
            part1Board,part1Stop = dropSand(part1Board,sandSpawn)
            part2Board,part2Stop = dropSand(part2Board,sandSpawn)
            part1Index = index
            part2Index = index
            index+=1

    print("Done",part1Index,part2Index)

if __name__ == "__main__":
    main()
def shapePoints(shape: int) -> int:
    return shape + 1


def outcomePoints(myMove: int, opponentMove: int) -> int:
    if myMove == 1:
        return 3 + shapePoints(opponentMove)  # Draw
    # adding 1 and modding by 3 makes it equal to the winning move
    elif myMove == 0:
        return 0 + shapePoints((opponentMove - 1) % 3)  # Lose
    # subtracting 1 and modding by 3 makes it equal to the winning move
    elif (myMove) == 2:
        return 6 + shapePoints((opponentMove + 1) % 3)  # Win


def main():
    f = open("Day 2/input.txt", "r")
    lines = f.read().split("\n")
    Score = 0
    print(lines)
    for line in lines:
        line = line.split()
        if len(line) != 0:
            # gives opponentsMove in 0-2 range being [Rock,Paper,Scissors]
            opponentMove = ord(line[0]) - ord("A")
            # give myMove in 0-2 range being [Rock,Paper,Scissors]
            myMove = ord(line[1]) - ord("X")
            moves = ["Rock", "Paper", "Scizzors"]
            print(
                moves[opponentMove], moves[myMove], outcomePoints(myMove, opponentMove)
            )
            print(Score)
            Score = Score + outcomePoints(myMove, opponentMove)
    print(Score)

    f.close()


if __name__ == "__main__":
    main()

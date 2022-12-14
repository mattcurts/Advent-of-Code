def leftInOrder(left, right):#returns 1 if left is in order, 0 if right is in order 2 if unsure
    inOrder = 2
    minlength = min(len(left), len(right))

    for i in range(minlength):
        if type(left[i]) == list and type(right[i]) == list:
            inOrder = leftInOrder(left[i], right[i])
            if inOrder == 1:
                return 1
            elif inOrder == 0:
                return 0
        elif type(left[i]) == list and type(right[i]) != list:
            inOrder = leftInOrder(left[i], [right[i]])
            if inOrder == 1:
                return 1
            elif inOrder == 0:
                return 0
        elif type(left[i]) != list and type(right[i]) == list:
            inOrder = leftInOrder([left[i]], right[i])
            if inOrder == 1:
                return 1
            elif inOrder == 0:
                return 0
        elif left[i] > right[i]:
            return 0
        elif left[i] < right[i]:
            return 1
    if len(left) > len(right):
        return 0
    if len(left) < len(right):
        return 1
    return inOrder

def Sort(data):#bubble sort
    n = len(data)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if leftInOrder(data[j], data[j+1]) == 0:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if swapped == False:
            break
    return data

def main():
    with open("Python/Day 13/input.txt", "r") as f:
        data = f.read().splitlines()
        for string in data:
            if string == "":
                data.remove(string)
        data = [eval(elem) for elem in data] #converts string to list
    leftList = []
    rightList = []
    i=0
    while i < len(data)-1:
        leftList.append(data[i])
        rightList.append(data[i+1])
        i += 2
    sumOfIndex = 0
    i = 0
    for left,right in zip(leftList,rightList):
        i+=1
        if leftInOrder(left, right) == 1:
            sumOfIndex+=i
        else:
            pass
    print("Part 1:Sum of index", sumOfIndex)
    data.append([[6]])
    data.append([[2]])
    sorted = Sort(data)
    part2 =1
    for sort in sorted:
        if sort == [[6]]:
            part2 *= sorted.index(sort)+1
        if sort == [[2]]:
            part2 *= sorted.index(sort)+1
    print("Part 2:Decoder Key", part2)

if __name__ == "__main__":
    main()
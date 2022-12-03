f = open("text.txt", "r")
ElfCount = 1
sum = 0
lines = f.read().split("\n")
Elves = []
for line in lines:

    if line.removesuffix("\n") == "":
        print("Elf #", ElfCount, " amount", sum)
        Elves.append(sum)
        ElfCount += 1
        sum = 0
    else:
        sum = sum + int(line)

Elves.sort(reverse=True)
result = Elves[0] + Elves[1] + Elves[2]
print(result)
f.close()

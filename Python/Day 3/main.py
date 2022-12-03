def pointScore(ch): # scores the points based on the priority
    if ch.isupper():
        return (ord(ch)-ord('A')) + 27
    else:
        return ord(ch)-ord('a') + 1

def part1(lines):
    totalPriority = 0
    for line in lines:
        mid = int((len(line)/2)) 
        rucksack1 = line[0:mid]
        rucksack2 = line[mid:] #splits the line into 2 even parts
        seen = [] 
        for ch in rucksack1:
            if ch in rucksack2 and ch not in seen:
                seen.append(ch) # prevents letters from being double-counted
                totalPriority += pointScore(ch)
    print(totalPriority)

def part2(lines):
    totalPriority = 0
    i =0
    for line in lines[::3]: 
        #skipping by 3 so we gather lines in groups of 3
        seen = []
        elf1 = lines[i]
        elf2 = lines[i+1].strip()
        elf3 = lines[i+2].strip()
        for ch in elf1:
            if(ch in elf2 and ch in elf3 and ch not in seen):
                #finds matching ch in all strings and avoids double counts
                seen.append(ch)
                totalPriority += pointScore(ch)
        i+=3
    print("Total priority",totalPriority)

def main():
    f = open("Python/Day 3/input.txt","r")
    lines = f.readlines()
    part1(lines)
    part2(lines)
    f.close()


if __name__ == "__main__":
    main()
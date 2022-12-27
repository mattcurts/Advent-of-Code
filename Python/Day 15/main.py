# Part 2 could be more optimized, but it works.
# running in reverse because the answer is near the bottom of the grid

def getSensorsAndBeacons(data):
    sensors = []
    beacons = []
    for string in data:
        substring=string.split(":")
        sensorX = substring[0].strip().split("=")[1].strip(", y")
        sensorY = substring[0].strip().split("=")[2]
        beaconX = substring[1].strip().split("=")[1].strip(", y")
        beaconY = substring[1].strip().split("=")[2]
        sensors.append((int(sensorX),int(sensorY)))
        beacons.append((int(beaconX),int(beaconY)))
    return sensors,beacons

def getDistance(sensor,beacon):
    return (abs((sensor[0]-beacon[0])) + abs((sensor[1]-beacon[1])))

def searchRow(sensors,beacons,desiredY):
    ranges =[]
    for sensor,beacon in zip(sensors,beacons):
        maxX = getDistance(sensor,beacon) - abs(sensor[1]-desiredY)
        if maxX > 0:
            ranges.append((sensor[0]-maxX,sensor[0]+maxX))
    return ranges


def part1(sensors,beacons,desiredY):
    ranges = searchRow(sensors,beacons,desiredY)
    nums = set()
    for rangeItem in ranges:
        nums.update(set(range(rangeItem[0],rangeItem[1]+1)))
    for beacon in beacons:
        if beacon[0] in nums and beacon[1] == desiredY:
            nums.remove(beacon[0])
    return len(nums)

def part2(sensors,beacons,maxY):
    for y in range(maxY,0,-1):
        ranges = searchRow(sensors,beacons,y)
        ranges.sort(key=lambda x: x[0])
        noGap,location= noGaps(ranges,maxY)
        if(not noGap):
            return location* 4000000 + y

def noGaps(ranges,maxY):
    start,end = 0,ranges[0][1]
    for i in range(0,len(ranges)):
        if ranges[i][0] <= end and ranges[i][1] >= end:
            end = ranges[i][1]
        elif ranges[i][0] <= end+1 and ranges[i][1] >= end+1:
            end = ranges[i][1]
        if start == 0 and end >= maxY:
            return True,0
    return False,end+1

def main():
    desiredY = 2000000
    maxY = 4000000
    with open("Python/Day 15/input.txt", "r") as f:
        data = f.read().splitlines()
    sensors,beacons = getSensorsAndBeacons(data)
    part1Answer = part1(sensors,beacons,desiredY)
    print("Part 1",part1Answer)
    part2Answer = part2(sensors,beacons,maxY)
    print("Part 2",part2Answer)

# not 6448359
if __name__ == "__main__":
    main()
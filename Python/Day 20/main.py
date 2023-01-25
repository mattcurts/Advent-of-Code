# assisted by r/adventofcode

class Number:
	def __init__(self, value):
		self.value = value

def input(decryption):
	#Making objects so duplicate values can be uniquely identified
	with open("Python/Day 20/input.txt", "r") as f:
		return list(map(lambda x: Number(int(x)*decryption), f.read().splitlines()))

def mix(numbers, order):
	for num in order:
		index = numbers.index(num)
		value = num.value
		newIndex = (index + value)%(len(numbers)-1) # accounting for shrinking list
		if newIndex == 0:
			newIndex = 0 if value >=0 else len(numbers) #to match puzzle input
		numbers.insert(newIndex,numbers.pop(index))

def findZeroIndex(order,numbers):
	for num in order:
		if num.value == 0:
			return numbers.index(num)

def solve(part):
	numbers = input(1 if part == 1 else 811589153)
	order = numbers.copy()
	for i in range(1 if part == 1 else 10):
		mix(numbers, order)

	zeroIndex = findZeroIndex(order,numbers)
	answer = 0
	for i in (1000,2000,3000):
		answer += numbers[(zeroIndex+i)%len(numbers)].value
	return answer
def main():
	print("Part 1:",solve(1))
	print("Part 2:",solve(2))

if __name__ == "__main__":
	main()
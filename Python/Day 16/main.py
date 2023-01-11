# assisted by r/adventofcode
def parseLine(line,connectedTo,rates):
	valve,connections = line.split(";")
	name = valve.split(" ")[1]
	rate = int(valve.split(" ")[-1].split("=")[1])
	# Create a list of connected valves
	connections = connections.split(" ")
	connections = [x.strip(",") for x in connections]
	connections = [x for x in connections if len(x) == 2 and x != "to"]
	connectedTo[name] = connections
	# Create a list of rates
	if rate != 0:
		rates[name] = rate
	rates["AA"] = 0

def distance(connectTo):
	#creates a 2d dictionary to act as a adjacency matrix
	adj = {j:{i:1 if  j in connectTo[i] else float("+inf") for i in connectTo} for j in connectTo}
	for i in connectTo:
		adj[i][i] = 0
	#finds the shortest path between all nodes using floyd warshall
	for k in adj:
		for i in adj:
			for j in adj:
				adj[i][j] = min(adj[i][j],adj[i][k]+adj[k][j])
	return adj

def bitmask(rates,closed):
	#creates a bitmask for each node to check if it has been visited
	keys = list(rates.keys())
	for i in range(len(rates)):
		closed[keys[i]] = 1 << i

def visit(cur,turnsLeft,state,curTotal,answer,adj,rates,closed):
	#Visits each node with a valve to open and finds the best path
	answer[state] = max(answer.get(state,0),curTotal)
	for dest in closed:
		newTurnsLeft = turnsLeft -adj[cur][dest] - 1
		if newTurnsLeft >= 0 and not state & closed[dest]:
			newState = state | closed[dest]
			newCurTotal = curTotal+ newTurnsLeft*rates[dest]
			visit(dest,newTurnsLeft,newState,newCurTotal,answer,adj,rates,closed)
	return answer

def main():
	with open("Python/Day 16/input.txt", "r") as f:
		data = f.read().splitlines()
	connectedTo,rates,closed = {},{},{}
	for line in data:
		parseLine(line,connectedTo,rates)
	bitmask(rates,closed)
	adj = distance(connectedTo)
	part1 = max(visit("AA",30,0,0,{},adj,rates,closed).values())
	print(part1)
	elephantAssist = visit("AA",26,0,0,{},adj,rates,closed)
	part2 = 0
	#ensures the two paths are different
	for key1,val1 in elephantAssist.items():
		for key2,val2 in elephantAssist.items():
			if not key1 & key2:
				part2 = max(part2,val1+val2)
	print(part2)




if __name__ == "__main__":
    main()
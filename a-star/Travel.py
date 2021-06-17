import operator

class City:
	edges = []
 
	def __init__(self, name='', root=None, greedy=0, heuristic=0):
		self.name = name
		self.root = root
		self.greedy = greedy
		self.heuristic = heuristic
		self.cost = greedy + heuristic
  

class Path:
	map = {}
	graph = None
	path_possibilities = []
	air_distance = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176,
                 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 
                 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 
                 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

	def start_search(self, origin, destination, distance):
		if origin not in self.map:
			self.map[origin] = {}
   
		if destination not in self.map:
			self.map[destination] = {}
   
		self.map[origin][destination] = distance
		self.map[destination][origin] = distance


	def read_file(self, file_name):
		file = open(file_name, 'r')
  
		for line in file:
			path = line.split(',')
			self.start_search(path[0], path[1], int(path[2][:-1]))


	def next_path(self, origin):
		edges = self.map[origin.name]
  
		if edges:
			print("\nPossibilities:")
   
			for next_city in edges:
				distance = edges[next_city]
				greedy = origin.greedy + distance
				heuristic = self.air_distance[next_city]
				city = City(next_city, origin, greedy, heuristic)
				origin.edges.append(city)
				self.path_possibilities.append(city)
    
			for path in self.path_possibilities:
				print("- "+path.name+":",path.heuristic,"+",path.greedy,"=",path.heuristic+path.greedy)
    
			self.path_possibilities = sorted(self.path_possibilities, key=operator.attrgetter('cost'))
			most_promising = self.path_possibilities.pop(0)
			print("Most promising: "+most_promising.name+"\n")
   
			return most_promising


	def search_shortest_path(self, origin, destination):
		self.path_possibilities = []
		shortest_path = [origin]
		root = None 	
		greedy = 0
		heuristic = self.air_distance[origin]
		self.graph = City(origin, root, greedy, heuristic)
		city = self.graph
		print("City: greedy + heuristic = cost\n\n\nOrigin:\n- "+origin+":",greedy,"+",heuristic,"=",greedy+heuristic,"\n")
  
		while (city.name != destination):
			city = self.next_path(city)
			shortest_path.append(city.name)
   
		path_list = ' -> '.join(map(str, shortest_path))
		print("\nShortest path:",path_list)
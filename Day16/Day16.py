
from re import X


f = open("example.txt", "r")
#f = open("input.txt", "r")

#2d array of every character in the file
maze = [ list(line.strip()) for line in f ]

class Node:
	def __init__(self, x:int, y:int, _type:chr):
		self.x = x
		self.y = y
		self.prev = None
		self.type = _type
		if( _type == 'S'):
			self.dist = 0
		else:
			self.dist = 2e30
	def wall(self) -> bool:
		return self.type == '#'
	def start(self) -> bool:
		return self.type == 'S'
	def end(self) -> bool:
		return self.type == 'E'
	def empty(self) -> bool:
		return self.type == '.'

start = (0,0)
end = (0,0)
 #find start(S) and end(E) in the maze
for i in range(len(maze)):
	for j in range(len(maze[i])):
		type = maze[i][j]
		maze[i][j] = Node(j,i, type)
		if type == 'S':
			start = maze[i][j]
		elif type == 'E':
			end = maze[i][j]

#declare constants for movement costs
FORWARD = 1
TURN = 1001


def pathing( current: Node, prevmove):
	worknodes = [(current,prevmove)]
	for curr in worknodes:
		dist = curr[0].dist
		x = curr[0].x
		y = curr[0].y
		prevmove = curr[1]
		next = maze[y+prevmove[1]][x+prevmove[0]]
		left = maze[y+prevmove[0]][x+prevmove[1]]
		right= maze[y-prevmove[0]][x-prevmove[1]]
		if( not next.wall() and next.dist >= dist + FORWARD):
			if (next.dist == dist + FORWARD):
				next.prev.append(curr)
			else:
				next.prev = [curr]
			next.dist = dist + FORWARD
			if(not next.end() ):
				worknodes.append( (next, prevmove) )
			else:
				print( f'New best route found {next.dist}')
		if( not left.wall() ) and (left.dist >= dist + TURN):
			if (left.dist == dist + TURN):
				left.prev.append(curr)
			else:
				left.prev = [curr]
			left.dist = dist + TURN
			if(not left.end() ):
				worknodes.append( (left, (prevmove[1], prevmove[0])) )
			else:
				print( f'New best route found {left.dist}')
		if( not right.wall() ) and (right.dist >= dist + TURN):
			if (right.dist == dist + TURN):
				right.prev.append(curr)
			else:
				right.prev = [curr]
			right.dist = dist + TURN
			if(not right.end() ):
				worknodes.append( (right, (-prevmove[1], -prevmove[0])) )
			else:
				print( f'New best route found {right.dist}')


def part1():
	movement = (1,0)
	pathing( start, movement )
	grid = [ [x.type for x in y] for y in maze ]

	tiles = 0
	paths = end.prev.copy()
	for curr in paths:
		if( curr[0] == start):
			continue
		grid[curr[0].y][curr[0].x] = 'X'
		tiles +=1
		paths += curr[0].prev
	for row in grid:
		for n in row:
			print(n, end='')
		print('')

	print( "Part 1")
	print( end.dist)
	print( "Part 2")
	print( tiles)
								 
	
	
part1()
	 



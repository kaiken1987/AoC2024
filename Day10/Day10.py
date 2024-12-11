
#f = open("example.txt", "r")
f = open("input.txt", "r")

#Class to represent graph nodes
class Node:
	
	def __init__(self, value, x, y):
		self.value = int(value)
		self.x = x
		self.y = y
		self.up = []
		self.down = []
		self.paths = 0
		self.peaks = []
	
	#String representation of the node
	def __str__(self):
			return f'({self.value:2d},{self.paths:2d})'

	#link nodes together if they are transitable	
	def link(self, node):
		if node.value-self.value == 1:
			self.up.append(node)
			node.down.append(self)
		elif node.value-self.value == -1:
			self.down.append(node)
			node.up.append(self)
	
	#Recursive function to find all paths from the current node to the head
	def transit1(self, peak ):
		if not peak in self.peaks:
			self.peaks.append(peak)
			for d in self.down:
				d.transit1( peak )
		
	def transit2(self, prevcnt ):
		self.paths += prevcnt
		for d in self.down:
			d.transit2( prevcnt )
			
nodes = []
peaks = []
heads = []

def part1():
	print( "Part 1")
	row = 0
	for line in f:
		col = 0
		nodes.append([])
		for x in line.strip():
			nodes[row].append(Node(x,col,row))
			if(x == '0'):
				heads.append(nodes[row][col])
			if(x == '9'):
				peaks.append(nodes[row][col])
			#link nodes together
			if(row>0):
				nodes[row][col].link( nodes[row-1][col] )
			if(col>0):
				nodes[row][col].link( nodes[row][col-1] )
			col += 1
		row += 1
	for peak in peaks:
		peak.transit1(peak)
	sum = 0
	for h in heads:
		print(h, end=' ')
		sum += len(h.peaks)
	print('\n')
	print(sum)
	
              
							 
	
def part2():
	print( "Part 2")
	for peak in peaks:
		peak.transit2(1)
	for r in nodes:
		for n in r:
			print(n, end=' ')
		print('\n')
	sum = 0
	for h in heads:
		print(h, end=' ')
		sum += h.paths
	print('\n')
	print(sum)
	
part1()
part2()
	 



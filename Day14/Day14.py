#if(True):
if(False):
	f = open("example.txt", "r")
	wid = 11
	hei = 7
else:
	f = open("input.txt", "r")
	wid = 101
	hei = 103

class robot:	
	def __init__(self, px, py, vx, vy):
		self.px = px
		self.py = py
		self.vx = vx
		self.vy = vy
		self.stepidx = 0
	def step(self, steps = 1):
		self.px = (self.px + self.vx*steps)%wid
		self.py = (self.py + self.vy*steps)%hei
		self.stepidx += steps
		
robots = []
for line in f:
	c1 = line.find(",")
	sp = line[c1:].find(" ")+c1
	eq = line[c1:].find("=")+c1
	c2 = line[eq:].find(",")+eq
	px = int(line[2:c1])
	py = int(line[c1+1:sp])
	vx = int(line[eq+1:c2])
	vy = int(line[c2+1:])
	robots.append( robot(px, py, vx, vy) )

def part1():
	print( "Part 1")
	for r in robots:
		r.step(100)
	#create 2d grid of ints of wid by hei
	grid = [[0 for x in range(wid)] for y in range(hei)]
	#mark robots in grid
	for r in robots:
			grid[r.py][r.px] += 1
	#print grid
	for y in range(hei):
		for x in range(wid):
			print(grid[y][x], end="")
		print('')

	midx = wid//2
	midy = hei//2
	quads = [0,0,0,0]
	for r in robots:
		if r.px < midx and r.py < midy:
			quads[0] += 1
		elif r.px < midx and r.py > midy:
			quads[1] += 1
		elif r.px > midx and r.py < midy:
			quads[2] += 1
		elif r.px > midx and r.py > midy:
			quads[3] += 1
	print(f'Quadrants: {quads}')
	print(f'Safety Factor: {quads[0]*quads[1]*quads[2]*quads[3]}')
							 
	
def part2():
	print( "Part 2")
	start = 7500
	for r in robots:
		r.step(7500)
	for step in range(7500,10000):
		for r in robots:
			r.step()
		#create 2d grid of ints of wid by hei
		rows = [0 for y in range(hei)]
		#mark robots in grid
		grid = [[0 for x in range(wid)] for y in range(hei)]
		#mark robots in grid
		for r in robots:
			grid[r.py][r.px] += 1
			rows[r.py] += 1
		
		#find christmas tree top
		possible = False
		for y in range(2,hei-20):
			if rows[y] < 3:
				continue
			for x in range(10,wid-10):
				if (grid[y][x] > 0 and
					grid[y+1][x-1] > 0 and grid[y+1][x] > 0 and grid[y+1][x] > 0 and
					grid[y+2][x-2] > 0 and grid[y+2][x-1] > 0 and grid[y+2][x] > 0 and grid[y+2][x+1] > 0 and grid[y+2][x+2] > 0):
					possible = True
					break
			if possible:
				break

		#print grid
		if(possible):
			print(f'Step {robots[0].stepidx}')
			for y in range(hei):
				for x in range(wid):
					if(grid[y][x] > 0):
						print('■', end="")
					else:
						print(' ', end="")
				print('')
			input()

	
part1()
part2()
	 



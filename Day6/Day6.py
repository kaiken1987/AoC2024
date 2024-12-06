
#f = open("example.txt", "r")
f = open("input.txt", "r")

grid = [ list(x.strip()) for x in f ]
#create 2d array of len(grid) x len(grid[0])
visited = [ [0 for x in range(0, len(grid[0]))] for y in range(0, len(grid)) ]

startx = -1
starty = -1
#find starting position marked by ^ in grid
for row in range(0, len(grid)):
	if '^' in grid[row]:
		startx = grid[row].index('^')
		starty = row
		break

#direction enums
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def part1():
	print( "Part 1")
	posx = startx
	posy = starty
	dir = NORTH 
	#start walking
	while( posx>=0 and posx<len(grid[0]) and posy>=0 and posy<len(grid) ):
		visited[posy][posx] = 1
		while True:
			newx = posx
			newy = posy
			#move in the direction we are facing
			if dir == NORTH:
				newy-=1
			elif dir == EAST:
				newx+=1
			elif dir == SOUTH:
				newy+=1
			elif dir == WEST:
				newx-=1
			if( newx<0 or newx>=len(grid[0]) or newy<0 or newy>=len(grid) ):
				posx = newx
				posy = newy
				break	
			gridchar = grid[newy][newx]
			#if we can move forward then do so
			if gridchar != '#':
				posx = newx
				posy = newy
				break
			#if we can't move forward then turn right
			dir = (dir+1)%4
	sum1 = 0
	for row in visited:
		sum1+=sum(row)
	
	print( "sum: " + str( sum1 ) )


def testloop( grid, posx, posy, dir )->bool:
	visits = [ [0 for x in range(0, len(grid[0]))] for y in range(0, len(grid)) ]
	while( posx>=0 and posx<len(grid[0]) and posy>=0 and posy<len(grid) ):
		if( visits[posy][posx] & 1<<dir ) != 0 : #we've already visited this cell in this direction
			return True
		visits[posy][posx] = visits[posy][posx] | (1<<dir)
		while True:
			newx = posx
			newy = posy
			#move in the direction we are facing
			if dir == NORTH:
				newy-=1
			elif dir == EAST:
				newx+=1
			elif dir == SOUTH:
				newy+=1
			elif dir == WEST:
				newx-=1
			if( newx<0 or newx>=len(grid[0]) or newy<0 or newy>=len(grid) ):
				return False # exited the grid
			gridchar = grid[newy][newx]
			#if we can move forward then do so
			if gridchar != '#':
				posx = newx
				posy = newy
				break
			#if we can't move forward then turn right
			dir = (dir+1)%4
	return False # exited the grid
							 
	
def part2():
	print( "Part 2")
	posx = startx
	posy = starty
	dir = NORTH 
	sum = 0
	#find starting position marked by ^ in grid
	for row in range(0, len(grid)):
		if '^' in grid[row]:
			posx = grid[row].index('^')
			posy = row
			break
	#test each cell in the grid
	for row in range(0, len(grid)):
		for col in range(0, len(grid[row])):
			if visited[row][col] != 1:
				continue
			if grid[row][col] != '.':
				continue
			#duplicate grid
			grid[row][col] = '#'
			if testloop( grid, posx, posy, dir ):
				#print( "found loop at " + str(col) + " " + str(row) )
				sum += 1
			grid[row][col] = '.'
	print( "sum: " + str( sum ) )
	
part1()
part2()
	 



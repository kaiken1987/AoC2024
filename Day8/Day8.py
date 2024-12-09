
#f = open("example.txt", "r")
f = open("input.txt", "r")

#dictionary of antenna positions
antennas = {}
row=0
col=0

for line in f:
	col=-1
	for x in line.strip():
		col+=1
		if x == '.': continue
		#if x isn't a key in antennas add empty list
		
		if x not in antennas:
			antennas[x] = []
		#add the position of the antenna to the list
		antennas[x].append([col,row])
	row+=1

boundsx = col
boundsy = row

def part1():
	print( "Part 1")
	found = []
	for key in antennas:
		print( key + ": " + str( antennas[key] ) )
		for i in range(0, len(antennas[key])):
			for j in range(i+1, len(antennas[key])):
				dx = antennas[key][i][0] - antennas[key][j][0]
				dy = antennas[key][i][1] - antennas[key][j][1]
				p1x=antennas[key][i][0]-dx*2
				p1y=antennas[key][i][1]-dy*2
				p2x=antennas[key][j][0]+dx*2
				p2y=antennas[key][j][1]+dy*2
				if ( p1x>=0 and p1x<=boundsx and p1y>=0 and p1y<boundsy and not (p1x,p1y) in found ):
					found.append( (p1x,p1y) )
				if ( p2x>=0 and p2x<=boundsx and p2y>=0 and p2y<boundsy and not (p2x,p2y) in found ):
					found.append( (p2x,p2y) )
	found.sort()
	print( found )
	print( "count: " + str(len(found)))
							 
	
def part2():
	print( "Part 2")
	
part1()
part2()
	 



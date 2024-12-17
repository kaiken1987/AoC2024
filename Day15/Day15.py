
#f = open("example.txt", "r")
f = open("input.txt", "r")

boxes = []
walls = []
robot = (0,0)
row = 0

for line in f:
	col  = 0
	if len(line)<3:
		break
	for x in line[:-1]:
		if x == "O":
			boxes.append( (col, row) )
		elif x == "#":
			walls.append( (col, row) )
		elif x == "@":
			robot = (col, row)
		col += 1
	row += 1
	
moves = [ x for x in f.readline().strip()]

def canpushBox( move2, movement ):
	idx = boxes.index( move2 )
	box2 = boxes[idx]
	box2 = (box2[0]+movement[0], box2[1]+movement[1])
	if box2 in walls:
		return False
	if (not box2 in boxes) or canpushBox(box2, movement):
		boxes[idx] = box2
		return True
	return False

def part1():
	print( "Part 1")
	idx = 0
	global robot
	for m in moves:
		movement = [0,0]
		idx += 1
		if m == "^":
			movement[1] = -1
		elif m == "v":
			movement[1] = 1
		elif m == "<":
			movement[0] = -1
		else:#if m == ">":
			movement[0] = 1
		move2 = (movement[0]+robot[0], movement[1]+robot[1])
		if move2 in walls:
			continue
		if (not move2 in boxes) or canpushBox( move2, movement ):
			robot = move2
		print( f'Robot {idx}: {robot}')
	sum = 0
	for b in boxes:
		sum += b[1]*100+b[0]
	print( f'Sum: {sum}')
							 
	
def part2():
	print( "Part 2")
	
part1()
part2()
	 



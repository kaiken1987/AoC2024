
f = open("example.txt", "r")
puzzle = [ ]

def testword( word ) -> bool:
	return word == 'XMAS'

def part1():
	print( "Part 1")
	found = 0
	cnts = [[0,0,0],[0,0,0],[0,0,0]]
	puzzle = [ x.strip() for x in f ]
	
	for row in range(0, len(puzzle)):
		for col in range(0, len(puzzle[row])):
			cnt = 0
			#only do checks if we have an X
			if ( puzzle[row][col] != 'X' ):
				continue
			#upwards
			if( row>=3):
				word = puzzle[row][col]+ puzzle[row-1][col] + puzzle[row-2][col] + puzzle[row-3][col]
				if testword( word ):
					cnts[0][1]+=1
			#downwards
			if (row<=len(puzzle)-4):
				word = puzzle[row][col]+ puzzle[row+1][col] + puzzle[row+2][col] + puzzle[row+3][col]
				if testword( word ):
					cnts[2][1]+=1
			#leftwards
			if( col>=3):
				word = puzzle[row][col]+ puzzle[row][col-1] + puzzle[row][col-2] + puzzle[row][col-3]
				if testword( word ):
					cnts[1][0]+=1
			#rightwards
			if( col<=len(puzzle[row])-4):
				word = puzzle[row][col]+ puzzle[row][col+1] + puzzle[row][col+2] + puzzle[row][col+3]
				if testword( word ):
					cnts[1][2]+=1
			#upleft
			if( row>=3 and col>=3):
				word = puzzle[row][col]+ puzzle[row-1][col-1] + puzzle[row-2][col-2] + puzzle[row-3][col-3]
				if testword( word ):
					cnts[0][0]+=1
			#upright
			if( row>=3 and col<=len(puzzle[row])-4):
				word = puzzle[row][col]+ puzzle[row-1][col+1] + puzzle[row-2][col+2] + puzzle[row-3][col+3]
				if testword( word ):
					cnts[0][2]+=1
			#downleft
			if( row<=len(puzzle)-4 and col>=3):
				word = puzzle[row][col]+ puzzle[row+1][col-1] + puzzle[row+2][col-2] + puzzle[row+3][col-3]
				if testword( word ):
					cnts[2][0]+=1
			#downright
			if( row<=len(puzzle)-4 and col<=len(puzzle[row])-4):
				word = puzzle[row][col]+ puzzle[row+1][col+1] + puzzle[row+2][col+2] + puzzle[row+3][col+3]
				if testword( word ):
					cnts[2][2]+=1
	for cnt in cnts:
		for c in cnt:
			found+=c

	print( "found: " + str( found ) )
							 
	
def part2():
	print( "Part 2")
	f.seek(0)
	found = 0
	puzzle = [ x.strip() for x in f ]
	
	for row in range(1, len(puzzle)-1):
		for col in range(1, len(puzzle[row])-1):
			cnt = 0
			#only do checks if we have an X
			if ( puzzle[row][col] != 'A' ):
				continue
			block = [ [puzzle[row-1][col-1], '.', puzzle[row-1][col+1]],['.','A', ','],[puzzle[row+1][col-1], '.', puzzle[row+1][col+1]] ]
			print( block )
			if ( 
				( (puzzle[row-1][col-1] == 'M' and puzzle[row+1][col+1] == 'S' ) or 
				  (puzzle[row-1][col-1] == 'S' and puzzle[row+1][col+1] == 'M' ) ) and 
				( (puzzle[row-1][col+1] == 'M' and puzzle[row+1][col-1] == 'S' ) or 
				  (puzzle[row-1][col+1] == 'S' and puzzle[row+1][col-1] == 'M' ) ) 
			):
				found += 1
	print( "found: " + str( found ) )
	
part1()
part2()

f = open("input.txt", "r")
part1()
part2()

	 



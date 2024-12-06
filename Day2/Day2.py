
#f = open("example.txt", "r")
f = open("input.txt", "r")

def safeTest( vals ) -> bool:
	if vals[0] == vals[1]:
		return False
	#handle increasing values
	last = vals[0]
	ok = range(1,4)
	if vals[0]<vals[1]:
		for val in vals[1:]:
			if not (val-last) in ok:
				return False
			last = val
	#handle decreasing values
	else:
		for val in vals[1:]:
			if not (last-val) in ok:
				return False
			last = val
	return True

def part1():
	print( "Part 1")
	safeCnt = 0
	for line in f:
		vals = line.split(' ')
		#convert vals to ints
		vals = [ int(x) for x in vals ]
		#if val[0] == val[1] then continue
		if safeTest(vals):
			safeCnt+=1	
	print( "safeCnt: " + str( safeCnt ) )
							 
	

def part2():
	print( "Part 2")
	safeCnt = 0
	for line in f:
		vals = line.split(' ')
		#convert vals to ints
		vals = [ int(x) for x in vals ]
		if safeTest(vals):
			safeCnt+=1	
		else:
			#try popping a single value for vals and retesting
			for i in range(0, len(vals)):
				temp = vals.copy()
				temp.pop(i)
				if safeTest(temp):
					safeCnt+=1
					break

	print( "safeCnt: " + str( safeCnt ) )
	
#part1()
part2()
	 



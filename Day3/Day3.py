import re

#f = open("example.txt", "r")
f = open("input.txt", "r")


def part1():
	print( "Part 1")
	sum = 0
	data = f.read()
	#use regex to find mul\((\d),(\d)\)
	matches = re.findall( r'mul\((\d+),(\d+)\)', data )
	for match in matches:
		sum += int(match[0])*int(match[1])
		
	print( "sum: " + str( sum ) )
							 
	
def part2():
	print( "Part 2")
	sum = 0
	#rewind file f
	f.seek(0)
	data = f.read()
	dos = data.split('do()')
	for do in dos:
		#remove anything after don't()
		idx = do.find("don't()")
		if idx >0:
			do = do[:idx]
		#use regex to find mul\((\d),(\d)\)
		matches = re.findall( r'mul\((\d+),(\d+)\)', do )
		for match in matches:
			sum += int(match[0])*int(match[1])
	print( "sum: " + str( sum ) )
	
part1()
part2()
	 



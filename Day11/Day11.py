from ast import Global
import math
from unittest import skip

#f = open("example.txt", "r")
f = open("input.txt", "r")


def part1():
	print( "Part 1")
	stones = [ int(x) for x in f.readline().strip().split() ]
	for i in range(25):
		#procss stones
		newstones = []
		for stone in stones:
			if(stone == 0):
				newstones.append(1)
			else:
				#get number of digits in stone
				digits = int(math.floor( math.log10(stone)+1 )) 
				#if even
				if( digits & 1 == 0 ): 
					fac = math.pow( 10, (digits>>1) )
					newstones.append( int(stone / fac) )
					newstones.append( int(stone % fac) )
				else:
					newstones.append( stone * 2024 )
		stones = newstones
		print( f"{i}\n" )

	print(f"Total paths: {len(stones)}")


def part2():
	print( "Part 2")
	global stones
	for i in range(25,75):
		#procss stones
		newstones = []
		for stone in stones:
			if(stone == 0):
				newstones.append(1)
			else:
				#get number of digits in stone
				digits = int(math.floor( math.log10(stone)+1 )) 
				#if even
				if( digits & 1 == 0 ): 
					fac = math.pow( 10, (digits>>1) )
					newstones.append( int(stone / fac) )
					newstones.append( int(stone % fac) )
				else:
					newstones.append( stone * 2024 )
		stones = newstones
		print( f"{i}\n" )

	print(f"Total paths: {len(stones)}")
	
part1()
part2()
	 


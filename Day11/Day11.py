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
		#print( f"{i}: {stones}\n" )

	print(f"Total stones: {len(stones)}")


def part2():
	print( "Part 2")
	f.seek(0)
	#list of stones and stone count
	stones = [ (int(x),1) for x in f.readline().strip().split() ]
	for i in range(75):
		#procss stones
		newstones = []
		for stone in stones:
			if(stone[0] == 0):
				newstones.append((1,stone[1]))
			else:
				#get number of digits in stone
				digits = int(math.floor( math.log10(stone[0])+1 )) 
				#if even
				if( digits & 1 == 0 ): 
					fac = math.pow( 10, (digits>>1) )
					newstones.append( (int(stone[0] / fac),stone[1]) )
					newstones.append( (int(stone[0] % fac),stone[1]) )
				else:
					newstones.append( (stone[0] * 2024,stone[1]) )
		#sort based on stone value
		newstones.sort( key = lambda x: x[0])
		stones.clear()
		for n in newstones:
			if(len(stones) ==0 or n[0]!=stones[-1][0]):
				stones.append(n)
			else:
				stones[-1] = (stones[-1][0],stones[-1][1]+n[1])
		print( f"{i}\n" )
	sum = 0
	for stone in stones:
		sum += stone[1]

	print(f"Total stones: {sum}")
	
part1()
part2()
	 


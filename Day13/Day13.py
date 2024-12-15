
import math
from msvcrt import SEM_NOALIGNMENTFAULTEXCEPT


#f = open("example.txt", "r")
f = open("input.txt", "r")

#extract a b values from example Button A: X+a, Y+b
def parse( button ):
	x = button.find("X")+2
	comma = button.find(",")
	y = button.find("Y")+2
	return (int(button[x:comma]), int(button[y:]))

machines = []
while( True ):
	ButtonA = f.readline()
	ButtonB = f.readline()
	Prize = f.readline()
	f.readline() #skip blank line
	if not ButtonA or not ButtonB or not Prize:
		break
	btnA = parse(ButtonA)
	btnB = parse(ButtonB)
	prize = parse(Prize)
	machine = { "btnA": btnA, "btnB": btnB, "prize": prize }
	machines.append(machine)

#All solutions

def part1():
	print( "Part 1")
	costs = 0
	for machine in machines:
		btnA = machine["btnA"]
		btnB = machine["btnB"]
		prize = machine["prize"]
		#int division to get max number of presses
		pressA = (prize[0]//btnA[0])
		if pressA>100:
			pressA = 100
		#fine multples of pressA and pressB that sum prize
		solutions = []
		while pressA>=0:
			while( (prize[0]-(pressA*btnA[0])) % btnB[0] != 0 and pressA>=0):
				pressA -= 1							 
			if pressA>=0:
				pressB = (prize[0]-(pressA*btnA[0])) // btnB[0]
				if( prize[1] == pressB*btnB[1] + pressA*btnA[1] ):
					solutions.append( (pressA, pressB) )
				pressA -= 1
		if len(solutions) > 0:
			#Find best solution if A presses cost 3 times more than B presses
			best = 2e30
			for s in solutions:
				if s[0]*3+s[1] < best:
					best = s[0]*3+s[1]
					machine["best"] = (s[0], s[1] )
			costs += best
	print (f'Total cost: {costs}')
			
def gcd(a,b):
			if b == 0:
				return a
			return gcd(b, a%b)

#test if number is natural number
def test( a ) -> bool:	
	return a>=0 and abs( a - int(a+0.0001) ) < 0.0001
	
	
def part2():
	print( "Part 2")
	costs = 0
	for machine in machines:
		btnA = machine["btnA"]
		btnB = machine["btnB"]
		prize = machine["prize"]
		offset = 10000000000000
		prize = (prize[0]+offset, prize[1]+offset)
		A = [[btnA[0], btnB[0]], [btnA[1], btnB[1]]]
		B = [prize[0], prize[1]]
		#Solve for Ax = B
		det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
		if det == 0:
			print("No solution")
			continue
		invdet = 1/det
		#inverse of A
		invA = [[A[1][1]*invdet, -A[0][1]*invdet], [-A[1][0]*invdet, A[0][0]*invdet]]
		#x = invA*B
		x = [invA[0][0]*B[0]+invA[0][1]*B[1], invA[1][0]*B[0]+invA[1][1]*B[1]]
		#x = [pressA, pressB]
		if test(x[0]) and test(x[1]):
			costs += x[0]*3+x[1]
			print(f'Press A: {x[0]}, Press B: {x[1]}')
		else:
			print("No solution")
	print (f'Total cost: {costs}')
	
part1()
part2()
	 



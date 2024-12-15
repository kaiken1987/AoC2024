
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
	#until end of file
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
			costs += best
	print (f'Total cost: {costs}')
			
	
def part2():
	print( "Part 2")
	
part1()
part2()
	 



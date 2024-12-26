
#f = open("example.txt", "r")
f = open("input.txt", "r")
state = { 'A': 0, 'B': 0, 'C': 0, 'Stack': [], 'idx': 0 }

def loadState( f ):
	state['idx'] = 0
	state['A'] = int(f.readline()[12:])
	state['B'] = int(f.readline()[12:])
	state['C'] = int(f.readline()[12:])
	f.readline()
	prog = f.readline().strip()[9:].split(",")
	state['Stack'] = [int(x) for x in prog]


def getCombo( arg ):
	if( arg == 4 ):
		return state['A']
	elif( arg == 5 ):
		return state['B']
	elif( arg == 6 ):
		return state['C']
	elif( arg >= 7 ):
		print("Error: arg out of range")
		return arg
	else:
		return arg

def part1():
	print( "Part 1")

	loadState(f)
	out = ''
	while(True):
		if( state['idx'] >= len(state['Stack']) or state['idx'] < 0):
			break
		ins = state['Stack'][state['idx']]
		arg = state['Stack'][state['idx']+1]
		cmb = getCombo(arg)
		if( ins == 0 ):
			#div A=A/(1 lsh combo)
			state['A'] = state['A'] // (1<<cmb)
		elif( ins == 1 ):
			#XOR B=B XOR arg
			state['B'] = state['B'] ^ arg
		elif( ins == 2 ):
			#B = combo % 7
			state['B'] = (cmb % 8)
		elif( ins == 3 ):
			#jump not 0
			if( state['A'] != 0 ):
				state['idx'] = arg
				continue
		elif( ins == 4 ):
			#XOR B=B XOR C
			state['B'] = state['B'] ^ state['C']
		elif( ins == 5 ):
			#output combo & 7
			out += str(cmb % 8) + ','
		elif( ins == 6 ):
			#div B=A/(1 lsh combo)
			state['B'] = state['A'] // (1<<cmb)
		elif( ins == 7 ):
			#div C=A/(1 lsh combo)
			state['C'] = state['A'] // (1<<cmb)
		state['idx'] += 2
	print(out)
	print(state)
	print('\n')




							 
	
def part2():
	print( "Part 2")

#until end of file f
while(True):
	try:
		part1()
	except:
		break
part2()
	 



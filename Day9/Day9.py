
#f = open("example.txt", "r")
f = open("input.txt", "r")

blocks = [ int(x) for x in f.readline() ]
memlen = sum(blocks)

def part1():
	print( "Part 1")
	memory = [-1 for x in range(0, memlen)]
	memindex = 0
	fileid = 0
	free = True
	#initialize memory
	for block in blocks:
		free = not free
		if(free):
			memindex+=block
			continue
		for i in range(0, block):
			memory[memindex+i] = fileid
		memindex+=block
		fileid+=1

	freeidx = 0
	fileidx = -1
	while(freeidx<memlen+fileidx):
		if(memory[freeidx]!=-1): 
			freeidx+=1 
		elif(memory[fileidx]==-1): 
			fileidx-=1 
		else:
			memory[freeidx] = memory[fileidx]
			memory[fileidx] = -1
			freeidx+=1
			fileidx-=1
	
	chksm = 0
	for i in range(len(memory)):
		m = memory[i]
		if(m!=-1):
			chksm+=m*i
	print( "chksm: " + str( chksm ) )



							 
	
def part2():
	print( "Part 2")
	
part1()
part2()
	 



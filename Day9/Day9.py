
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
	frees = []
	files = []
	free = True
	memindex = 0
	fileid = 0
	#find free and file blocks
	for block in blocks:
		free = not free
		if(free):
			frees.append((memindex,block))
		else:
			files.append((memindex,block,fileid))
			fileid+=1
		memindex+=block

	#compact used blocks
	for i in range(len(files)-1, -1, -1):
		pos = files[i][0]
		sz = files[i][1]
		for j in range(0, len(frees)):
			if frees[j][0]>pos:
				break
			if frees[j][1] == sz:
				files[i] = (frees[j][0],files[i][1],files[i][2])
				frees.remove(frees[j])
				frees.append((pos,sz))
				break
			elif( frees[j][1] > sz ):
				files[i] = (frees[j][0],files[i][1],files[i][2])				
				frees[j] = (frees[j][0]+sz,frees[j][1]-sz)
				frees.append((pos,sz))
				break
				
	chksm = 0
	for i in range(len(files)):
		pos = files[i][0]
		sz = files[i][1]
		id = files[i][2]
		chksm+=id*(sz*pos+sz*(sz-1)/2)
	print( "chksm: " + str( chksm ) )

	
#part1()
part2()
	 



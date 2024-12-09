
#f = open("example.txt", "r")
f = open("input.txt", "r")

def cat(x,y)->int:
	fac = 10
	while(True):
		if(y<fac):
			return x*fac+y
		fac*=10

def add(x,y)->int:
	return x+y
def mul(x,y)->int:
	return x*y

lines = []
for line in f:
	limit, line = line.split(": ")
	limit = int(limit)
	lines.append([limit,line])
	

def calc(vals, ops, limit) -> list:
	if(len(vals)==2):
		result = []
		for op in ops:
			result.append(op(vals[0], vals[1]))
		return result 
	else:
		ret = calc(vals[:-1], ops, limit)
		val = vals[-1]
		result = []
		for x in ret:
			for op in ops:
				y = op(x,val)
				if y<=limit:
					result.append(op(x,val) )
		return result


def part1():
	print( "Part 1")
	cnt = 0
	sum = 0
	ops = [add, mul]
	for line in lines:
		vals = [int(x) for x in line[1].split()]
		limit = line[0]
		ret = calc(vals, ops, limit)
		for x in ret:
			if x == limit:
				sum+=x
				cnt+=1
				break
	
	print( "cnt: " + str( cnt ) )
	print( "sum: " + str( sum ) )
							 
	
def part2():
	print( "Part 2")
	cnt = 0
	sum = 0
	ops = [add, mul, cat]
	for line in lines:
		vals = [int(x) for x in line[1].split()]
		limit = line[0]
		ret = calc(vals, ops, limit)
		for x in ret:
			if x == limit:
				sum+=x
				cnt+=1
				break
	
	print( "cnt: " + str( cnt ) )
	print( "sum: " + str( sum ) )
	
part1()
part2()
	 




f = open("example.txt", "r")
#f = open("input.txt", "r")

Def calc(vals) -> list:
    if(len(vals)==2):
        return [vals[0]+vals[1], vals[0]*vals[1]] 
    else:
        ret = calc(vals[1:0])
        

def part1():
	print( "Part 1")
							 
	
def part2():
	print( "Part 2")
	
part1()
part2()
	 




#f = open("example.txt", "r")
f = open("input.txt", "r")
input = [ x.strip() for x in f ]
idx = input.index('')
rules = input[:idx]
pages = input[idx+1:]
pages = [p.split(',') for p in pages]
sum1 = 0
def part1()->int:
	print( "Part 1")
	sum = 0
	for page in pages:
		valid = True
		for rule in rules:
			first, second = rule.split('|')
			#find first value if throws continue
			if not first in page:
				continue
			idxf = page.index(first)
			if not second in page:
				continue
			idxs = page.index(second)
			if idxf>idxs:
				valid = False
				break
		if( valid ):
			sum+=int(page[int(len(page)/2)])
	print( "sum: " + str( sum ) )
	return sum
	
def part2(offset:int):
	print( "Part 2")
	sum = -offset
	for page in pages:
		valid = False
		while(not valid):
			valid = True
			for rule in rules:
				first, second = rule.split('|')
				#find first value if throws continue
				if not first in page:
					continue
				idxf = page.index(first)
				if not second in page:
					continue
				idxs = page.index(second)
				if idxf<idxs:
					continue
				#page order is invalid swap pages
				page[idxs] = first
				page[idxf] = second
				valid = False
				break
			print( page )
			
		if( valid ):
			sum+=int(page[int(len(page)/2)])
	print( "sum: " + str( sum ) )
	
sum1= part1()
part2(sum1)
	 



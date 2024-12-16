import curses

f = open("example.txt", "r")
#f = open("input.txt", "r")

#convert file characters to 2d array

plots = [ list(x.strip()) for x in f.readlines() ]
#convert from strings to chars
for i in range(len(plots)):
	for j in range(len(plots[i])):
		plots[i][j] = ord(plots[i][j])

def traverse(x, y):
	plant = plots[y][x]
	marked = plots[y][x]-ord('A')+ord('a')
	plots[y][x] = marked
	parim = 0
	area = 1
	if y>0:
		#above
		if plots[y-1][x] == plant:
			a,p = traverse(x, y-1)
			area += a
			parim += p
		elif plots[y-1][x] != marked:
			parim += 1
	else:
		parim += 1
	if y<len(plots)-1:
		#below
		if plots[y+1][x] == plant:
			a,p = traverse(x, y+1)
			area += a
			parim += p
		elif plots[y+1][x] != marked:
			parim += 1
	else:
		parim += 1
				
	#left
	if x>0:
		if plots[y][x-1] == plant:
			a,p = traverse(x-1, y)
			area += a
			parim += p
		elif plots[y][x-1] != marked:
			parim += 1
	else:
		parim += 1
	#right
	if x<len(plots[y])-1:
		if plots[y][x+1] == plant:
			a,p = traverse(x+1, y)
			area += a
			parim += p
		elif plots[y][x+1] != marked:
			parim += 1
	else:
		parim += 1
	return area, parim



def part1():
	print( "Part 1")
	#find each set of plots that are connected
	sum = 0
	for i in range(len(plots)):		
		for j in range(len(plots[i])):
			if plots[i][j] in range(ord('a'),ord('z')+1):
				continue
			area, parim = traverse(j, i)
			print(area, parim)
			sum += area*parim
	print(sum)
			
	
def traverse2(x, y):
	plant = plots[y][x]
	marked = plots[y][x]-ord('a')+ord('A')
	plots[y][x] = marked
	parim = []
	area = [(x,y)]
	if y>0:
		#above
		if plots[y-1][x] == plant:
			a,p = traverse2(x, y-1)
			area += a
			parim += p
		elif plots[y-1][x] != marked:
			parim.append((x+0.5,y))
	else:
		parim.append((x+0.5,y))
	if y<len(plots)-1:
		#below
		if plots[y+1][x] == plant:
			a,p = traverse2(x, y+1)
			area += a
			parim += p
		elif plots[y+1][x] != marked:
			parim.append((x+0.5,y+1))
	else:
		parim.append((x+0.5,y+1))
	#left
	if x>0:
		if plots[y][x-1] == plant:
			a,p = traverse2(x-1, y)
			area += a
			parim += p
		elif plots[y][x-1] != marked:
			parim.append((x,y+0.5))
	else:
		parim.append((x,y+0.5))
	#right
	if x<len(plots[y])-1:
		if plots[y][x+1] == plant:
			a,p = traverse2(x+1, y)
			area += a
			parim += p
		elif plots[y][x+1] != marked:
			parim.append((x+1,y+0.5))
	else:
		parim.append((x+1,y+0.5))
	return area, parim
				

def part2():
	wid = len(plots[0])*2+1
	hei = len(plots)*2+2
	stdscr = curses.initscr()
	win = curses.newwin(hei, wid, 0, 0)
	print( "Part 2")
	sum = 0
	for i in range(len(plots)):		
		for j in range(len(plots[i])):
			if plots[i][j] in range(ord('A'),ord('Z')+1):
				continue
			area, parim = traverse2(j, i)
			#convert plots[i][j] from ord to str
			char = chr(plots[i][j])
			for a in area:
				win.addch(a[0]*2+1, a[1]*2+1, char)
			for p in parim:
 				win.addch(int(p[0]*2), int(p[1]*2), '☺')
			sum += len(area)*len(parim)
			win.refresh()
	win.addstr(hei-1,1,str(sum))
	win.getch()
	
part1()
part2()
	 



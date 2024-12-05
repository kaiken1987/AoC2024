f = open("input.txt", "r")
#f = open("example.txt", "r")


list1 =[]
list2 =[]

def part1():
   print( "Part 1")
   #create 2 lists of numbers
   dif = 0
   #load in values from file using '   ' as a delimiter
   for line in f:
      val1, val2 = line.split('   ')
      list1.append( int(val1) )
      list2.append( int(val2) )
   #sort the lists
   list1.sort()
   list2.sort()
   #loop through the lists
   for val1, val2 in zip(list1, list2):
      #compare the two lists
      dif += abs( int(val1) - int(val2) )      
   print( "Diff: " + str( dif ) )
      
   
def part2():
   print( "Part 2")
   #count the occurance of each number in list1 in list2
   sum = 0
   for val in list1:
      cnt = list2.count(val)     
      sum+=val*cnt
   print( "similarity: " + str( sum ) )


   
part1()
part2()
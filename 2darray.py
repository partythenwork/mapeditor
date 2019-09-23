import random
import pprint

WIDTH = 10
HEIGHT = 5

#create the 2d array and assign all values to integer 0
map = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
#print out the 2d array to verify contents
pprint.pprint(map)
print()

#now loop through map and assign values into each coordinate
y=0
for row in map:
	x=0
	for element in row:
		value = str(random.randrange(0,20))
		if len(value)<2:
			value = '0'+value
		map[y][x] = value
		x+=1
	y+=1
	
pprint.pprint(map)
import random
import pprint

WIDTH = 10
HEIGHT = 5

#this is a study to populate a 2d array and assign random values into the array.
#the values are going to be from 0 to 20, but if the value is less than 10 then we 
#add a 0 in front to make sure that there are two digits, but the values will have
#to be stored as characters instead of an integer

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

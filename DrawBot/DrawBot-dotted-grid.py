### Drawing with DrawBot ###

# Grid (10 x 10) of blue dots

distance = 100
fill(0, 0, 0.75)
for x in range(0, 10):
	for y in range(0, 10):
	    oval(x*distance + distance, y*distance + distance, 10, 10)

### Drawing with DrawBot ###

# Parametric grid of blue dots, randomized size and colour

# parameters
number = 10 # number of dots in one row/column
minSize = 10 # size of a dot
maxSize = 20
step = 30
margin = 50

# size of the canvas
size(2 * margin + (number - 1) * step, 2 * margin + (number - 1) * step)


# dots
for x in range(margin, number * step + margin, step):
    for y in range(margin, number * step + margin, step):
        r = random()
        g = random()
        b = random()
        size = randint(minSize, maxSize)
        fill(r, g, b)
        oval(x - size/2, y - size/2, size, size)

### Drawing with DrawBot ###

# Random circles

HEIGHT = WIDTH = 400

for i in range(100):
    x = randint(0, HEIGHT)
    y = randint(0, WIDTH)
    r = randint(50, 100)
    oval(x, y, r, r)


### Iteration ###

# iteration over list items
A = [0,1,2, "xp3"]
for i in A:
	print i

# iteration over string
for char in "Monotype":
	print char

# iteration over range of integers
for i in range(50):
	print i**2 # power of 2

for i in range(2,8):
	print i**2 # power of 2

# iteration using list/string length
MT = "Monotype"
for i, char in enumerate(MT):
	print i, char

# iteration over dictionary
unicodes = {"space":"0020", "A":"0041", "f":"0066", "Agrave":"00C0"}
for glName, glUnicode in unicodes.items():
	print '"%s" has unicode %d (in decimal).' % (glName, int(glUnicode, 16))

# with condition included
unicodes = {"space":"0020", "A":"0041", "f":"0066", "Agrave":"00C0"}
for glName, glUnicode in unicodes.items():
	if int(glUnicode, 16) > 65:
		print '"%s" has greater unicode than A.' % glName
	elif int(glUnicode, 16) < 65:
		print '"%s"" has smaller unicode than A.' % glName
	else:
		print '"%s" is A.' % glName

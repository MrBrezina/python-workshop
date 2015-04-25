# Define function to decompose glyph name to name and suffix
# if name does not have suffix (separated by period) return
# empty suffix
# the function should return tuple (name, suffix)
# examples:	"Agrave.sc" -> ("Agrave", "sc")
#			"ampersand.alt" -> ("ampersand", "alt")
#			"space" -> ("space")
# hint: you can use string method find()

# header:
# def getNameAndSuffix(name):
# returns tuple










# long solution
def getNameAndSuffix(name):
	"""
	Returns tuple of name and its suffix.
	"""

	index = name.find(".")
	if index != -1:
		# there is a suffix
		shortname = name[:index]
		suffix = name[index+1:]
	else:
		# there is no period, no suffix
		shortname = name
		suffix = ""
	return (shortname, suffix)


# shorter solution
def getNameAndSuffix(name):
	"""
	Returns tuple of name and its suffix.
	"""
	index = name.find(".")
	if index != -1:
		# there is a suffix
		return name[:index], name[index+1:]
	else:
		# there is no period, no suffix
		return name, ""


# another solution, using split() and join()
def getNameAndSuffix(name):
	"""
	Returns tuple of name and its suffix.
	"""

	x = name.split(".")
	if len(x) == 1: # if there is not any suffix add empty record
		x.append("")
	
	suffixes = ".".join(x[1:])	# there may be more periods inthe name
	return (x[0], suffixes) # convert list to tuple

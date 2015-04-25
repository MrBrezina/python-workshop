# Define two functions
# one to fill glyph dictionary with data
# and the other to print formatted
# glyph data to console
# if isComposite is true the glyph has a list of components
# that is list of component names

# header:
# def getGlyph(name, uni, isComposite, components):
# returns glyph record
# def printGlyph(glyphDict):
# return nothing

# format of glyph record
glyphDict = {
	"name":"",
	"unicode":0,
	"isComposite":False,
	"components":[]
}










# solution
def getGlyph(name, uni, isComposite, components):
	"""
	Build glyph dictionary.
	"""

	glyph = {}
	glyph["name"] = name
	glyph["unicode"] = uni
	glyph["isComposite"] = isComposite
	glyph["components"] = components
	
	return glyph

def printGlyph(glyphDict):
	"""
	Print glyph dictionary formatted.
	"""
	
	print "Glyph ", glyphDict["name"]
	print "	", glyph["unicode"]
	if isComposite:
		print "Has components: ", ", ".join(components)

# Define a function that revereses
# a language dictionary
# expect that all values can work as
# keys and that they are unique

# header:
# def reverseDict(dic):
# returns dictionary

# dictionary
cs_en = {
	"ahoj":"heya",
	"nashledanou":"goodbye",
	"na zdravi":"cheers",
	"jedna":"one",
	"dva":"two",
	"tri":"three"
}










# solution
def reverseDict(dic):
	"""
	Function reverses dictionary to be indexed by its values,
	keys become values.
	"""

	dic_rev = {}
	for key, item in dic.items():
		dic_rev[item] = key

	return dic_rev


# short solution
def reverseDict(dic):
	"""
	Function reverses dictionary to be indexed by its values,
	keys become values.
	"""

	return dict(zip(dic.values(), dic.keys()))


### String ###

myString = "Test string"
myString2 = 'Test string'
longString = """
	this is often
	used for documentation
	or just anywhere where more lines
	are needed
"""
longString2 = '''
	another way
	to write the same
'''

myNewString = "Hi in Czech is 'Ahoj'"
myNewString = myNewString + "!"	# concatenation
myNewString += "!!"
print myNewString
repetition = "ten" * 10	# repeat 10x
print repetition
myNewString[0]			# first character
print repetition[10]	# eleventh character
print repetition[0:3]	# three characters, from index 0 to index 3
print repetition[2:4]	# two characters,from index 0 to index 4
print repetition[:6]	# first six characters
print myNewString[-1]	# last character
print myNewString[5:]	# only characters from sixth on
print len(myNewString)	# string length

# comparisons
print "abcd" > "abc"	# is longer
print "abcd" < "abce"	# is same, but comparing alphabetically
a = "password"			# assignment
print a == "password"	# equality test

# case conversions
name = "dan"
surname = "RhaTigan"
print name.capitalize()
print surname.upper()
print surname.lower()
print name.capitalize() + " " + surname.lower().capitalize()

# find & replace
text = "When you are finished changing, you are finished. (Ben Franklin)"
print text
print text.find("you") 				# index of the first occurrence
text = text.replace("you", "we")	# substitutes second argument for first
print text

# content tests
print "textual56".isdigit()
print "textual56".isalpha()
print "56".isdigit()


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
repetition = "ten" * 10			# repeat 10x
repetition
myNewString[0]	# first character
repetition[10]	# eleventh character
repetition[0:3]	# three characters, from index 0 to index 3 [excluded]
repetition[2:4]	# two characters,from index 0 to index 4 [excluded]
repetition[:6]	# first six characters
myString[-1]	# last character
myString[5:]	# only characters from sixth on
len(myString)	# string length

# comparisons
"abcd" > "abc"	# is longer
"abcd" < "abce"	# is same, but comparing alphabetically
a = "password"	# assignment
a == "password"	# equality test

# case conversions
name = "dan"
surname = "RhaTigan"
name.capitalize()
surname.upper()
surname.lower()
name.capitalize() + " " + surname.lower().capitalize()

# find & replace
text = "When you are finished changing, you are finished. (Ben Franklin)"
text.find("you") 			# index of the first occurence
text.replace("you", "we")	# substitutes second argument for first

# content tests
"textual56".isdigit()
"textual56".isalpha()
"56".isdigit()

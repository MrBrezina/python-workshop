# simple example to demonstrate
# basic Python syntax elements
# these are comments

a = 25	# assignment, intializing variable a
b = 3	# assignment, intializing variable b

if a > 20:		# conditional statement if
	# starting indented block
	a = 15	# assignment
	b = 4
	print "a is bigger than 20"	# print statement
	# end of indented block

else:
	# another indented block
	a = a + b + 1	# assigning result of an expression
	b = a - 5		# assigning result of an expression
	print "a is smaller than 20"
	# end of indented block

print a	# print statement
print b

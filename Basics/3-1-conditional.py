
### Conditional ###

# simple conditional
number = 8
if number % 2:
	print "The number is odd."
else:
	print "The number is even."

# zero test before division
num = 20
dnom = -3.7
if dnom != 0:
	print num/dnom

# without else, but with elif
s = "00041"
print s, " is "
if len(s) > 4:
	print "too long"
elif len(s) < 4:
	print "too short."

# with elif and else
s = "00041"
print s, " is "
if len(s) > 4:
	print "too long"
elif len(s) < 4:
	print "too short."
else:
	print "is accurate!"

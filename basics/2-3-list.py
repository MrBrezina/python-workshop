
### List ###

# list of numbers

x = [1,2,3,5,4]
print x

x.append(0)
print x

print x[1]
print x[0]
print x[2:]
print x[:-1]
print x[2:4]

print x
x.sort()
print x

# list of strings

y = ["John", "Jane", "Charlene", "Paul"]
print y
y.reverse()
print y
print sorted(y)
print y

# list with mixed content

a = []		# empty list
a.append(0)	# append item to a list
a.append(-2.7)
a.append("text")
b = a				# just reference!
b.append([1,2,3])	# appending list
b.append(True)
print a
print a[3][1]		# refering to the sublist
print a[3]  		# refering to the sublist
print len(a)		# length
print len(a[2])
print 3 in a		# test for presence in the list
print 3 in a[3]	# presence in the sub-list
del a[0]	# delete first item
del a[1:]	# delete all, but first item

# create a duplicate copy of a list, not just link

c = list(a)

# extending vs. appending

print a
a.append([1,2]) # append a list
print a
print c
c.extend([1,2]) # append contents of a list
print c

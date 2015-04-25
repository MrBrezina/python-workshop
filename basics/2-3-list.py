
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

# get length of a list
print len(x)
print len(x[2:4])

# sort list
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

a = []		        # empty list
a.append(0)	        # append item to a list
a.append(-2.7)
a.append("text")
b = a				# just a reference!
b.append([1,2,3])	# appending list
b.append(True)
print a
print a[3][1]		# referring to the sublist
print a[3]  		# referring to the sublist
print len(a)		# length
print "here", a
print len(a[3])
print 3 in a		# test for presence of an item in the list
print "text" in a
print 3 in a[3]     # presence in the sub-list
print [1,2,3] in a
print sorted([3,2,1]) in a
del a[0]            # delete first item
print a
del a[1:]           # delete all, but first item
print a

# create a duplicate copy of a list, not just link

c = list(a)

# extending vs. appending

print a
a.append([1,2]) # append a list
print a
print c
c.extend([1,2]) # append contents of a list
print c

print a
a.insert(1, 76) # first goes the index, second is the item
print a

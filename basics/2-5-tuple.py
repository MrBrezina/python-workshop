
### Tuple ###

record = ()		# empty tuple
record = ("Gerry")	# error
record = ("Gerry", )	# one-item tuple (the comma is necessary)
record = ("Gerry", "Leonidas", "senior lecturer")
record[1].upper()
record += ("Ian",)
record[1] = "David"		# error, tuples are immutable
record[0:3]*3
record[-1] + record[-3]	# result is string
record[0:2] + record[-1]	# error
first, second = record[0:2]	# sub-tuple is unpacked to two variables
first
second
len(record)	# the length of tuple

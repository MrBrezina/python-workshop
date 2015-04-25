
### Tuple ###

record = ()                 # empty tuple
record = ("Gerry")          # error
record = ("Gerry", )        # one-item tuple (the comma is necessary)
record = ("Gerry", "Leonidas", "senior lecturer")
print record[1].upper()
record += ("Ian",)          # extending tuple
print record
record[1] = "David"         # error, tuples are immutable (items cannot be changed directly)
print record[0:3]*3
print record[-1] + record[-3]	# result is string
print record[0:2] + record[-1]	# error, second operand is a string
first, second = record[0:2]     # sub-tuple is unpacked to two variables
print first
print second
print len(record)               # the length of a tuple

record = ("Gerasimos", )+record[1:]
print record

# Define function to convert decimal unicode integer
# to hexadecimal number represented as four-character string
# hint: use hex() function
# test on different values
# different numbers give strings of different length
# there are various solutions how to add missing leading zeros
# use .upper() to convert the string to uppercase only

# header:
# def unicode2string(unicodeValue):
# retruns string










# long solution
def unicode2string(unicodeValue):
	"""
	Convert unicode value to hexadecimal
	string of exactly 4 characters.
	"""

	hexcode = hex(unicodeValue)
	hexcode = hexcode[2:]
	hexcode = "0000" + hexcode
	hexcode = hexcode[-4:]
	hexcode = hexcode.upper()
	return hexcode


# very short solution
def unicode2string(unicodeValue):
	"""
	Convert unicode value to hexadecimal
	string of exactly 4 characters.
	"""
	
	return ("000"+hex(unicodeValue)[2:])[-4:].upper()

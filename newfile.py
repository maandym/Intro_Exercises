""" 1.     takes an integer value and returns True if k is even, and  False otherwise.  However, your function cannot use the multiplication, modulo, or division operators 
"""


# def isOdd(integer):
# 	integer=bin(integer)
# 	print integer[-1]
# 	print type(integer[-1])
# 	if int(integer[-1])==1:
# 		print "Integer is odd!"
# 	else:
# 		print "Integer is even."



# isOdd(2)
# isOdd(3)
# isOdd(4)
# isOdd(5)



integer=int(raw_input("Please input an integer or go away.  "))


def isOdd(integer):
	integer=bin(integer)
	if int(integer[-1])==1:
		print "Integer is odd!"
	else:
		print "Integer is even."


isOdd(2)
isOdd(integer)
isOdd(4)
isOdd(123)
isOdd(5)

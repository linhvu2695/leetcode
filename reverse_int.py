''''
	Given a signed 32-bit integer x, return x with its digits reversed. 
	If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

import sys

def reverse_int1(x):
	#remove negative sign since Python modulo works differently
	neg = False
	if x < 0:
		x = -x
		neg = True

	#pop the last digit of x and stack it to rev
	rev = 0
	while x != 0:
		pop = x % 10
		x = x // 10
		if (rev > sys.maxsize/10) | (rev < (-sys.maxsize-1)/10):
			return 0
		rev = rev*10 + pop
	
	if neg == False:	
		return rev
	else:
		return -rev

def reverse_int2(x):
	#remove negative sign
	neg = False
	if x < 0:
		x = -x
		neg = True

	x_string = str(x)
	rev = int(x_string[::-1])
	
	if neg == False:
		return rev
	else:
		return -rev


def main():
	print(reverse_int1(-120))
	print(reverse_int2(-120))

if __name__ == '__main__':
	main()
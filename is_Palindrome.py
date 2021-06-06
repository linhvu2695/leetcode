'''
	Given an integer x, return true if x is palindrome integer.
'''


def isPalindrome(x):
	if x < 0:
		return False

	rev = 0
	while x > rev:
		pop = x % 10
		rev = rev*10 + pop
		x = x//10

	return ((x==rev) | (x==rev//10))




def main():
	print(isPalindrome(12321))

if __name__ == '__main__':
	main()
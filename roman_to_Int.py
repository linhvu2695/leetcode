'''
	Given a roman numeral, convert it to an integer.
'''

def romantoInt(numeral):
	d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	val = 0

	for i in range(0, len(numeral)):
		if i+1 < len(numeral):
			#add if  s[i] >= s[i+1], otherwise subtract
			if d[numeral[i]] >= d[numeral[i+1]]:
				val += d[numeral[i]]
			else:
				val -= d[numeral[i]]
		else:
			val += d[numeral[i]]

	return val


def main():
	numeral = 'MCMXCIV'
	print(romantoInt(numeral))

if __name__ == '__main__':
	main()
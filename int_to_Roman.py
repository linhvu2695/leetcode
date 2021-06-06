'''
	Given a integer, convert it to a roman numeral.
'''

def inttoRoman(x):
	d ={1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
	d_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	ans = ''

	if x==0:
		return 'Roman numerals dont have 0'
	else:
		for i in d_list:
			if x != 0:
				quotient = x // i
				if quotient != 0:
					for j in range(0, quotient):
						ans = ans + str(d[i])
			x = x%i

	return ans

def main():
	num = 1994
	print(inttoRoman(num))

if __name__ == '__main__':
	main()
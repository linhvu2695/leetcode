'''
	Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
	Determine if the input string is valid.
'''

def isValid(s):
	s = s.replace(' ','')

	d = {'(': ')', '[': ']', '{': '}'}

	p_list = []

	#use a stack to push opening brackets ([{ & 
	#pop when encounter a matching closing brackets )]}
	for i in range(0, len(s)):
		if s[i] in d.keys():
			p_list.append(s[i])
		else:
			if len(p_list) != 0:
				if s[i] == d[p_list[-1]]:
					p_list.pop()
				else:
					return False
			else:
				return False

	return (len(p_list)==0)



def main():
	par_string = r'{ { } [ ] [ [ [ ] ] ] } '
	print(f'Input {par_string} is: ' + str(isValid(par_string)))

if __name__ == '__main__':
	main()
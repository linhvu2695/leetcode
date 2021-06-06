'''
	Given integer array nums, return the third maximum number in this array. 
	If the third maximum does not exist, return the maximum number.
'''

#use set
def thirdMax(nums):
	maxset = set()
	        
	for item in nums:
		maxset.add(item)
		if len(maxset) > 3:
			maxset.remove(min(maxset))

	if len(maxset) == 3:
		return min(maxset)
	return max(maxset)

def main():
	nums = [2,2,3,1]
	print(thirdMax(nums))

if __name__ == '__main__':
	main()
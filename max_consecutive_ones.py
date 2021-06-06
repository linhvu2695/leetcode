'''
	Given a binary array nums, 
	return the maximum number of consecutive 1's in the array.
'''

def maxOnes(nums):
	max = 0
	streak = 0

	for i in range(0, len(nums)):
		if nums[i] == 1:
			streak += 1
			if streak > max:
				max = streak
		else:
			streak = 0

	return max

def main():
	print(maxOnes([1,1,0,1,1,1]))


if __name__ == '__main__':
	main()
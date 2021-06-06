'''
	Given an integer array nums sorted in non-decreasing order, 
	return an array of the squares of each number sorted in non-decreasing order.
'''

def sortedSquares(nums):
	squares = []
	l = 0
	r = len(nums)-1

	while l <= r:
		if nums[l]*nums[l] > nums[r]*nums[r]:
			squares.append(nums[l]*nums[l])
			l += 1
		else:
			squares.append(nums[r]*nums[r])
			r -= 1

	return squares[::-1]


def main():
	print(sortedSquares([-4,-1,0,3,10]))


if __name__ == '__main__':
	main()
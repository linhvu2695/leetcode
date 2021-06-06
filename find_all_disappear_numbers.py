'''
	Given an array nums of n integers where nums[i] is in the range [1, n], 
	return an array of all the integers in the range [1, n] that do not appear in nums.
'''

#nums:    | 7 8 9 5 6 3 7 3 9 |
#counters:| 1 2 3 4 5 6 7 8 9 |
#indices: | 0 1 2 3 4 5 6 7 8 |

#without using extra memory (counters array), we can still use the indices as our counter
def findDisappearNumbers(nums):
	n = len(nums)

	#mark elements with indices among the array's values
	for i in range(0, n):
		idx = abs(nums[i]) - 1
		#if unread (+ve), then mark as read
		if nums[idx] > 0:
			nums[idx] *= -1

	for i in range(n):
		if nums[i] > 0:
			nums[i] = i + 1

	i = 0
	while i < n:
		if nums[i] < 0:
			nums.pop(i)
			n -= 1
		else:
			i += 1


	return nums

def main():
	arr = [5, 6, 1, 5, 6, 1]
	print (findDisappearNumbers(arr))

if __name__ == '__main__':
	main()
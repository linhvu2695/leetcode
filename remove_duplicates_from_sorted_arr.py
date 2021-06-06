'''
	Given a sorted array nums, remove the duplicates in-place such that 
	each element appears only once and returns the new length.
'''

def removeDup1(arr):
	i = 0
	while i < len(arr)-1:
		if arr[i] == arr[i+1]:
			arr.remove(arr[i+1])
		else:
			i += 1

	return(arr, len(arr))

#check for all duplicated and remove them all at once, since remove operation is time-consuming
def removeDup2(nums):
	i = 0
	while  i < len(nums)-1:
		if nums[i] == nums[i+1]:
			j = i+1
			while j < len(nums)-1:
				if nums[j] != nums[j+1]:
					break
				else:
					j += 1
			del nums[i+1:j+1]
		i += 1

	return (nums,len(nums))

#two-pointers approach: 
#read_ptr scan the array & tell write_ptr to write a new values when found new unique value
def removeDup3(nums):
	w = 1

	for r in range(1, len(nums)):
		if nums[r] != nums[r-1]:
			nums[w] = nums[r]
			w += 1
	del nums[w+1:len(nums)]

	return (nums, w)

def main():
	arr = [0,0,1,1,1,2,2,3,3,4]
	arr, length = removeDup3(arr)
	print('New array: ' + str(arr))
	print('Length of new array: ' + str(length))


if __name__ == '__main__':
	main()
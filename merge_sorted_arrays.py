'''
	Given two sorted integer arrays nums1 and nums2, 
	merge nums2 into nums1 as one sorted array.
'''

def mergeSortedArrays(nums1, m, nums2, n):
	ptr1 = 0
	ptr2 = 0

	while (ptr1 < m) & (ptr2 < n):
		if nums1[ptr1] > nums2[ptr2]:
			nums1.insert(ptr1, nums2[ptr2])
			nums1.pop()
			ptr1 += 1
			ptr2 += 1
			m += 1
		else:
			ptr1 += 1

	if ptr2 < n:
		while ptr2 < n:
			nums1.insert(ptr1,nums2[ptr2])
			nums1.pop()
			ptr1 += 1
			ptr2 += 1


def main():
	nums1 = [1,2,3,0,0,0]
	m = 3
	nums2 = [2,5,6]
	n = 3
	mergeSortedArrays(nums1, m, nums2, n)
	print(nums1)

if __name__ == '__main__':
	main()

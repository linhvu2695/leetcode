''''
Given an array of integers nums and an integer target
Return indices of the two numbers such that they add up to target.
'''

#brute force
def twoSum1(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


#Hash Table: reduce lookup time froom O(n) to O(1) by trading space for speed
def twoSum2(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range (0, len(nums)):
            hashMap[nums[i]] = i
        
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if (hashMap.has_key(complement)) & (hashMap[complement] != i):
                return [i, hashMap[complement]]

def main():
    print('Approach 1: ', twoSum1(nums=[2,7,11,15], target=9))
    print('Approach 2: ', twoSum1(nums=[2,7,11,15], target=9))


if __name__ == '__main__':
	main()
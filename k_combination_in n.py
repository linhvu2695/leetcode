def combine(n, k):
	def backtrackNum(left_pointer, remain, result):
		for i in range(left_pointer, n-remain+1):
			#place candidate
			result.append(list_num[i])
			remain -= 1

			if remain != 0:
				#backtrack next candidate
				backtrackNum(i+1, remain, result)
			else:
				result_list.append(list(result))
			
			#remove candidate
			result.pop()
			remain += 1
			
		return

	#initialize list n
	list_num = []
	for i in range(n):
		list_num.append(i+1)
	n = len(list_num)
	
	result_list = []
	backtrackNum(0, k, [])

	return result_list

print('Results: ', combine(6, 4))


'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.
'''

def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    size_max = 0
    stack = []
    n = len(heights)
    
    for i in range(n):
        if not stack:
            stack.append([heights[i], i])
        else:
            if heights[i] >= stack[-1][0]:
                stack.append([heights[i], i])
            else:
                #most recent rectangle cannot extend
                while heights[i] < stack[-1][0]:
                    top_idx = stack[-1][1]
                    size_max = max(size_max, stack[-1][0]*(i-top_idx))
                    stack.pop()
                    if not stack:
                        break
                stack.append([heights[i], top_idx])  #indexed with the index of the latest removed item
    
    #clear the rest of the stack
    while stack:
        top_idx = stack[-1][1]
        size_max = max(size_max, stack[-1][0]*(n-top_idx))
        stack.pop()
        
            
    return size_max

def main():
    heights = [2,1,5,6,2,3]
    print(largestRectangleArea(heights))

if __name__ == '__main__':
	main()
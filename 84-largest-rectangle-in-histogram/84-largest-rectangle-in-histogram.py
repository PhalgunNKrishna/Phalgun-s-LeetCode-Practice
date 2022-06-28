class Solution:
    
    # MOST INTUITIVE APPROACH
    # Basically, find area of all the possible rectangles. for each rectangle, find the shortest height (hence third for loop)
    def alargestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                minHeight = inf
                for k in range(i, j + 1):
                    minHeight = min(minHeight, heights[k])
                maxArea = max(maxArea, minHeight * (j - i + 1))
        
        return maxArea
    
    # I don't need to iterate through all the bars between i and j to find the minHeight
    def blargestRectangleArea(self, heights: List[int]) -> int:
         
        maxArea = 0
        
        for i in range(len(heights)):
            minHeight = heights[i]
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                maxArea = max(maxArea, minHeight * (j - i + 1))
                
        return maxArea
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area
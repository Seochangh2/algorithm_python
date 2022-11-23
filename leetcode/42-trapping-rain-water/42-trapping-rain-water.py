class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol = 0
        max_height = max(height)
        left , right = 0 , len(height) -1
        max_left , max_right = height[left],height[right]
        
        while(left<right):
            max_left , max_right = max(height[left],max_left) , max(height[right],max_right)
            
            if max_left <= max_right and max_height >= max_left:
                vol += max_left - height[left]
                left +=1
                
            elif max_left > max_right and max_height >= max_right :
                vol += max_right - height[right]
                right -=1 
                
        return vol
            
            
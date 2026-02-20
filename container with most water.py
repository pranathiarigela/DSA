def area(height):
    left=0
    right=len(height)-1
    maxarea=0
    while left<=right:
        width=right-left
        h=min(height[left],height[right])
        area=width*h
        maxarea=max(area,maxarea)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return maxarea
height=[1,8,6,2,5,4,8,3,7]
print(area(height))
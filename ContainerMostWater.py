#Find two lines, which together with x-axis forms a container, 
# such that the container contains the most water.
def maxArea(height):
    maxArea=0
    for i in range(len(height)):
        remaining = height[i+1:]
        distance = 0
        for j in remaining:
            distance+= 1
            area = (min(j,height[i])) * distance
            if area >maxArea:
                maxArea=area
    return maxArea

def maxArea(h):
        water = 0
        l, r = 0, len(h)-1
        while l < r:
            if h[l] <= h[r]:
                water = max(water, (r-l) * h[l])
                l += 1
            else:
                water = max(water, (r-l) * h[r])
                r -= 1
        return water
print(maxArea([1,8,6,2,5,4,8,3,7]))
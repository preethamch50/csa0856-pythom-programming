#Given n non-negative integers a1,a2,a3,…an where each represents a point at coordinate (i, ai) . „ n „ vertical lines are drawn such that the two endpoints of line i is at (i, ai) nd (i,0). Find two lines, which together with x-axis forms a container, such that the container contains the most water. The program should return an integer which corresponds to the maximum area of water that can be contained (maximum area instead of maximum volume sounds weird but this is the 2D plane we are working with for simplicity).

Sol:
def maxArea(A, Len) :
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
           
            # Calculating the max area
            area = max(area, min(A[j], A[i]) * (j - i))
    return area
 
# Driver code
a = [ 1, 5, 4, 3 ]
 
len1 = len(a)
print(maxArea(a, len1))

#Output:
6

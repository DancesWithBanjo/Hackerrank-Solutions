# Checks a 2d array for the greatest "hourglass"
# an hourglass is the sum of the following selection in 2d array
# Example:
#
#    a b c      1 2 3        
#      d          4    --> 28              
#    e f g      5 6 7

def hourglassSum(arr):
    max_sum = 0
    total = 0

    if len(arr) < 3:
        return -1

    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            total = (arr[i][j]+arr[i][j+1]+arr[i][j+2])+(arr[i+1][j+1])+(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            if (total > max_sum):
                max_sum = total
    return max_sum
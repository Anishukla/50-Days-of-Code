# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Easy

# Complete the hourglassSum function below.
def hourglassSum(arr):
    val = []
    for i in range(1, 5):
        for j in range(1, 5):
            val.append(arr[i-1][j-1] + arr[i-1][j]+ arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1] + arr[i][j])

    return max(val)
        

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
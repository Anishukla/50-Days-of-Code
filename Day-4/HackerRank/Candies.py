# Complete the candies function below.
# Level :- Medium
def candies(n, A):
    c = [1]*n
    for i in range(n-1):
        if A[i+1]>A[i]:           
            c[i+1] = c[i]+1

    for j in range(n-1, 0, -1):
        if A[j-1]>A[j] and c[j-1]<=c[j]:
            c[j-1] = c[j]+1
            
    res = sum(c)
    return res

if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    res = candies(n, arr)
    print(res)
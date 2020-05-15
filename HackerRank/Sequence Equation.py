# Complete the permutationEquation function below.
# Level:Easy
def permutationEquation(A, N):
    di = {}
    L = []

    for i in range(N):
        di.update({A[i]:i+1})
        
    for j in range(1, N+1):
        val = di[j]
        req = di[val]
        L.append(req)

    return L

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    res = permutationEquation(p, n)
    print(res)
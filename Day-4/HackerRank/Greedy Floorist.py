import math
# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if k<len(c):
        c = sorted(c, reverse=True)
        val = 0
        count = math.ceil(len(c)/k)
        
        for i in range(1, count):
            for j in range(k):
                val = val + i*c[k*(i-1)+j]
                
        req = len(c)%k
            
        if req==0:
            r=k
            for p in range(len(c)-r, len(c)):
                val = val + count*c[p]
                
        else:
            for p in range(len(c)-req, len(c)):
                val = val + count*c[p]

        return val
        
    else:
        return sum(c)

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
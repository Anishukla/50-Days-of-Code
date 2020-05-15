T = int(input())
j = T
for i in range(T): 
    N=int(input())
    if N<4:
        print(1)
        print(N,end=" ")
        for i in range(N):
            print(i+1,end=" ")
        
    else:
        req=4
        print(int(N/2))
        print(3,1,2,3)
        while req<N:
            if N-req>=1:
                print(2, req, req+1)
                req=req+2
                
        if N%2==0:
            print(1, N)

            
    
    while(j > 1):
        j = j//2

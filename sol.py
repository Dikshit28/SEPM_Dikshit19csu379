def solve(n,A,x,k):
        #code here
        dis=[]
        for i in range(len(A)-1):
            dis.append(A[i+1]-A[i])
        i=0
        while(k>0 or i<n-1):
            if x>dis[i]:
                x-=dis[i]
            else:
                k-=1
            i+=1
        return i+1

n,x,k=map(int,input().strip().split())
A=[int(i) for i in input().strip().split()]
ans=solve(n,A,x,k)
print(ans)
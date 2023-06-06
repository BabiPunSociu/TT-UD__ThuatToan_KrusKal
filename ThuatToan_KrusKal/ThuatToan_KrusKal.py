# Cây khung nhỏ nhất

F=[0]*100005
def root(x):
    while F[x]: x=F[x]
    return x

if __name__ == "__main__":
    n,m=map(int,input().split())
    A=[]
    for i in range(m):
        u,v,w=map(int,input().split())
        A.append((u,v,w))
    A.sort(key = lambda x: x[2])
    res=0
    for u,v,w in A:
        x=root(u)
        y=root(v)
        if x!=y:
            while u!=x :
                z=F[u]
                F[u]=x 
                u=z
            while v!=y :
                z=F[v]
                F[v]=x #chu y day van la x
                v=z
            F[y]=x 
            res += w 
    print(res)

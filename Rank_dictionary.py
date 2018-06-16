def main():
    n=str(input())
    order=sorted(n)
    vis={}
    for i in n:
        vis[i]=0        
    j=0 ; rank=1 ; i=0
    while len(order)!=0:       
        if n[j]==order[i]:
            del order[i]
            i=0
            j+=1
            for k in order:
                vis[k]=0
            continue
        else:
            if vis[order[i]]:
                i+=1
                continue
            vis[order[i]]=1
            rank+=int(fact(len(order)-1)/repeat(order,i))
        i+=1
    print(rank)

def fact(i):
    if not i:
        return 1
    return i*fact(i-1)

def repeat(order,k):
    vis=[0]*len(order)
    vis[k]=1 ; repeat=1
    for i in range(len(order)):
        count=1
        if not vis[i]:
            for j in range(i+1,len(order)):
                if not vis[j] and order[i]==order[j]:
                    vis[j]=1
                    count+=1
        repeat*=fact(count)
    return repeat

main()

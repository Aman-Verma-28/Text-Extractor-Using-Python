for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    for i in range(n-1):
        x=l[i]
        y=l[i+1]
        while x*2<y:
            count+=1
            x*=2
    print(count)
li = list(map(int,input().split()))
n=len(li)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(li[j]>li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]
print(li)

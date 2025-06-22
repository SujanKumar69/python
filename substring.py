s=input()
substring=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        substring.append(s[i:j])
substring=[i for i in substring if s.count(i)>2]
print(substring[-1])

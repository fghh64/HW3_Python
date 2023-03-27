a=list(map(int, input().split()))
s=0
for i in range(len(a)):
    for j in range(i+1, len(a)):
            if a[i]==a[j]:
                  s=s+1
print(s)

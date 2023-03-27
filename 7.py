k=input()
i="f"
k1=k.find(i)
k2=k.rfind(i)
if k1==k2 and k1 != -1:
    print(k1)
elif k1 != k2:
    print(k1,k2)

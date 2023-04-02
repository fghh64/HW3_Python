def IsSymmetric():
    a=int(input())
    m=[]
    c=0 #счет
    for i in range(a):
        r=list(map(int,input().split())) #вводим матрицу
        m.append(r)
    d=m[a-1][0] #запоминаем левое нижнее число
    for j in range(a):
        if m[a-1-j][j]==d: #сравниваем прошлое число с числами идущими по диагонале
            c=c+1
    return a==c
print(IsSymmetric())


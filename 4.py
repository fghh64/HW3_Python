d=int(input())
k=['Манная','Гречневая','Пшенная','Овсяная','Рисовая']
for i in range(0, d):
    v=k[i%len(k)]
    print(v)
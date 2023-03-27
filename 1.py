def can_eat():
    x, y = map(int, input().split())
    x1, y1 = map(int, input().split())
    if (x+2==x1 and (y+1==y1 or y-1==y1)):
        print(True)
    elif (x+1==x1 and (y+2==y1 or y-2==y1)):
        print(True)
    elif (x-2==x1 and (y+1==y1 or y-1==y1)):
        print(True)
    elif (x-1==x1 and (y+2==y1 or y-2==y1)):
        print(True)
    else:
        print(False)
can_eat()
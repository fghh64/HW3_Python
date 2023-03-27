s=list(map(int, input().split()))
s.insert(0, (s[len(s)-1]))
s.pop()
print(*s)
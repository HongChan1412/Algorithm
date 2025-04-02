n, m = map(int, input().split(" "))
a = []
res = ""
for i in range(1, n+1):
    a.append(i)
for _ in range(m):
    i, j = map(int, input().split(" "))
    a[i-1], a[j-1] = a[j-1], a[i-1]
for idx, i in enumerate(a):
    if idx+1 == len(a):
        res += f"{i}"
    else:
        res += f"{i} "
print(res)

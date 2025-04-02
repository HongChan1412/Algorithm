n, m = map(int, input().split(" "))
a = []
res = ""
for i in range(n):
    a.append(0)
for _ in range(m):
    i, j, k = map(int, input().split(" "))
    for _ in range(i, j+1):
        a[_-1] = k
        a[_-1] = k
for idx, i in enumerate(a):
    if idx+1 == len(a):
        res += f"{i}"
    else:
        res += f"{i} "
print(res)
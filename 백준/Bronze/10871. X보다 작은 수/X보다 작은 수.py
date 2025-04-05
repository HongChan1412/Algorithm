n, x = map(int, input().split(" "))
c = list(map(int, input().split(" ")))
res = ""
for idx, i in enumerate(c):
    if i < x:
        if idx+1 == n:
            res += f"{i}"
        else:
            res += f"{i} "
print(res)
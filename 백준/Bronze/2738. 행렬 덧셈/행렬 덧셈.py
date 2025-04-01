N, M = map(int, input().split())
a, b = [], []
for i in range(N):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(N):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(N):
    for j in range(M):
        print(a[i][j] + b[i][j], end=" ")
    print()
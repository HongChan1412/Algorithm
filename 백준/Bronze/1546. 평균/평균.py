res = 0.0
n = int(input())
a = list(map(int, input().split(" ")))
a_max = max(a)
for i in a:
    res += i/a_max*100
print(res/n)
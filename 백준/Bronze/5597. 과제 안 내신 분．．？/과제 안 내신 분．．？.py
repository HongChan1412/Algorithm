a = []
for i in range(1, 31):
    a.append(i)
for i in range(28):
    a.remove(int(input()))
for i in a:
    print(i)
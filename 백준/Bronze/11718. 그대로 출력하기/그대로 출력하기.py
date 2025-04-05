lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except:
        break

for i in lines:
    print(i)
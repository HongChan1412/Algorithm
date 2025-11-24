str = input()
answer = ""
for i in str:
    if i >= "a" and i <= "z":
        answer += i.upper()
    elif i >= "A" and i <= "Z":
        answer += i.lower()
print(answer)

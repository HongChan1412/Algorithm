N = int(input())
res = 0
for i in range(N):
    s = list(input())
    s_list = []
    if_word = True
    for j in range(len(s)):
        if s[j] in s_list:
            if_word = False
            break
        if j != len(s)-1:
            if s[j] != s[j+1]:
                s_list.append(s[j])
    if if_word:
        res += 1

print(res)
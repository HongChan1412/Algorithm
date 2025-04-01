s = input()
s = list(s.upper())
s_dict = {}
for i in s:
    if i not in s_dict:
        s_dict[i] = 0
    s_dict[i] += 1
res = 0
res_tf = True
for k, v in s_dict.items():
    if v > res:
        res = v
        res_v = k
        res_tf = True
    elif v == res:
        res_tf = False
if res_tf:
    print(res_v)
else:
    print("?")
cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()
n = len(s)
res = 0

def replace_cro(s, i):
    global res, n
    if i in s:
        s = s.replace(i, " "*len(i), 1)
        res += 1
        n -= len(i)
        return replace_cro(s, i)
    return s

for i in cro_list:
    s = replace_cro(s, i)
print(n+res)
h, m = map(int, input().split(" "))
term = int(input())
term_h, term_m = divmod(term, 60)
m += term_m
h += term_h
if m > 59:
    h = h + 1
    m = m - 60
if h > 23:
    h = h - 24
print(h, m)
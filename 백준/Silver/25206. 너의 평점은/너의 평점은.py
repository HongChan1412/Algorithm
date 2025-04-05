grades = 0.0
scores = 0.0
scr_dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for i in range(20):
    name, grade, scr = map(str, input().split())
    if scr == "P":
        continue
    grades += float(grade)
    scores += scr_dict.get(scr) * float(grade)

print(scores / grades)
def solution(spell, dic):
    answer = 0
    answer = 2
    for i in dic:
        spell_in = True
        for j in spell:
            if j not in i:
                spell_in = False
                break
        if spell_in:
            answer = 1
            break
    return answer
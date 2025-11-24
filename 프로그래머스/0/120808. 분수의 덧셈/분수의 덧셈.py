def solution(numer1, denom1, numer2, denom2):
    answer = []
    bunja1 = numer1 * denom2
    bunja2 = numer2 * denom1
    
    bunja = bunja1 + bunja2
    bunmo = denom1 * denom2
    
    answer = [bunja, bunmo]
    for i in reversed(range(2, 1000000)):
        if bunmo % i == 0 and bunja % i == 0:
            if bunmo == bunja:
                answer = [1, 1]
                return answer
            print(i)
            answer = [int(bunja / i), int(bunmo / i)]
            return answer
    
    return answer
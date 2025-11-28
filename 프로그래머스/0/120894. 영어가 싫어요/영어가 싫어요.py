def solution(numbers):
    answer = 0
    answer = ""
    numbers_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    temp = ""
    for i in numbers:
        temp += i
        if temp in numbers_list:
            if temp == "zero":
                answer += "0"
            elif temp == "one":
                answer += "1"
            elif temp == "two":
                answer += "2"
            elif temp == "three":
                answer += "3"
            elif temp == "four":
                answer += "4"
            elif temp == "five":
                answer += "5"
            elif temp == "six":
                answer += "6"
            elif temp == "seven":
                answer += "7"
            elif temp == "eight":
                answer += "8"
            elif temp == "nine":
                answer += "9"
            temp = ""
    answer = int(answer)
    return answer
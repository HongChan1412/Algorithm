s = input()

def judge_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return judge_palindrome(s[1:-1])
    else:
        return False

if judge_palindrome(s):
    print(1)
else:
    print(0)